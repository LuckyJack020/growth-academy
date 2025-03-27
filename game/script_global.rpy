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
define PRG2 = Character('Aida', color="#FF3399") #normal speaking voice
define PRGCell = Character('Aida', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="PRGCell")
define AltPRGCell = Character('Aida', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}') #hidden picture
define WG = Character('Alice', color="#CC33FF")
define WGCell = Character('Alice', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="WGCell")

define MC_FMG = Character('Keisuke & Akira', color="#C0C0C0")
define MC_BE = Character('Keisuke & Honoka', color="#C0C0C0")

#Supporting Cast
define Chibuki = Character('Chibuki', color="#CC33FF")
define ChibukiCell = Character('Chibuki', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="ChibukiCell")
define Jineko = Character('Jineko', color="#228B22")
define Kanami = Character('Kanami', color="#C0C0C0")
define Kokutan = Character('Kokutan', color="#C0C0C0")
define Minori = Character('Minori', color="#FF91DC")
define Natsuko = Character('Natsuko', color="#8E0C0C")
define Okisho = Character('Okisho', color="#8D2394", what_prefix='{size=+2}', what_suffix='{/size}')
define RM = Character('Daichi', color="#BDB8A5")
define Ryoko = Character('Ryoko', color="#FF91DC")
define Sakura = Character('Sakura', color="#FF3399")
define Tako = Character('Tako', color="#ce9b50")
define Yuki = Character('Yuki', color="#FF91DC")
define YukiCell = Character('Yuki', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="YukiCell")
define Yua = Character('Yua', color="#C0C0C0") #Natsuko’s Mother

#School Staff
define HR = Character('Tashi-sensei', color="#C0C0C0")
define Naoki = Character('Naoki-sensei', color="#C0C0C0")
define Nurse = Character('Nurse Kiyomi', color="#C0C0C0") #Lips
define Nurse2 = Character('Nurse Kiyomi', color="#0099CC") # Nails
define Lunch = Character('Lunchlady', color="#CC33FF")
define Hageshi = Character('Hageshi-sensei', color="#C0C0C0")
define Misuboro = Character('Misuboro', color="#0099CC")
define Principal = Character('Principal Noguchi', color="#C0C0C0")
define Sugiyama = Character('Sugiyama-sensei', color="#C0C0C0")
define Takamura = Character('Takamura-sensei', color="#C0C0C0")
define Tsubasa = Character('Tsubasa-sensei', color="#C0C0C0")

#Parents and Other Relatives
define Akihiro = Character('Akihiro', color="#C0C0C0") #Naomi’s Father
define Dad = Character('Dad', color="#C0C0C0") #Keisuke’s Father
define DadCell = Character('Dad', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}') #Keisuke’s Father Cell
define Enmei = Character('Enmei', color="#C0C0C0") #Aida's Father
define Daitaro = Character('Daitaro', color="#C0C0C0") #Alice’s Father
define Fujio = Character('Fujio', color="#C0C0C0") #Honoka's Father
define FujioCell = Character('Fujio', color="#C0C0C0") #Honoka's Father
define Kazumi = Character('Kazumi', color="#C0C0C0") #Naomi’s Sister
define Midori = Character('Midori', color="#C0C0C0") #Akira’s Father
define Miko = Character('Miko', color="#C0C0C0") #Naomi’s Mother
define Minami = Character('Minami', color="#C0C0C0") #Shiori’s Mother
define Mom = Character('Mom', color="#FF3300") #Keisuke’s Mother
define MomCell = Character('Mom', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}') #Keisuke’s Mother Cell
define TakaraUnknown = Character('Aida\'s Mother', color="#C0C0C0") #Aida’s Mother
define Takara = Character('Takara', color="#C0C0C0") #Aida’s Mother
define TakaraCell = Character('Takara', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}') #Aida's Mother Cell
define Tomoko = Character('Tomo', color="#FF3300") #Keisuke’s Sister
define TomokoCell = Character('Tomo', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="TomoCell") #Keisuke’s Sister Cell
define Vivian = Character('Vivian', color="#C0C0C0") #Alice’s Mother
define Yuko = Character('Yuko', color="#FF3300") #Akira’s Mother
define YukoCell = Character('Yuko', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="YukoCell") #Akira’s Mother Cell

#Other Students
define Fumika = Character('Fumika', color="#FF91DC") #GTS Route
define Genji = Character('Genji', color="#C0C0C0") #MC Route
define Gou = Character('Gou', color="#C0C0C0") #RM Route
define Etsuko = Character('Etsuko', color="#C0C0C0") #MC Route
define Hamikawa = Character('Hamikawa', color="#C0C0C0") #AE Route
define Haruhiro = Character('Haruhiro', color="#C0C0C0") #BE Route
define Hotaru = Character('Hotaru', color="#C0C0C0") #MC Route
define Junsei = Character('Junsei', color="#C0C0C0") #RM Route
define Koneko = Character('Koneko', color="#C0C0C0") #BE Route
define Michiko = Character('Michiko', color="#C0C0C0") #PRG Route
define Sakie = Character('Sakie', color="#C0C0C0") #BE Route

#Background Characters
define Akio = Character('Akio', color="#C0C0C0") #GTS Route
define Chie = Character('Chie', color="#FF9900") #FMG Route, MC Route
define Chiyo = Character('Chiyo-san', color="#FF9900") #MC Route - Tsubasa-sensei’s wife
define Francois = Character('François', color="#CC33FF") #WG Route
define Fujimoto = Character('Fujimoto', color="#DDA510") #FMG Route
define Haruko = Character('Haruko', color="#DDA510") #FMG Route, MC Route
define Hidaka = Character('Hidaka', color="#DDA510") #FMG Route
define Katsumi = Character('Katsumi', color="#C0C0C0") #AE Route
define Lee = Character('Lee', color="#C0C0C0") #WG Route - Summer Arc
define Minei = Character('Minei', color="#C0C0C0") #FMG Route
define Misaki = Character('Misaki', color="#C0C0C0") #WG Route
define Miura = Character('Miura', color="#C0C0C0") #FMG Route
define Ren = Character('Ren', color="#C0C0C0") #Botanist: MC Route, GTS Route
define Shino = Character('Shino', color="#C0C0C0") #WG Route - Summer Arc
define Takada = Character('Takada', color="#C0C0C0") #WG Route - Summer Arc
define Wobbles = Character('Wobbles', color="#E54C84") #AE Route - Shiori's Hypnotized State

#General Use
define All = Character('Everyone', color="#ffffff")
define Announcer = Character('Announcer', color="#C0C0C0")
define Announcer2 = Character('Announcer 2', color='#C0C0C0')
define Attendant = Character('Attendant', color="#C0C0C0")
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
define Contractor = Character('Contractor', color="#C0C0C0")
define Coworker = Character('Coworker', color="#C0C0C0")
define Coworker2 = Character('Coworker2', color="#C0C0C0")
define DJ = Character('DJ', color="#C0C0C0")
define Driver = Character('Driver', color="#C0C0C0")
define FemStudent1 = Character('Female Student 1', color="#ce6950") #New color maybe?
define FemStudent2 = Character('Female Student 2', color="#ce9b50") #New color maybe?
define Giant1 = Character('Giant 1', color="#C0C0C0")
define Giant2 = Character('Giant 2', color="#C0C0C0")
define Girls = Character('Girls', color="#ffffff")
define Guard = Character('Guard', color="#C0C0C0")
define Hostess = Character('Hostess', color="#C0C0C0")
define Intercom = Character('Intercom', color="#C0C0C0")
define Interviewer = Character('Interviewer', color="#C0C0C0")
define Judge = Character('Judge', color="#C0C0C0")
define LittleGirl = Character('Little Girl', color="#FF91DC")
define Lifeguard = Character('Lifeguard', color="#C0C0C0")
define Letter = Character('Letter', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Local = Character('Local', color="#C0C0C0")
define Magician = Character('Magician', color="#C0C0C0")
define Manager = Character('Manager', color="#C0C0C0")
define Masseuse1 = Character('Masseuse 1', color="#C0C0C0")
define Masseuse2= Character('Masseuse 2', color="#C0C0C0")
define Note = Character('Note', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Owner = Character('Store Owner', color="#C0C0C0")
define Postwoman = Character('Postwoman', color="#C0C0C0")
define Receptionist = Character('Receptionist', color="#C0C0C0")
define Referee = Character('Referee', color="#C0C0C0")
define Secretary1 = Character('Secretary 1', color="#C0C0C0")
define Secretary2 = Character('Secretary 2', color="#C0C0C0")
define Secretary3 = Character('Secretary 3', color="#C0C0C0")
define Stewardess = Character("Stewardess", color="C0C0C0")
define Student = Character('Student', color="#FF3300")
define Student1 = Character('Student 1', color="#FF3300")
define Student2 = Character('Student 2', color="#FF3300")
define Student3 = Character('Student 3', color="#FF3300")
define Student4 = Character('Student 4', color="#FF3300")
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
image NYI = "Graphics/ui/bg/NYI.webp"

#Campus
image Admin Hallway = "Graphics/ui/bg/hallway.webp"
image Art Classroom = DynamicImage("Graphics/ui/bg/artroom_[gametime].webp")
image Auditorium = DynamicImage("Graphics/ui/bg/archiveBG/auditorium_[gametime].webp")
image Auditorium Storage = DynamicImage("Graphics/ui/bg/archiveBG/auditoriumstorage_[gametime].webp")
image Bathroom = "Graphics/ui/bg/archiveBG/bathroom.webp"
image Biology Lab = DynamicImage("Graphics/ui/bg/archiveBG/biologylab_[gametime].webp") #Biology Laboratory Classroom
image Cafeteria = "Graphics/ui/bg/archiveBG/cafeteria.webp"
image Campus Center = DynamicImage("Graphics/ui/bg/archiveBG/campuscenter_[gametime].webp")
image Classroom = DynamicImage("Graphics/ui/bg/classroom_[gametime].webp") #Tashi-sensei's Homeroom Classroom
image ClassroomAlt = DynamicImage("Graphics/ui/bg/classroom_alt_[gametime].webp") #Tashi-sensei's Homeroom Classroom - Alternate View
image Classroom2 = DynamicImage("Graphics/ui/bg/archiveBG/classroom_2_[gametime].webp") #Takamura-sensei's Homeroom Classroom
image Classroom3 = DynamicImage("Graphics/ui/bg/classroom_3_[gametime].webp") #Tsubasa-sensei's Homeroom Classroom
image Classroom4 = DynamicImage("Graphics/ui/bg/archiveBG/classroom_4_[gametime].webp") #Hageshi-sensei's Homeroom Classroom
image Coach Office = DynamicImage("Graphics/ui/bg/archiveBG/coachoffice_[gametime].webp")
image Clock Tower = DynamicImage("Graphics/ui/bg/clocktower_[gametime].webp")
image Computer Room = DynamicImage("Graphics/ui/bg/computerroom_[gametime].webp")
image Cooking Classroom = "Graphics/ui/bg/cooking.webp"
image Faculty Room = DynamicImage("Graphics/ui/bg/archiveBG/facultyroom_[gametime].webp")
image Gate Front = "Graphics/ui/bg/gatefront.webp"
image Gym = DynamicImage("Graphics/ui/bg/gym_[gametime].webp")
image Hallway = DynamicImage("Graphics/ui/bg/archiveBG/schoolhallway1_[gametime].webp")
image Hallway2 = DynamicImage("Graphics/ui/bg/archiveBG/schoolhallway2_[gametime].webp")
image HallwayStairs = DynamicImage("Graphics/ui/bg/schoolhallway_[gametime].webp") #Hallway3
image Hospital Room = "Graphics/ui/bg/NYI.webp"
image Info Desk = DynamicImage("Graphics/ui/bg/archiveBG/infodesk_[gametime].webp")
image Library = DynamicImage("Graphics/ui/bg/archiveBG/library_[gametime].webp")
image Lockers = DynamicImage("Graphics/ui/bg/lockers_[gametime].webp")
image Lockers Showers = "Graphics/ui/bg/archiveBG/lockers_showers.webp"
image Music Classroom = DynamicImage("Graphics/ui/bg/archiveBG/music_[gametime].webp")
image Nurse Office = DynamicImage("Graphics/ui/bg/archiveBG/nurseoffice_[gametime].webp")
image Office = DynamicImage("Graphics/ui/bg/archiveBG/office_[gametime].webp")
image Pool = DynamicImage("Graphics/ui/bg/archiveBG/schoolpool_[gametime].webp")
image Principal Office = DynamicImage("Graphics/ui/bg/archiveBG/principaloffice_[gametime].webp")
image Recreation = "Graphics/ui/bg/NYI.webp"
image Roof = DynamicImage("Graphics/ui/bg/roof_[gametime].webp") #Academy Building
image Roof Entrance = DynamicImage("Graphics/ui/bg/roofentrance_[gametime].webp") #Academy Building
image Roof2 = DynamicImage("Graphics/ui/bg/archiveBG/roof2_[gametime].webp") #Dorms Building
image Roof2 Fall = DynamicImage("Graphics/ui/bg/archiveBG/roof2fall_[gametime].webp") #Dorms Building
image School Exterior = DynamicImage("Graphics/ui/bg/archiveBG/schoolexterior_[gametime].webp")
image School Front = DynamicImage("Graphics/ui/bg/schoolfront_[gametime].webp")
image School Inner = "Graphics/ui/bg/schoolinner.webp"
image School Planter = "Graphics/ui/bg/archiveBG/schoolplanter_[gametime].webp"
image School Planter Winter = "Graphics/ui/bg/archiveBG/schoolplanter_winter.webp"
image School Shed = DynamicImage("Graphics/ui/bg/schoolshed_[gametime].webp")
image School Building Side = "Graphics/ui/bg/archiveBG/schoolside_[gametime].webp"
image Stage = DynamicImage("Graphics/ui/bg/archiveBG/stage_[gametime].webp")
image Student Government = DynamicImage("Graphics/ui/bg/archiveBG/studentgovernment_[gametime].webp")
image Track = DynamicImage("Graphics/ui/bg/archiveBG/track_[gametime].webp")
image Workshop = "Graphics/ui/bg/NYI.webp"

#Dorms
image Dorm Exterior = DynamicImage("Graphics/ui/bg/dormexterior_[gametime].webp")
image Dorm Entrance = DynamicImage("Graphics/ui/bg/archiveBG/dormentrance_[gametime].webp")
image Dorm Entrance Fall = DynamicImage("Graphics/ui/bg/archiveBG/dormentrancefall_[gametime].webp")
image Dorm Hallway = "Graphics/ui/bg/archiveBG/dormhallway.webp"
image Dorm Interior = DynamicImage("Graphics/ui/bg/archiveBG/dorminterior_[gametime].webp")
image Dorm AE = DynamicImage("Graphics/ui/bg/archiveBG/AEdorm_[gametime].webp")
image Dorm BE = DynamicImage("Graphics/ui/bg/archiveBG/BEdorm_[gametime].webp")
image Dorm FMG = DynamicImage("Graphics/ui/bg/FMGdorm_[gametime].webp")
image Dorm GTS = DynamicImage("Graphics/ui/bg/archiveBG/GTSdorm_[gametime].webp")
image Dorm PRG = DynamicImage("Graphics/ui/bg/PRGdorm_[gametime].webp")
image Dorm WG = DynamicImage("Graphics/ui/bg/archiveBG/WGDorm_[gametime].webp")
image Dorm Tomoko = DynamicImage("Graphics/ui/bg/TMDorm_[gametime].webp")

#Giants Facilities
image Chukan Point = DynamicImage("Graphics/ui/bg/chukanpoint_[gametime].webp")
image Courtyard GTS = "Graphics/ui/bg/NYI.webp"
image Giant Dorm Exterior = DynamicImage("Graphics/ui/bg/GTSdorm_quarry_exterior_[gametime].webp")
image Giant Dorm Interior = DynamicImage("Graphics/ui/bg/GTSdorm_quarry_interior_[gametime].webp")
image Giant Dorm Quarry = "Graphics/ui/bg/GTSDorm_quarry_rocks.webp"
image Giants Gate = DynamicImage("Graphics/ui/bg/chukanpoint_[gametime].webp")

#Seichou Town
image Arcade = DynamicImage("Graphics/ui/bg/archiveBG/arcade_[gametime].webp")
image Art Gallery = "Graphics/ui/bg/NYI.webp"
image Bakery = DynamicImage("Graphics/ui/bg/archiveBG/bakery_[gametime].webp")
image Bakery Entrance = DynamicImage("Graphics/ui/bg/archiveBG/bakeryentrance_[gametime].webp")
image Ballroom = DynamicImage("Graphics/ui/bg/archiveBG/ballroom_[gametime].webp")
image Cafe = DynamicImage("Graphics/ui/bg/archiveBG/cafe_[gametime].webp")
image Cafe Seats = DynamicImage("Graphics/ui/bg/archiveBG/cafe_seats_[gametime].webp")
image Clothes Store = "Graphics/ui/bg/archiveBG/clothesstore.webp"
image Disco Club = DynamicImage("Graphics/ui/bg/archiveBG/discoclub_[gametime].webp")
image Diner = "Graphics/ui/bg/archiveBG/burgerrestaurant.webp"
image Festival = DynamicImage("Graphics/ui/bg/archiveBG/festival_[gametime].webp")
image Festive Tent = "Graphics/ui/bg/NYI.webp"
image Flower Field = DynamicImage("Graphics/ui/bg/archiveBG/flowerfield_[gametime].webp")
image Game Store = "Graphics/ui/bg/archiveBG/gamestore.webp"
image Hotel Exterior = DynamicImage("Graphics/ui/bg/archiveBG/hotelexterior_[gametime].webp")
image Hotel Room = DynamicImage("Graphics/ui/bg/archiveBG/hotelroom_[gametime].webp")
image Hotel Desk = DynamicImage("Graphics/ui/bg/archiveBG/hoteldesk.webp")
image Hotel Elevator = DynamicImage("Graphics/ui/bg/archiveBG/hotelelevator.webp")
image Hotel Lobby = DynamicImage("Graphics/ui/bg/archiveBG/hotellobby_[gametime].webp")
image Hotel Lounge = DynamicImage("Graphics/ui/bg/archiveBG/hotellounge_[gametime].webp")
image Hotel Restaurant = "Graphics/ui/bg/archiveBG/hotelrestaurant.webp"
image Mall = "Graphics/ui/bg/archiveBG/mall.webp"
image Mall Candyshop = "Graphics/ui/bg/archiveBG/mall_candyshop.webp"
image Movie Theater = "Graphics/ui/bg/archiveBG/movietheater.webp"
image Movie Theater Lights = "Graphics/ui/bg/archiveBG/movietheater_lights.webp"
image Movie Theater Exterior = DynamicImage("Graphics/ui/bg/archiveBG/movietheaterext_[gametime].webp")
image Park = DynamicImage("Graphics/ui/bg/archiveBG/park_[gametime].webp")
image Pharmacy = DynamicImage("Graphics/ui/bg/archiveBG/pharmacy_[gametime].webp")
image Restaurant = "Graphics/ui/bg/restaurant.webp"
image Sound Studio = DynamicImage("Graphics/ui/bg/archiveBG/soundstudio_[gametime].webp")
image Store = DynamicImage("Graphics/ui/bg/store_[gametime].webp")
image Supermarket = DynamicImage("Graphics/ui/bg/archiveBG/supermarket_[gametime].webp")
image Sushi Restaurant = "Graphics/ui/bg/archiveBG/sushirestaurant.webp"
image Sushi Restaurant Seats = "Graphics/ui/bg/archiveBG/sushirestaurant_seats.webp"
image Theater Concert = "Graphics/ui/bg/archiveBG/theater-concert.webp"
image Theater Concert Spotlight = "Graphics/ui/bg/archiveBG/theater-concert-spotlight.webp"
image Theater Exterior = DynamicImage("Graphics/ui/bg/theater-exterior_[gametime].webp")
image Theater Interior = "Graphics/ui/bg/theater-interior.webp"
image Theater Interior Spotlight = "Graphics/ui/bg/theater-interior-spotlight.webp"
image Town = DynamicImage("Graphics/ui/bg/archiveBG/town_[gametime].webp")
image Town Alley = DynamicImage("Graphics/ui/bg/archiveBG/townalley_[gametime].webp")
image Town Bus = DynamicImage("Graphics/ui/bg/archiveBG/townbus_[gametime].webp")
image Town Docks = DynamicImage("Graphics/ui/bg/archiveBG/towndocks_[gametime].webp")
image Town Shops = DynamicImage("Graphics/ui/bg/archiveBG/townshops_[gametime].webp")
image Town Street = DynamicImage("Graphics/ui/bg/archiveBG/townstreet_[gametime].webp")
image Waterpark = DynamicImage("Graphics/ui/bg/archiveBG/waterpark_[gametime].webp")
image Waterpark Pool = DynamicImage("Graphics/ui/bg/archiveBG/waterparkpool_[gametime].webp")

#Satoyama Village
image Ryokan Onsen = DynamicImage("Graphics/ui/bg/archiveBG/ryokanonsen_[gametime].webp")
image Ryokan Onsen Steamed = DynamicImage("Graphics/ui/bg/archiveBG/ryokanonsen_steamed_[gametime].webp")
image Ryokan Bathroom = DynamicImage("Graphics/ui/bg/archiveBG/ryokanbathroom_[gametime].webp")
image Ryokan Exterior = DynamicImage("Graphics/ui/bg/archiveBG/ryokanexterior_[gametime].webp")
image Ryokan Room = DynamicImage("Graphics/ui/bg/archiveBG/ryokanroom_[gametime].webp")

#Beachside Village
image Beach = DynamicImage("Graphics/ui/bg/archiveBG/beach_[gametime].webp")
image Frozen Beach = "Graphics/ui/bg/archiveBG/beach_frozen.webp"

#Giants Town
image Giants Town = "Graphics/ui/bg/NYI.webp"
image Giants Town Store = "Graphics/ui/bg/NYI.webp"

#Mountains
image Mountains = DynamicImage("Graphics/ui/bg/archiveBG/mountains_[gametime].webp")
image Mountains Shrine = "Graphics/ui/bg/mountains_shrine.webp"
image Mountains Torii Gate = "Graphics/ui/bg/mountains_gate.webp"

#Island
image Dock = "Graphics/ui/bg/dock_[gametime].webp"
image Field = DynamicImage("Graphics/ui/bg/archiveBG/field_[gametime].webp")
image Field Winter = DynamicImage("Graphics/ui/bg/archiveBG/field_[gametime].webp") #TBI
image Flower Clearing = DynamicImage("Graphics/ui/bg/archiveBG/flowerclearing_[gametime].webp")
image Hill Road = DynamicImage("Graphics/ui/bg/archiveBG/hillroad_[gametime].webp")
image Lake Road = DynamicImage("Graphics/ui/bg/lakeroad_[gametime].webp")
image Night Sky = "Graphics/ui/bg/archiveBG/night_sky.webp"
image Temple = DynamicImage("Graphics/ui/bg/archiveBG/temple_[gametime].webp")
image Temple Fall = DynamicImage("Graphics/ui/bg/archiveBG/templefall_[gametime].webp")
image View Point = DynamicImage("Graphics/ui/bg/archiveBG/viewpoint_[gametime].webp")
image Woods = DynamicImage("Graphics/ui/bg/archiveBG/woods_[gametime].webp")
image Woods Winter = "Graphics/ui/bg/archiveBG/woods_winter.webp"

#Alice’s Summer Estate
image RV Interior = "Graphics/ui/bg/WG_summer_rv.webp"
image Summer Balcony Exterior = DynamicImage("Graphics/ui/bg/WG_summer_balcony_ext_[gametime].webp")
image Summer Balcony Interior = DynamicImage("Graphics/ui/bg/WG_summer_balcony_ext_[gametime].webp")
image Summer Beach = DynamicImage("Graphics/ui/bg/WG_summer_beach_[gametime].webp")
image Summer Beach Closed = "Graphics/ui/bg/WG_summer_beach_closed.webp"
image Summer Beach Ocean = "Graphics/ui/bg/WG_summer_beach_ocean.webp"
image Summer Bedroom = DynamicImage("Graphics/ui/bg/WG_summer_bedroom_[gametime].webp")
image Summer Dining Room = "Graphics/ui/bg/WG_summer_diningroom.webp"
image Summer Guest Bathroom = DynamicImage("Graphics/ui/bg/WG_summer_guest_bathroom_[gametime].webp")
image Summer Guest Bathroom Steamed = DynamicImage("Graphics/ui/bg/WG_summer_guest_bathroom_steamed_[gametime].webp")
image Summer Guest Bedroom = DynamicImage("Graphics/ui/bg/WG_summer_guest_bedroom_[gametime].webp")
image Summer Hallway = "Graphics/ui/bg/WG_summer_hallway.webp"
image Summer House Back = "Graphics/ui/bg/WG_summer_houseback.webp"
image Summer House Entrance = "Graphics/ui/bg/WG_summer_entrance.webp"
image Summer House Front = "Graphics/ui/bg/WG_summer_housefront.webp"
image Summer Living Room = "Graphics/ui/bg/WG_summer_livingroom.webp"

#Okinawa - FMG Arc
image Okinawa Airport = "Graphics/ui/bg/archiveBG/okinawa_airport.webp"
image Okinawa Beach = DynamicImage("Graphics/ui/bg/archiveBG/okinawa_beach_[gametime].webp")
image Okinawa Bedroom = DynamicImage("Graphics/ui/bg/archiveBG/okinawa_bedroom_[gametime].webp")
image Okinawa Cottage = "Graphics/ui/bg/archiveBG/okinawa_cottage.webp"
image Okinawa House Exterior = DynamicImage("Graphics/ui/bg/okinawa_houseexterior_[gametime].webp")
image Okinawa House Interior = DynamicImage("Graphics/ui/bg/okinawa_houseinterior_[gametime].webp")
image Okinawa House Hallway = DynamicImage("Graphics/ui/bg/okinawa_househallway_[gametime].webp")
image Okinawa Island = "Graphics/ui/bg/archiveBG/okinawa_island.webp"
image Okinawa Market = "Graphics/ui/bg/archiveBG/okinawa_market.webp"
image Okinawa Ocean = DynamicImage("Graphics/ui/bg/archiveBG/okinawa_ocean_[gametime].webp")

#Other - Tokyo
image Tokyo = DynamicImage("Graphics/ui/bg/tokyo_streets_[gametime].webp")
image Tokyo Abandoned Building = "Graphics/ui/bg/NYI.webp"
image Tokyo Architect Office = DynamicImage("Graphics/ui/bg/archiveBG/tokyo_architectoffice_[gametime].webp")
image Tokyo Club = "Graphics/ui/bg/archiveBG/tokyo_club.webp"
image Tokyo Club Alt = "Graphics/ui/bg/archiveBG/tokyo_club2.webp"
image Tokyo Club Interior = "Graphics/ui/bg/archiveBG/tokyo_clubinterior.webp"
image Tokyo Club Stage = "Graphics/ui/bg/archiveBG/tokyo_clubstage.webp"
image Tokyo Club Stage Alt = "Graphics/ui/bg/archiveBG/tokyo_clubstage2.webp"
image Tokyo House Exterior = DynamicImage("Graphics/ui/bg/tokyo_houseexterior_[gametime].webp")
image Tokyo Dining Room = "Graphics/ui/bg/NYI.webp"
image Tokyo MC Apartment = DynamicImage("Graphics/ui/bg/archiveBG/tokyo_mcapartment_[gametime].webp")
image Tokyo Mega Metro = DynamicImage("Graphics/ui/bg/archiveBG/tokyo_megametro_[gametime].webp")
image Tokyo Restaurant = DynamicImage("Graphics/ui/bg/archiveBG/tokyo_restaurant.webp")
image Tokyo Station = DynamicImage("Graphics/ui/bg/tokyo_station_[gametime].webp")
image Tokyo Train = DynamicImage("Graphics/ui/bg/tokyo_train_[gametime].webp")
image Tokyo Office = "Graphics/ui/bg/NYI.webp"

#Other - Kagoshima
image Kagoshima Aquarium = DynamicImage("Graphics/ui/bg/archiveBG/kagoshima_aquarium_[gametime].webp")

#Other - Kanagawa
image Kanagawa Street = DynamicImage("Graphics/ui/bg/archiveBG/kanagawa_street_[gametime].webp")
image Kanagawa Alley = DynamicImage("Graphics/ui/bg/archiveBG/kanagawa_alley_[gametime].webp")
image Kanagawa Game Store = "Graphics/ui/bg/archiveBG/kanagawa_gamestore.webp"
image Kanagawa Supermarket Exterior = "Graphics/ui/bg/archiveBG/kanagawa_supermarketexterior.webp"
image Kanagawa Supermarket Interior = "Graphics/ui/bg/archiveBG/kanagawa_supermarketinterior.webp"
image Kanagawa Station = DynamicImage("Graphics/ui/bg/archiveBG/kanagawa_station_[gametime].webp")

#Other - Yokohama
image Yokohama HighRise Hallway = DynamicImage("Graphics/ui/bg/archiveBG/yokohama_highrise_hallway_[gametime].webp")
image Yokohama HighRise Office = "Graphics/ui/bg/archiveBG/yokohama_highrise_office.webp"
image Yokohama HighRise Skyline = DynamicImage("Graphics/ui/bg/archiveBG/yokohama_highrise_skyline_[gametime].webp")

#General
image Airport = "Graphics/ui/bg/NYI.webp"
image Car Interior = DynamicImage("Graphics/ui/bg/archiveBG/carinterior_[gametime].webp")
image Bus Interior = DynamicImage("Graphics/ui/bg/archiveBG/businterior_[gametime].webp")
image Ferry = DynamicImage("Graphics/ui/bg/ferry_[gametime].webp")
image Plane Interior = "Graphics/ui/bg/NYI.webp"

#CG + Images
image daymenubg = "Graphics/ui/bg/archiveBG/menubg-day.webp"

image cg AE000 = "Graphics/ui/gallery/AE000.webp"
image cg AE015 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE015.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE024 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE024.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE024b = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE024b.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE024c = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE024c.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE024d = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE024d.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE024e = "Graphics/ui/gallery/AE024e.webp"
image cg AE025 = "Graphics/ui/gallery/AE025.webp"
image cg AE050_bj1 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_bj1.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_bj2 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_bj2.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_bj3 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_bj3.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_bj4 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_bj4.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_sit1 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_sit1.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_sit2 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_sit2.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_spank1 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_spank1.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_spank2 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_spank2.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_spank3 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_spank3.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_spank4 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_spank4.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_behind1 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_behind1.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_behind2 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_behind2.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_behind3 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_behind3.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_behind4 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_behind4.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_behind5 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_behind5.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE050_behind6 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE050_behind6.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE053_mirror1 = "Graphics/ui/gallery/AE053_mirror1.webp"
image cg AE053_mirror2 = "Graphics/ui/gallery/AE053_mirror2.webp"
image cg AE074_snow1 = "Graphics/ui/gallery/AE074_snow1.webp"
image cg AE074_snow2 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE074_snow2.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE074_snow3 = "Graphics/ui/gallery/AE074_snow3.webp"
image cg AE092_tv1 = "Graphics/ui/gallery/AE092_tv1.webp"
image cg AE092_tv2 = "Graphics/ui/gallery/AE092_tv2.webp"
image cg AE092_tv3 = "Graphics/ui/gallery/AE092_tv3.webp"
image cg AE098D_musicvideo1 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE098D_musicvideo1.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE098D_musicvideo2 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE098D_musicvideo2.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE098D_musicvideo3 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE098D_musicvideo3.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE098D_musicvideo4 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/AE098D_musicvideo4.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg AE098D_musicvideo5 = "Graphics/ui/gallery/AE098D_musicvideo5.webp"

image cg BE000 = "Graphics/ui/gallery/BE000.webp"
image cg BE000b = "Graphics/ui/gallery/BE000b.webp"
image cg BE001 = "Graphics/ui/gallery/BE001.webp"
image cg BE010_pov1 = "Graphics/ui/gallery/BE010_pov1.webp"
image cg BE010_pov2 = "Graphics/ui/gallery/BE010_pov2.webp"
image cg BE010_pov3 = "Graphics/ui/gallery/BE010_pov3.webp"
image cg BE010_pov4 = "Graphics/ui/gallery/BE010_pov4.webp"
image cg BE010_pov5 = "Graphics/ui/gallery/BE010_pov5.webp"
image cg BE020_date1 = "Graphics/ui/gallery/BE020_date1.webp"
image cg BE020_date2 = "Graphics/ui/gallery/BE020_date2.webp"
image cg BE020_date3 = "Graphics/ui/gallery/BE020_date3.webp"
image cg BE020_date4 = "Graphics/ui/gallery/BE020_date4.webp"
image cg BE020_date5 = "Graphics/ui/gallery/BE020_date5.webp"
image cg BE020_date6 = "Graphics/ui/gallery/BE020_date6.webp"
image cg BE020_date7 = "Graphics/ui/gallery/BE020_date7.webp"
image cg BE028 = "Graphics/ui/gallery/BE028.webp"
image cg BE028_fem = "Graphics/ui/gallery/BE028_fem.webp"
image cg BE031 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/BE031.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg BE031b = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/BE031b.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg BE031c = "Graphics/ui/gallery/BE031c.webp"
image cg BE032 = "Graphics/ui/gallery/BE032.webp"
image cg BE043_movie1 = "Graphics/ui/gallery/BE043_movie1.webp"
image cg BE043_movie2 = "Graphics/ui/gallery/BE043_movie2.webp"
image cg BE043_movie1_fem = "Graphics/ui/gallery/BE043_movie1_fem.webp"
image cg BE043_movie2_fem = "Graphics/ui/gallery/BE043_movie2_fem.webp"
image cg BE049 = "Graphics/ui/gallery/BE049.webp"

image cg FMG001 = "Graphics/ui/gallery/FMG001.webp"
image cg FMG016 = "Graphics/ui/gallery/FMG016.webp"
image cg FMG041 = "Graphics/ui/gallery/FMG041.webp"
image cg FMG050 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/FMG050.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg FMG055 = "Graphics/ui/gallery/FMG055.webp"
image cg FMG056 = "Graphics/ui/gallery/FMG056.webp"
image cg FMG058 = "Graphics/ui/gallery/FMG058.webp"
image cg FMG058_pose1 = "Graphics/ui/gallery/FMG058_pose1.webp"
image cg FMG058_pose2 = "Graphics/ui/gallery/FMG058_pose2.webp"
image cg FMG058_pose3 = "Graphics/ui/gallery/FMG058_pose3.webp"
image cg FMG061 = "Graphics/ui/gallery/FMG061.webp"
image cg FMG067 = "Graphics/ui/gallery/FMG067.webp"
image cg FMG072 = "Graphics/ui/gallery/FMG072.webp"
image cg FMG077 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/FMG077.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg FMG080 = "Graphics/ui/gallery/FMG080.webp"
image cg FMG082 = "Graphics/ui/gallery/FMG082.webp"
image cg FMG087A = "Graphics/ui/gallery/FMG087A.webp"
image cg FMG090 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/FMG090.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg FMG092 = "Graphics/ui/gallery/FMG092.webp"
image cg FMG095 = "Graphics/ui/gallery/FMG095.webp"

image cg GTS000 = "Graphics/ui/gallery/GTS000.webp"
image cg GTS016 = "Graphics/ui/gallery/GTS016.webp"
image cg GTS024 = "Graphics/ui/gallery/GTS024.webp"
image cg GTS025 = "Graphics/ui/gallery/GTS025.webp"
image cg GTS035 = "Graphics/ui/gallery/GTS035.webp"
image cg GTS043_planks1 = "Graphics/ui/gallery/GTS043_planks1.webp"
image cg GTS044_stars1 = "Graphics/ui/gallery/GTS044_stars1.webp"
image cg GTS044_stars2 = "Graphics/ui/gallery/GTS044_stars2.webp"
image cg GTS046_upskirt = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/GTS046_upskirt.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg GTS046_hold1 = "Graphics/ui/gallery/GTS046_hold1.webp"
image cg GTS046_hold2 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/GTS046_hold2.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg GTS046_hold3 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/GTS046_hold3.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg GTS050_nightmare1 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/GTS050_nightmare1.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")

image cg PRG020 = "Graphics/ui/gallery/PRG020.webp"
image cg PRG025 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/PRG025.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg PRG028a = "Graphics/ui/gallery/PRG028a.webp"
image cg PRG028b = "Graphics/ui/gallery/PRG028b.webp"
image cg PRG028c = "Graphics/ui/gallery/PRG028c.webp"
image cg PRG028d = "Graphics/ui/gallery/PRG028d.webp"
image PRG028_scared = "Graphics/ui/gallery/PRG028_scared.webp"
image PRG028_neutral = "Graphics/ui/gallery/PRG028_neutral.webp"
image PRG028_nervous = "Graphics/ui/gallery/PRG028_nervous.webp"
image PRG028_blush = "Graphics/ui/gallery/PRG028_blush.webp"
image cg PRG028_bg = "Graphics/ui/gallery/PRG028_bg.webp"
image PRG028_blur = "Graphics/ui/gallery/PRG028_blur.webp"
image cg PRG038 = "Graphics/ui/gallery/PRG038.webp"
image cg PRG038_poster = "Graphics/ui/gallery/PRG038_poster.webp"
image cg PRG045 = "Graphics/ui/gallery/PRG045.webp"
image cg PRG052 = "Graphics/ui/gallery/PRG052.webp"
image cg PRG054_forest = "Graphics/ui/gallery/PRG054_forest.webp"
image PRG054_forestBlur = "Graphics/ui/gallery/PRG054_forestBlur.webp"
image PRG054_Aida = "Graphics/ui/gallery/PRG054_Aida.webp"
image cg PRG054All = "Graphics/ui/gallery/PRG054All.webp"
image cg PRG061_back = "Graphics/ui/gallery/PRG061_back.webp"
image cg PRG061_front = "Graphics/ui/gallery/PRG061_front.webp"

image cg WG000 = "Graphics/ui/gallery/WG000.webp"
image cg WG009 = "Graphics/ui/gallery/WG009.webp"
image cg WG010_BE = "Graphics/ui/gallery/WG010_BE.webp"
image cg WG010 = "Graphics/ui/gallery/WG010.webp"
image cg WG039 = "Graphics/ui/gallery/WG039.webp"
image cg WG042 = "Graphics/ui/gallery/WG042.webp"
image cg WG046 = "Graphics/ui/gallery/WG046.webp"
image cg WG047 = "Graphics/ui/gallery/WG047.webp"
image cg WG051 = "Graphics/ui/gallery/WG051.webp"
image cg WG055 = "Graphics/ui/gallery/WG055.webp"
image cg WG060S = "Graphics/ui/gallery/WG060S.webp"
image cg WG061 = "Graphics/ui/gallery/WG061.webp"
image cg WG070 = "Graphics/ui/gallery/WG070.webp"
image cg WG071 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/WG071.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg WG072 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/WG072.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg WG076 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/WG076.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg WG079_drawing1 = "Graphics/ui/gallery/WG079_drawing1.webp"
image cg WG079_drawing2 = "Graphics/ui/gallery/WG079_drawing2.webp"
image cg WG085 = "Graphics/ui/gallery/WG085.webp"
image cg WG089 = "Graphics/ui/gallery/WG089.webp"
image cg WG091 = ConditionSwitch(
    "persistent.enable_nsfw == True", "Graphics/ui/gallery/WG091.webp",
    "True", "Graphics/ui/gallery/nsfw-cg.webp")
image cg WG093 = "Graphics/ui/gallery/WG093.webp"
image cg WG097_drawing = "Graphics/ui/gallery/WG097_drawing.webp"
image cg WG101_drawing1 = "Graphics/ui/gallery/WG101_drawing1.webp"
image cg WG101_drawing2 = "Graphics/ui/gallery/WG101_drawing2.webp"

image cg MC000 = "Graphics/ui/gallery/MC000.webp"
image cg MC003 = "Graphics/ui/gallery/MC003.webp"

image cg Global010 = "Graphics/ui/gallery/Global010.webp"

image cg RM000 = "Graphics/ui/gallery/RM000.webp"
image cg RM000_escape1 = "Graphics/ui/gallery/RM000_escape1.webp"
image cg RM000_escape2 = "Graphics/ui/gallery/RM000_escape2.webp"
image cg RM000_escape3 = "Graphics/ui/gallery/RM000_escape3.webp"

#Character sprites
image AE neutral = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral.webp")
image AE neutral-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-2.webp")
image AE neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-annoyed.webp")
image AE neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-eyebrow.webp")
image AE neutral-noglasses = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-noglasses.webp")
image AE neutral-smug = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-smug.webp")
image AE happy = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/happy.webp")
image AE smile = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/happy-2.webp")
image AE pondering = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/pondering.webp")
image AE sad = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/sad.webp")
image AE sad-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/sad-2.webp")
image AE frown = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/sad.webp")
image AE surprised = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/surprised.webp")
image AE surprised-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/surprised-2.webp")
image AE admire = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/admire.webp")
image AE angry = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry.webp")
image AE angry-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry-2.webp")
image AE angry-3 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry-3.webp")
image AE angry-4 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry-4.webp")
image AE aroused = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused.webp")
image AE back = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/behind.webp")
image AE embarrassed = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/embarrassed.webp")
image AE aroused-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused-2.webp")
image AE aroused-3 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused-3.webp")
image AE aroused-4 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused-4.webp")
image AE glasses = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/unique.webp")
image AE glasses-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/unique-2.webp")
image AE glasses-3 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/unique-3.webp")
image AE ass = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/ass.webp")
image AE ass-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/ass.webp")
image AE afraid = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/afraid.webp")
image AE ahegao = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/ahegao.webp")
image AE hatred = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/hatred.webp")
image AE love = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/love.webp")
image AE rage = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/rage.webp")

image BE neutral = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/neutral.webp")
image BE happy = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/happy.webp")
image BE sad = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/sad.webp")
image BE smug = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/smug.webp")
image BE surprised = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/surprised.webp")
image BE surprised-2 = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/surprised-2.webp")
image BE angry = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/angry.webp")
image BE aroused = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/aroused.webp")
image BE unique = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/unique.webp")
image BE confused = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/confused.webp")
image BE crying = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/crying.webp")
image BE disoriented = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/disoriented.webp")
image BE doubt = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/doubt.webp")
image BE embarrassed = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/embarrassed.webp")
image BE embarrassed-2 = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/embarrassed-2.webp")
image BE flustered = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/flustered.webp")
image BE furious = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/furious.webp")
image BE seductive = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/seductive.webp")
image BE shrug = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/shrug.webp")
image BE unamused = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/unamused.webp")
image BE wink = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/wink.webp")
image BE worried = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/worried.webp")

image FMG neutral = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/neutral.webp")
image FMG happy = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/happy.webp")
image FMG sad = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/sad.webp")
image FMG sad-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/sad-2.webp")
image FMG sad-3 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/sad-3.webp")
image FMG surprised = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/surprised.webp")
image FMG surprised-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/surprised-2.webp")
image FMG confused = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/surprised.webp")
image FMG angry = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/angry.webp")
image FMG angry-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/angry-2.webp")
image FMG angry-3 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/angry-3.webp")
image FMG aroused = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/aroused.webp")
image FMG aroused-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/aroused-2.webp")
image FMG disappointed = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/disappointed.webp")
image FMG flex = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/flex.webp")
image FMG upbeat = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/upbeat.webp")

image GTS neutral = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/neutral.webp")
image GTS neutral-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/neutral-2.webp")
image GTS happy = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/happy.webp")
image GTS happy-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/happy-2.webp")
image GTS sad = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/sad.webp")
image GTS sad-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/sad-2.webp")
image GTS surprised = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/surprised.webp")
image GTS angry = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/angry.webp")
image GTS aroused = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/aroused.webp")
image GTS embarrassed = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.webp")
image GTS shy = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.webp")
image GTS blush = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.webp")
image GTS wink = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/wink.webp")
image GTS unique = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/unique.webp")
image GTS unique-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/unique-2.webp")
image GTS despaired-thought = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/despaired-thought.webp")
image GTS pondering = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/pondering.webp")

image GTS_S neutral = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/neutral.webp")
image GTS_S neutral-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/neutral-2.webp")
image GTS_S happy = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/happy.webp")
image GTS_S happy-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/happy-2.webp")
image GTS_S sad = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/sad.webp")
image GTS_S sad-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/sad-2.webp")
image GTS_S surprised = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/surprised.webp")
image GTS_S angry = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/angry.webp")
image GTS_S aroused = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/aroused.webp")
image GTS_S embarrassed = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/embarrassed.webp")
image GTS_S shy = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/embarrassed.webp")
image GTS_S blush = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.webp")
image GTS_S wink = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/wink.webp")
image GTS_S unique = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/unique.webp")
image GTS_S unique-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/unique-2.webp")
image GTS_S despaired-thought = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/despaired-thought.webp")
image GTS_S pondering = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/pondering.webp")

image side GTS_S neutral = DynamicImage("Graphics/GTS/[globalsize]_s/side/neutral.webp")
image side GTS_S neutral-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/neutral.webp") #nyi
image side GTS_S happy = DynamicImage("Graphics/GTS/[globalsize]_s/side/happy.webp")
image side GTS_S happy-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/happy.webp") #nyi
image side GTS_S sad = DynamicImage("Graphics/GTS/[globalsize]_s/side/sad.webp")
image side GTS_S sad-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/sad-2.webp")
image side GTS_S surprised = DynamicImage("Graphics/GTS/[globalsize]_s/side/surprised.webp")
image side GTS_S angry = DynamicImage("Graphics/GTS/[globalsize]_s/side/angry.webp")
image side GTS_S aroused = DynamicImage("Graphics/GTS/[globalsize]_s/side/aroused.webp")
image side GTS_S embarrassed = DynamicImage("Graphics/GTS/[globalsize]_s/side/embarrassed.webp")
image side GTS_S shy = DynamicImage("Graphics/GTS/[globalsize]_s/side/embarrassed.webp")
image side GTS_S blush = DynamicImage("Graphics/GTS/[globalsize]_s/side/embarrassed.webp")
image side GTS_S wink = DynamicImage("Graphics/GTS/[globalsize]_s/side/wink.webp")
image side GTS_S unique = DynamicImage("Graphics/GTS/[globalsize]_s/side/unique.webp")
image side GTS_S unique-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/unique-2.webp")
image side GTS_S despaired-thought = DynamicImage("Graphics/GTS/[globalsize]_s/side/despaired-thought.webp")
image side GTS_S pondering = DynamicImage("Graphics/GTS/[globalsize]_s/side/pondering.webp")

image PRG neutral = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/neutral.webp")
image PRG happy = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/happy.webp")
image PRG excited = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/excited.webp")
image PRG sad = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/sad.webp")
image PRG surprised = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/surprised.webp")
image PRG angry = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/angry.webp")
image PRG aroused = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/aroused.webp")
image PRG blush = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/blush.webp")
image PRG blush-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/blush-2.webp")
image PRG flattered = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/flattered.webp")
image PRG unique = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/unique.webp")
image PRG unique-happy = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/unique-happy.webp")
image PRG unique-blush = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/unique-blush.webp")
image PRG worried = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/worried.webp")
image PRG sad-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/sad-2.webp")
image PRG lactate = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/lactate.webp")
image PRG lactate2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/lactate2.webp")
image PRG admire = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/admire.webp")
image PRG admire-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/admire-2.webp")
image PRG doubt = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/doubt.webp")
image PRG insecure = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/insecure.webp")
image PRG unsure = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/unsure.webp")
image PRG nervous = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/nervous.webp")
image PRG satisfied = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/satisfied.webp")
image PRG angry-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/angry-2.webp")
image PRG scared = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/scared.webp")
image PRG grope = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/grope.webp")
image PRG grope-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/grope-2.webp")
image PRG embarrassed = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/embarrassed.webp")

image WG neutral = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/neutral.webp")
image WG neutral-2 = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/neutral-2.webp")
image WG happy = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/happy.webp")
image WG happy-2 = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/happy-2.webp")
image WG sad = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/sad.webp")
image WG sly = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/sly.webp")
image WG surprised = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/surprised.webp")
image WG surprised-2 = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/surprised-2.webp")
image WG angry = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/angry.webp")
image WG aroused = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/aroused.webp")
image WG haughty = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/unique.webp")
image WG stern = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/stern.webp")
image WG doubt = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/doubt.webp")
image WG bored = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/bored.webp")
image WG coy = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/coy.webp")
image WG back = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/behind.webp")
image WG pondering = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/pondering.webp")
image WG worried = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/worried.webp")

image side MC = DynamicImage("Graphics/MC/[globalsize]/side/[MCOutfit]/side.webp")
image side AECell = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/side.webp") #mainly used only in 098-D
image side BECell = DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/side.webp")
image side WGCell = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/side.webp")
image side FMGCell = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/side.webp")
image side GTSCell = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/side.webp")
image side PRGCell = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/side.webp")
image side TomoCell = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/side.webp")
image side ChibukiCell = DynamicImage("Graphics/minor/chibuki/side.webp")
image side YukoCell = DynamicImage("Graphics/minor/parents/yuko/side.webp")
image side YukiCell = DynamicImage("Graphics/minor/yuki/[globalsize]/side.webp")

#Minor characters
#If you add new sizes here, remember to update "legalsizes" in updateMinorSizes() in script.rpy

image RM neutral = "Graphics/minor/RM/neutral.webp"
image RM neutral-2 = "Graphics/minor/RM/neutral-2.webp"
image RM angry = "Graphics/minor/RM/angry.webp"
image RM angry-2 = "Graphics/minor/RM/angry-2.webp"
image RM concerned = "Graphics/minor/RM/concerned.webp"
image RM concerned-2 = "Graphics/minor/RM/concerned-2.webp"
image RM distrustful = "Graphics/minor/RM/distrustful.webp"
image RM doubt = "Graphics/minor/RM/doubt.webp"
image RM happy = "Graphics/minor/RM/happy.webp"
image RM happy-2 = "Graphics/minor/RM/happy-2.webp"
image RM sad = "Graphics/minor/RM/sad.webp"
image RM smug = "Graphics/minor/RM/smug.webp"

image Yuki neutral = DynamicImage("Graphics/minor/yuki/[globalsize]/neutral.webp")
image Yuki happy = DynamicImage("Graphics/minor/yuki/[globalsize]/happy.webp")
image Yuki sad = DynamicImage("Graphics/minor/yuki/[globalsize]/sad.webp")
image Yuki surprised = DynamicImage("Graphics/minor/yuki/[globalsize]/surprised.webp")
image Yuki gossip = DynamicImage("Graphics/minor/yuki/[globalsize]/gossip.webp")

image HR neutral = "Graphics/minor/faculty/HR/neutral.webp"
image HR neutral-2 = "Graphics/minor/faculty/HR/neutral-2.webp"
image HR angry = "Graphics/minor/faculty/HR/angry.webp"
image HR annoyed = "Graphics/minor/faculty/HR/annoyed.webp"
image HR unique = "Graphics/minor/faculty/HR/unique.webp"
image HR unique-2 = "Graphics/minor/faculty/HR/unique-2.webp"

image Hageshi neutral = "Graphics/minor/faculty/hageshi/neutral.webp"
image Hageshi angry = "Graphics/minor/faculty/hageshi/angry.webp"
image Hageshi satisfied = "Graphics/minor/faculty/hageshi/satisfied.webp"

image Takamura neutral = "Graphics/minor/faculty/takamura/[TakamuraOutfit]/neutral.webp"
image Takamura flattered = "Graphics/minor/faculty/takamura/[TakamuraOutfit]/flattered.webp"
image Takamura happy = "Graphics/minor/faculty/takamura/[TakamuraOutfit]/happy.webp"
image Takamura reassuring = "Graphics/minor/faculty/takamura/[TakamuraOutfit]/reassuring.webp"
image Takamura sad = "Graphics/minor/faculty/takamura/[TakamuraOutfit]/sad.webp"
image Takamura strict = "Graphics/minor/faculty/takamura/[TakamuraOutfit]/strict.webp"

image Tsubasa neutral = "Graphics/minor/faculty/tsubasa/neutral.webp"
image Tsubasa annoyed = "Graphics/minor/faculty/tsubasa/annoyed.webp"
image Tsubasa intrigued = "Graphics/minor/faculty/tsubasa/intrigued.webp"
image Tsubasa satisfied = "Graphics/minor/faculty/tsubasa/satisfied.webp"

image Chiyo neutral = "Graphics/minor/other/chiyo/neutral.webp"

#legalsizes already updated, change images when bigger sprites exist
image Tomoko annoyed = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/annoyed.webp")
image Tomoko defiant = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/defiant.webp")
image Tomoko distracted = Composite(
    (443, 651),
    (0, 0), DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/distracted.webp"),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 5", "Graphics/minor/tomoko/overlays/emoji1.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 10 and getAffection('TM') >= 6", "Graphics/minor/tomoko/overlays/emoji2.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 15 and getAffection('TM') >= 11", "Graphics/minor/tomoko/overlays/emoji3.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 20 and getAffection('TM') >= 16", "Graphics/minor/tomoko/overlays/emoji4.webp",
        None, Null()),
    )
image Tomoko distracted-2 = Composite(
    (443, 651),
    (0, 0), DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/distracted-2.webp"),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 5", "Graphics/minor/tomoko/overlays/emoji1.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 10 and getAffection('TM') >= 6", "Graphics/minor/tomoko/overlays/emoji2.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 15 and getAffection('TM') >= 11", "Graphics/minor/tomoko/overlays/emoji3.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 20 and getAffection('TM') >= 16", "Graphics/minor/tomoko/overlays/emoji4.webp",
        None, Null()),
    )
image Tomoko distracted-3 = Composite(
    (443, 651),
    (0, 0), DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/distracted-3.webp"),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 5", "Graphics/minor/tomoko/overlays/emoji1.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 10 and getAffection('TM') >= 6", "Graphics/minor/tomoko/overlays/emoji2.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 15 and getAffection('TM') >= 11", "Graphics/minor/tomoko/overlays/emoji3.webp",
        None, Null()),
    (0, 0), ConditionSwitch(
        "getAffection('TM') <= 20 and getAffection('TM') >= 16", "Graphics/minor/tomoko/overlays/emoji4.webp",
        None, Null()),
    )
image Tomoko embarrassed = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/embarrassed.webp")
image Tomoko flattered = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/flattered.webp")
image Tomoko neutral = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/neutral.webp")
image Tomoko happy = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/happy.webp")
image Tomoko smile = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/smile.webp")
image Tomoko surprised = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/surprised.webp")
image Tomoko unique = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/unique.webp")
image Tomoko worried = DynamicImage("Graphics/minor/tomoko/[globalsize]/[TomoOutfit]/worried.webp")

image Ryoko neutral = "Graphics/minor/ryoko/[RyokoOutfit]/neutral.webp"
image Ryoko neutral-2 = "Graphics/minor/ryoko/[RyokoOutfit]/neutral-2.webp"
image Ryoko happy = "Graphics/minor/ryoko/[RyokoOutfit]/happy.webp"
image Ryoko annoyed = "Graphics/minor/ryoko/[RyokoOutfit]/annoyed.webp"
image Ryoko camera = "Graphics/minor/ryoko/[RyokoOutfit]/camera.webp"
image Ryoko surprised = "Graphics/minor/ryoko/[RyokoOutfit]/surprised.webp"
image Ryoko tongue = "Graphics/minor/ryoko/[RyokoOutfit]/unique.webp"
image Ryoko confused = "Graphics/minor/ryoko/[RyokoOutfit]/confused.webp"
image Ryoko embarrassed = "Graphics/minor/ryoko/[RyokoOutfit]/embarrassed.webp"

image Chibuki neutral = "Graphics/minor/chibuki/neutral.webp"

image Kanami neutral = "Graphics/minor/kanami/[globalsize]/[KanamiOutfit]/neutral.webp"
image Kanami angry = "Graphics/minor/kanami/[globalsize]/[KanamiOutfit]/angry.webp"
image Kanami embarrassed = "Graphics/minor/kanami/[globalsize]/[KanamiOutfit]/embarrassed.webp"
image Kanami happy = "Graphics/minor/kanami/[globalsize]/[KanamiOutfit]/happy.webp"
image Kanami sad = "Graphics/minor/kanami/[globalsize]/[KanamiOutfit]/sad.webp"
image Kanami surprised = "Graphics/minor/kanami/[globalsize]/[KanamiOutfit]/surprised.webp"

image Kokutan neutral = "Graphics/minor/kokutan/neutral.webp"

image Minori neutral = "Graphics/minor/minori/[MinoriOutfit]/neutral.webp"
image Minori happy = "Graphics/minor/minori/[MinoriOutfit]/happy.webp"
image Minori embarrassed = "Graphics/minor/minori/[MinoriOutfit]/embarrassed.webp"
image Minori sad = "Graphics/minor/minori/[MinoriOutfit]/sad.webp"

image Sakura angry = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/angry.webp")
image Sakura awkward = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/awkward.webp")
image Sakura deadpan = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/deadpan.webp")
image Sakura frustrated = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/frustrated.webp")
image Sakura neutral = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/neutral.webp")
image Sakura neutral-2 = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/neutral-2.webp")
image Sakura happy = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/happy.webp")
image Sakura happy-2 = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/happy-2.webp")
image Sakura nervous = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/nervous.webp")
image Sakura sad = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/sad.webp")
image Sakura sad-2 = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/sad-2.webp")
image Sakura sad-3 = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/sad-3.webp")
image Sakura surprised = DynamicImage("Graphics/minor/sakura/[globalsize]/[SakuraOutfit]/surprised.webp")

image Natsuko neutral = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/neutral.webp")
image Natsuko annoyed = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/annoyed.webp")
image Natsuko disappointed = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/disappointed.webp")
image Natsuko smug = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/smug.webp")
image Natsuko flex = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/flex.webp")
image Natsuko frustrated = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/frustrated.webp")
image Natsuko happy = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/happy.webp")
image Natsuko flirty = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/flirty.webp")
image Natsuko aroused = DynamicImage("Graphics/minor/natsuko/[globalsize]/[NatsOutfit]/aroused.webp")

image Tako neutral = "Graphics/minor/tako/[globalsize]/[TakoOutfit]/neutral.webp"
image Tako angry = "Graphics/minor/tako/[globalsize]/[TakoOutfit]/angry.webp"
image Tako excited = "Graphics/minor/tako/[globalsize]/[TakoOutfit]/excited.webp"
image Tako happy = "Graphics/minor/tako/[globalsize]/[TakoOutfit]/happy.webp"
image Tako unique = "Graphics/minor/tako/[globalsize]/[TakoOutfit]/unique.webp"
image Tako sad = "Graphics/minor/tako/[globalsize]/[TakoOutfit]/sad.webp"
image Tako confused = "Graphics/minor/tako/[globalsize]/[TakoOutfit]/confused.webp"

image Midori neutral = "Graphics/minor/parents/midori/neutral.webp"
image Midori happy = "Graphics/minor/parents/midori/happy.webp"
image Midori nervous = "Graphics/minor/parents/midori/nervous.webp"
image Midori pout = "Graphics/minor/parents/midori/pout.webp"
image Midori sad = "Graphics/minor/parents/midori/sad.webp"
image Midori surprised = "Graphics/minor/parents/midori/surprised.webp"
image Midori unique = "Graphics/minor/parents/midori/unique.webp"

image Okisho neutral = "Graphics/minor/okisho/[globalsize]/[OkishoOutfit]/neutral.webp"
image Okisho neutral-2 = "Graphics/minor/okisho/[globalsize]/[OkishoOutfit]/neutral-2.webp"
image Okisho angry = "Graphics/minor/okisho/[globalsize]/[OkishoOutfit]/angry.webp"
image Okisho happy = "Graphics/minor/okisho/[globalsize]/[OkishoOutfit]/happy.webp"
image Okisho sad = "Graphics/minor/okisho/[globalsize]/[OkishoOutfit]/sad.webp"
image Okisho surprised = "Graphics/minor/okisho/[globalsize]/[OkishoOutfit]/surprised.webp"
image Okisho unique = "Graphics/minor/okisho/[globalsize]/[OkishoOutfit]/unique.webp"

image Yuko neutral = "Graphics/minor/parents/yuko/neutral.webp"
image Yuko angry = "Graphics/minor/parents/yuko/angry.webp"
image Yuko happy = "Graphics/minor/parents/yuko/happy.webp"
image Yuko shrug = "Graphics/minor/parents/yuko/shrug.webp"
image Yuko smug = "Graphics/minor/parents/yuko/smug.webp"
image Yuko surprised = "Graphics/minor/parents/yuko/surprised.webp"
image Yuko unique = "Graphics/minor/parents/yuko/unique.webp"

image Yua neutral = "Graphics/minor/parents/yua/neutral.webp"
image Yua flex = "Graphics/minor/parents/yua/flex.webp"
image Yua happy = "Graphics/minor/parents/yua/happy.webp"
image Yua sad = "Graphics/minor/parents/yua/sad.webp"

image Akihiro neutral = "Graphics/minor/parents/akihiro/neutral.webp"
image Miko neutral = "Graphics/minor/parents/miko/neutral.webp"

image Minami neutral = "Graphics/minor/parents/minami/neutral.webp"
image Minami annoyed = "Graphics/minor/parents/minami/annoyed.webp"
image Minami dark = "Graphics/minor/parents/minami/dark.webp"
image Minami happy = "Graphics/minor/parents/minami/happy.webp"
image Minami unique = "Graphics/minor/parents/minami/unique.webp"

image Jineko neutral = "Graphics/minor/jineko/[globalsize]/[JinekoOutfit]/neutral.webp"
image Jineko angry = "Graphics/minor/jineko/[globalsize]/[JinekoOutfit]/angry.webp"
image Jineko happy = "Graphics/minor/jineko/[globalsize]/[JinekoOutfit]/happy.webp"
image Jineko sad = "Graphics/minor/jineko/[globalsize]/[JinekoOutfit]/sad.webp"
image Jineko surprised = "Graphics/minor/jineko/[globalsize]/[JinekoOutfit]/surprised.webp"
image Jineko unique = "Graphics/minor/jineko/[globalsize]/[JinekoOutfit]/unique.webp"

image Daitaro neutral = "Graphics/minor/parents/daitaro/neutral.webp"
image Vivian neutral = "Graphics/minor/parents/vivian/neutral.webp"
image Vivian happy = "Graphics/minor/parents/vivian/happy.webp"
image Vivian surprised = "Graphics/minor/parents/vivian/surprised.webp"

image dummy = "Graphics/ui/dummy.png"

#Overlays
image FerryTomo1 = "Graphics/minor/tomoko/overlays/table-overlay.webp"
image HairpinGTS1 = "Graphics/GTS/1/overlays/hairpin-overlay.webp"
image FlowerPRG2 = "Graphics/PRG/2/overlays/flower-overlay.webp"
image GumAE6EP = "Graphics/AE/6/overlays/gum-overlay.webp"
image WmHairpinBE2 = "Graphics/BE/2/overlays/hairpin-overlay.webp"
image NoHairpinBE = "Graphics/BE/[globalsize]/overlays/nohairpin-overlay.webp"
image AthleticSoccerBE1 = "Graphics/BE/1/overlays/soccer-overlay.webp"
image AlternateOutfitBE = "Graphics/BE/[globalsize]/overlays/alternate-overlay.webp"
image Table = "Graphics/BE/4/overlays/table-overlay.webp"
image TableBE = "Graphics/BE/4/overlays/table-boobs-overlay.webp"
image TableBEWorried = "Graphics/BE/4/overlays/table-boobs-worried-overlay.webp"

#Audio
define audio.AE = "Audio/BGM/scene_AE.ogg"
define audio.AEAlt = "Audio/BGM/scene_AEalt.ogg"
define audio.BE = "Audio/BGM/scene_BE.ogg"
define audio.FMG = "Audio/BGM/scene_FMG.ogg" #Pump It
define audio.GTS = "Audio/BGM/scene_GTS.ogg" #Hidden Meadow
define audio.GTSAlt = "Audio/BGM/scene_GTS2.ogg" #Hidden Meadow (Taishogoto Ver.)
define audio.RM = "Audio/BGM/scene_RM.ogg" #K. Tera
define audio.RMInvestigate = "Audio/BGM/TheInvestigator.ogg" #Alt Daichi Theme
define audio.MC = "Audio/BGM/scene_MC.ogg" #Our Protagonist
define audio.MCGuitar = "Audio/BGM/scene_MCguitar.ogg"
define audio.PRG = "Audio/BGM/scene_PRG.ogg" #Quiet Wandering
define audio.PRGMusicBox = "Audio/BGM/scene_PRGMusicBox.ogg" #Quiet Wandering (Music Box)
define audio.PRGDramatic = "Audio/BGM/scene_PRGdrama.ogg" #Small Moments
define audio.PRGChallenge = "Audio/BGM/scene_PRGchallenge.ogg" #The Challenge
define audio.PRGOverflow = "Audio/BGM/scene_PRGOverflow.ogg" #Overflow
define audio.PRGAlt = "Audio/BGM/scene_PRG2.ogg" #Press On
define audio.WG = "Audio/BGM/scene_WG.ogg" #Aristocratic Opulence
define audio.WGAlt = "Audio/BGM/scene_WG2.ogg" #Elegant Antics
define audio.Argue = "Audio/BGM/tension.ogg" #Argument
define audio.Beach = "Audio/BGM/scene_beach.ogg" #Sea Breeze
define audio.Bittersweet = "Audio/BGM/scene_bittersweet.mp3" #PH - Hobby Atelier Carrot Wine
define audio.BigChanges = "Audio/BGM/scene_uncategorized2.mp3"
define audio.BrightLights = "Audio/BGM/BrightLights.ogg" #Town Theme
define audio.Busy = "Audio/BGM/scene_busy.mp3" #PH - Pierrot Lunaire
define audio.ChangingSeasons = "Audio/BGM/ChangingSeasons.ogg" #Contemplation Theme
define audio.Chase = "Audio/BGM/Chase.ogg"
define audio.ClearSkies = "Audio/BGM/theme_clearskies.ogg"
define audio.Country = "Audio/BGM/scene_country.ogg" #Country Theme
define audio.CreepingPresence = "Audio/BGM/CreepingPresence.ogg"
define audio.DayByDay = "Audio/BGM/scene_daybyday.ogg" #General Music 3
define audio.Daymenu = "Audio/BGM/menu_daymenu.ogg" #PH - Yoshiki Ara
define audio.DifferentPaths = "Audio/BGM/differentpaths.ogg"
define audio.DormLife = "Audio/BGM/scene_dorm.ogg"
define audio.Festival = "Audio/BGM/scene_festival.ogg" #Dokkoi!
define audio.HallowedHalls = "Audio/BGM/hallowedhalls.ogg" #Hallowed Halls
define audio.HigherEdu = "Audio/BGM/scene_higheredu.ogg" #Higher Education (This is what Hallway is, in any scripts)
define audio.HigherEduC = "Audio/BGM/scene_highereduC.ogg" #Higher Education Claviola Variant
define audio.Holiday = "Audio/BGM/scene_holiday.ogg" #Winter Wonderland
define audio.KnowMyself = "Audio/BGM/knowmyself.mp3" #Know Myself (short loop) by Patrick Patrikios
define audio.FullKnowMyself = "Audio/BGM/knowmyself_full.mp3" #Know Myself (full song) by Patrick Patrikios
define audio.LastBell = "Audio/BGM/general4.ogg" #Last Bell
define audio.Love = "Audio/BGM/love.ogg"
define audio.LoveA = "Audio/BGM/love_A.ogg"
define audio.LoveB = "Audio/BGM/love_B.ogg"
define audio.LoveC = "Audio/BGM/love_C.ogg"
define audio.LoveMB = "Audio/BGM/love_mb.ogg" #Music Box variant of Love
define audio.Memories = "Audio/BGM/memories.mp3"
define audio.Misfit = "Audio/BGM/scene_themisfit.ogg" #Okisho's Theme
define audio.MomentTime = "Audio/BGM/MomentTime.ogg" #A Moment in Time
define audio.Motivation = "Audio/BGM/motivation.ogg"
define audio.Natsuko = "Audio/BGM/theme_natsuko.ogg" #Hatred
define audio.Nembutsu = "Audio/BGM/scene_nembutsu.ogg" #Morning Mist - altTitle
define audio.Nostalgia = "Audio/BGM/nostalgia.ogg"
define audio.NostalgiaSax = "Audio/BGM/nostalgia_sax.ogg"
define audio.OuttaMyFace = "Audio/BGM/OuttaMyFace.ogg"
define audio.Peaceful = "Audio/BGM/scene_peaceful.mp3" #PH
define audio.Rain = "Audio/BGM/scene_rain.mp3" #PH - Hobby Atelier Carrot Wine
define audio.Reality = "Audio/BGM/reality.ogg"
define audio.RevvinUp = "Audio/BGM/RevvinUp.ogg"
define audio.Rivalry = "Audio/BGM/rivalry.ogg"
define audio.Requiem = "Audio/BGM/requiem.mp3" #Distant Questioning
define audio.Romance = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Schoolday = "Audio/BGM/scene_schoolday.mp3" #PH - Yoshiki Ara
define audio.Secret = "Audio/BGM/scene_secret.ogg" #A Secret Place
define audio.Stardust = "Audio/BGM/stardust.ogg"
define audio.Steamy = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Sunset = "Audio/BGM/scene_sunset.mp3"
define audio.Tension = "Audio/BGM/tensemoment.ogg" #A Tense Moment
define audio.TheAnswer = "Audio/BGM/the_answer.ogg"
define audio.Tomoko = "Audio/BGM/scene_tomoko.ogg" #Finding Purpose
define audio.TremblingWhispers = "Audio/BGM/tremblingWhispers.ogg"
define audio.TwilightBright = "Audio/BGM/twilightBright.ogg"
define audio.TwilightAmbient = "Audio/BGM/twilightAmbient.ogg"
define audio.TwilightDusk = "Audio/BGM/twilightDusk.ogg"
define audio.WildBlur = "Audio/BGM/scene_uncategorized1.mp3" #Wild Blur
define audio.Winter = "Audio/BGM/scene_winter.ogg" #Solstice Night
define audio.WinterVocal = "Audio/BGM/scene_wintervocal.ogg"

define audio.BrandenburgNo4 = "Audio/BGM/brandenburgno4.mp3" #Kevin MacLeod
define audio.Gymnopedie = "Audio/BGM/gymnopedie.mp3" #Erik Satie
define audio.Pastorale = "Audio/BGM/Pastorale.ogg" #Joel Cummins
define audio.SimpleSonata = "Audio/BGM/SimpleSonata.ogg" #Sir Cubworth
define audio.MinuetG = "Audio/BGM/MinuetG.ogg" #Tullio Forlenza
define audio.MoonlightSonata = "Audio/BGM/moonlightsonata.mp3" #Beethoven
define audio.AgnusDeiX = "Audio/BGM/agnusdeix.mp3" #Kevin MacLeod
define audio.AngelsWeep = "Audio/BGM/angelsweep.mp3" #Audionautix
define audio.BachGavottes = "Audio/BGM/Bach_Gavottes.mp3" #Johann Sebastian Bach
define audio.ConcertinoTeleman = "Audio/BGM/Concertino_Teleman.mp3" #Georg Philipp Telemann
define audio.InvitationCastleBall = "Audio/BGM/InvitationCastle_Doug.mp3" #Doug Maxwell
define audio.BaroqueCoffeeHouse = "Audio/BGM/BaroqueCoffee_Doug.mp3" #Doug Maxwell
define audio.SonataFMajor = "Audio/BGM/Sonata_AllegroF.mp3"
define audio.SummerSymphonyBall = "Audio/BGM/SummerSymphonyBall_Cubworth.mp3" #Sir Cubworth
define audio.HarpsichordFugue = "Audio/BGM/HarpsichordFugue.ogg" #Sir Cubworth
define audio.BaroqueLetter = "Audio/BGM/BaroqueLetter.ogg" #Aaron Kenny
define audio.BaroqueLetter2 = "Audio/BGM/BaroqueLetter2.ogg" #Aaron Kenny
define audio.Bourree = "Audio/BGM/Bourree.ogg" #Joel Cummins
define audio.SoloCelloPassion = "Audio/BGM/SoloCelloPassion.ogg" #Doug Maxwell
define audio.Zephyrs = "Audio/BGM/Zephyrs.ogg" #To the Zephyrs, by Philipp Gottlieb Anton Sr.
define audio.Fiddles = "Audio/BGM/Fiddles.ogg" #Fiddles McGinty by Kevin MacLeod
define audio.SlowDance = "Audio/BGM/1940SlowDance.ogg" #Doug Maxwell
define audio.SwingBadaBing = "Audio/BGM/SingSwing.ogg" #Doug Maxwell

define audio.EventStart = "Audio/SFX/sfx_eventstart.ogg"
define audio.AidaCowWalk = "Audio/SFX/Diant/sfx_aida_cowbellwalk.ogg"
define audio.AidaCowSex = "Audio/SFX/Diant/sfx_aida_cowbellsex.ogg"
define audio.AlarmClock = "Audio/SFX/sfx_alarmclock.ogg"
define audio.Bird = "Audio/SFX/sfx_tbi.ogg" #NEED (current one too long)
define audio.Cheer = "Audio/SFX/sfx_cheer.mp3"
define audio.ClockTower = "Audio/SFX/sfx_clocktower.mp3"
define audio.ClothingTearShort = "Audio/SFX/Clothing/sfx_clothingtear_short.ogg"
define audio.Crash = "Audio/SFX/sfx_thud.wav" #NEED UPDATE
define audio.CricketAmbience = "Audio/SFX/sfx_cricketambience.ogg" #Use "play music" to loop as a track
define audio.DoorOpen = "Audio/SFX/Door/sfx_door_open.ogg"
define audio.DoorShut = "Audio/SFX/Door/sfx_door_shut.ogg"
define audio.Boing = "Audio/SFX/sfx_boing.ogg"
define audio.Knock = "Audio/SFX/sfx_knock.mp3"
define audio.KnockEcho = "Audio/SFX/Door/sfx_door_knockecho.ogg"
define audio.Stomach = "Audio/SFX/sfx_tbi.ogg"
define audio.MaleStepAway = "Audio/SFX/Misc/sfx_footsteps_maleaway.ogg"
define audio.LightRainAmbience = "Audio/SFX/Ambience/sfx_rainambience_light.ogg"
define audio.MidRainAmbience = "Audio/SFX/Ambience/sfx_rainambience_mid.ogg"
define audio.Thud = "Audio/SFX/sfx_thud.wav"
define audio.Thunder = "Audio/SFX/sfx_thunder.wav"
define audio.Victory = "Audio/SFX/sfx_victory.ogg"
define audio.Whistle = "Audio/SFX/sfx_whistle.mp3"
define audio.Bell = "Audio/SFX/sfx_bell.mp3"
define audio.ReleaseArrow = "Audio/SFX/sfw_releasearrow.wav"
define audio.PhoneVibrate = "Audio/SFX/Phone/sfx_phonevibrate_3x.ogg"
define audio.Vibrate = "Audio/SFX/sfx_vibrate.ogg"

init 1 python:
    eventlibrary['MC001'] = {"name": "Sharpening the Senses", "girls": ["MC", "RM"], "type": EventTypeEnum.OPTIONAL,                      "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": []}
    eventlibrary['MC002'] = {"name": "Warmth of a Heart", "girls": ["faculty"], "type": EventTypeEnum.OPTIONAL,                      "location": "facultyroom",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size2"],                  "conditions": [[ConditionEnum.EVENT, "MC001"]]}
    eventlibrary['MC003'] = {"name": "Will She Ever Grow up?", "girls": ["TM", "RM"], "type": EventTypeEnum.OPTIONAL,                      "location": "dormexterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size2"],          "conditions": [[ConditionEnum.EVENT, "global005"]]}
    eventlibrary['MC004'] = {"name": "Summary", "girls": ["MC"], "type": EventTypeEnum.OPTIONAL,                      "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size2"],          "conditions": [[ConditionEnum.EVENT, "MC003"]]}
    eventlibrary['MC005'] = {"name": "Golden Week", "girls": ["MC"], "type": EventTypeEnum.OPTIONAL,                      "location": "park",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["XX20"],          "conditions": [[ConditionEnum.TIMEFLAG, "aftersize2"]]}
    eventlibrary['MC006'] = {"name": "A Bad Handoff", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                               "location": "auditorium",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["XX20"],      "conditions": [[ConditionEnum.OR, [ConditionEnum.EVENT, "MC005"], [ConditionEnum.FLAG, "XX12"]]]}
    eventlibrary['MC007'] = {"name": "Stakeout at the Bakeout", "girls": ["RM"], "type": EventTypeEnum.OPTIONAL,             "location": "bakery",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size3", "noMC007"],                "conditions": [[ConditionEnum.AND, [ConditionEnum.NOEVENT, "FMG010"], [ConditionEnum.FLAG, "XX15"]]]}
    eventlibrary['MC008'] = {"name": "edoc ruo", "girls": ["MC", "BE"], "type": EventTypeEnum.OPTIONAL,                           "location": "classroom",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],                "conditions": [[ConditionEnum.TIMEFLAG, "XX20"]]}
    eventlibrary['MC009'] = {"name": "La Femme de France", "girls": ["faculty"], "type": EventTypeEnum.OPTIONAL,             "location": "cookingclassroom",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size4"],                "conditions": [[ConditionEnum.FLAG, "XX22"]]}
    eventlibrary['MC011'] = {"name": "Put Up a Fight", "girls": ["faculty"], "type": EventTypeEnum.OPTIONAL,                           "location": "cafeteria",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size4"],     "conditions": [[ConditionEnum.TIMEFLAG, "size3"]]}
    eventlibrary['MC012'] = {"name": "GnG", "girls": ["MC"], "type": EventTypeEnum.OPTIONAL,                           "location": "hallway",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size4"],     "conditions": [[ConditionEnum.OR, [ConditionEnum.EVENT, "global032"], [ConditionEnum.EVENT, "GTS032"]]]}
    eventlibrary['MC013'] = {"name": "Finals", "girls": ["MC"], "type": EventTypeEnum.OPTIONAL,                           "location": "classroom",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size4"],     "conditions": [[ConditionEnum.FLAG, "XX35"]]}
    eventlibrary['MC014'] = {"name": "The Line", "girls": ["TM"], "type": EventTypeEnum.OPTIONAL,                           "location": "gamestore",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size4"],     "conditions": [[ConditionEnum.FLAG, "XX37"]]}
    eventlibrary['MC023'] = {"name": "Stranger Than Fiction", "girls": ["MC"], "type": EventTypeEnum.OPTIONAL,               "location": "hallwaystairs",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size5"],     "conditions": [[ConditionEnum.FLAG, "XX54"]]}
    eventlibrary['MC024'] = {"name": "The Scholarship", "girls": ["MC"], "type": EventTypeEnum.OPTIONAL,                           "location": "infodesk",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size5"],     "conditions": [[ConditionEnum.FLAG, "XX56"]]}
    eventlibrary['MC033'] = {"name": "The Sentinel of Seichou", "girls": ["faculty"], "type": EventTypeEnum.OPTIONAL,                   "location": "facultyroom",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["XX80"],     "conditions": [[ConditionEnum.FLAG, "XX73"]]}
    eventlibrary['MC041'] = {"name": "Not So Big Afterall", "girls": ["faculty"], "type": EventTypeEnum.OPTIONAL,             "location": "cafeteria",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.TIMEFLAG, "size6"]]}
    eventlibrary['MC042'] = {"name": "Keisuke End", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                                "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.EVENT, "MC033"]]}

    eventlibrary['global005'] = {"name": "And the Results Are In", "girls": ["MC"], "type": EventTypeEnum.OPTIONALCORE,        "location": "auditorium",    "priority": PrioEnum.ALL, "next": "", "obsflags": [],           "conditions": [[ConditionEnum.TIMEFLAG, "testday"]]}
    eventlibrary['global010'] = {"name": "A Start of Something Big", "girls": ["MC"], "type": EventTypeEnum.OPTIONALCORE,        "location": "campuscenter",    "priority": PrioEnum.ALL, "next": "", "obsflags": [],           "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['global026'] = {"name": "Talk of the Town", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,             "location": "classroom",        "priority": PrioEnum.ALL,  "next": "", "obsflags": [],          "conditions": [[ConditionEnum.AND, [ConditionEnum.TIMEFLAG, "XX25"], [ConditionEnum.NOROUTELOCK, "PRG"]]]}
    eventlibrary['global032'] = {"name": "The Departure", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,             "location": "classroom",        "priority": PrioEnum.ALL,   "next": "",  "obsflags": ["noGTS030"],          "conditions": [[ConditionEnum.AND, [ConditionEnum.TIMEFLAG, "size3"], [ConditionEnum.FLAG, "XX32"]]]}
    eventlibrary['RM001'] = {"name": "Getting to Know Your Roommate", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,  "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.FLAG, "RMRoute_Unlocked"]]}
    eventlibrary['RM002'] = {"name": "Ties that Bind", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                   "location": "gatefront",       "priority": PrioEnum.NONE, "next": "", "obsflags": ["size5"],          "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "RM001"], [ConditionEnum.EVENT, "global005"]]]}
    eventlibrary['RM003'] = {"name": "Mystery of the Seichou Dock", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,     "location": "dock",       "priority": PrioEnum.NONE, "next": "", "obsflags": ["size5"],          "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "RM002"], [ConditionEnum.FLAG, "XX12"]]]}
    eventlibrary['RM004'] = {"name": "Voices of the Past", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,     "location": "classroom_3",       "priority": PrioEnum.NONE, "next": "", "obsflags": ["size3"],          "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "RM003"], [ConditionEnum.FLAG, "XX15"]]]}
    eventlibrary['RM005'] = {"name": "Milestone", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,     "location": "dorminterior",       "priority": PrioEnum.NONE, "next": "", "obsflags": ["size3"],          "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "RM004"], [ConditionEnum.TIMEFLAG, "XX20"]]]}
    eventlibrary['RM006'] = {"name": "The Gate", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,     "location": "dorminterior",       "priority": PrioEnum.NONE, "next": "", "obsflags": ["size4"],          "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "RM005"], [ConditionEnum.FLAG, "XX22"]]]}

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
    #AE size2
    eventlibrary['AE011'] = {"name": "Raising the Question", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE012",    "obsflags": [],                "conditions": []}
    eventlibrary['AE012'] = {"name": "Inquiry and Response", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE013", "obsflags": [],                "conditions": []}
    eventlibrary['AE013'] = {"name": "Stickers on Caskets", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE014", "obsflags": [],                "conditions": []}
    eventlibrary['AE014'] = {"name": "The Daily Grind", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE015", "obsflags": [],                "conditions": []}
    eventlibrary['AE015'] = {"name": "Hostage Situation", "girls": ["AE"], "type": EventTypeEnum.CORE,                          "location": "office",           "priority": PrioEnum.NONE, "sp": 3,     "next": "AE016", "obsflags": [],                "conditions": []}
    eventlibrary['AE016'] = {"name": "A Little List", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "library",          "priority": PrioEnum.NONE, "sp": 3,     "next": "AE017", "obsflags": [],                "conditions": []}
    eventlibrary['AE017'] = {"name": "Chopsticks", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "AE018", "obsflags": [],                "conditions": []}
    eventlibrary['AE018'] = {"name": "Miseri Mei", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "AE019", "obsflags": [],                "conditions": []}
    eventlibrary['AE019'] = {"name": "Rondo Alla Turca", "girls": ["AE"], "type": EventTypeEnum.CORE,                           "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 4,     "next": "AE020", "obsflags": [],                "conditions": []}
    eventlibrary['AE020'] = {"name": "Pascha Nostrum", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "AE021", "obsflags": [],                "conditions": []}
    eventlibrary['AE021'] = {"name": "Prelude for Choir", "girls": ["AE", "WG", "PRG"], "type": EventTypeEnum.CORE,            "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "AE022", "obsflags": [],                "conditions": []}
    eventlibrary['AE022'] = {"name": "Casta Diva", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hallway",          "priority": PrioEnum.NONE, "sp": 5,     "next": "AE023", "obsflags": [],                "conditions": []}
    eventlibrary['AE023'] = {"name": "Sarabande", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "hallway",          "priority": PrioEnum.NONE, "sp": 5,     "next": "AE024", "obsflags": [],                "conditions": []}
    eventlibrary['AE024'] = {"name": "Carmen", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "roof",             "priority": PrioEnum.NONE, "sp": 5,     "next": "AE025", "obsflags": [],                "conditions": []}
    eventlibrary['AE025'] = {"name": "Seasons", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 5,     "next": "AE026", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE026'] = {"name": "The Most Wondrous Dream", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 6,     "next": "AE027", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE027'] = {"name": "Through Thicc or Thin", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "classroom",        "priority": PrioEnum.NONE, "sp": 6,     "next": "AE028", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE028'] = {"name": "Bolero", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "roof",             "priority": PrioEnum.NONE, "sp": 6,     "next": "AE029", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE029'] = {"name": "Moon in June", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 6,     "next": "AE030", "obsflags": [],                "conditions": []}
    #AE size3
    eventlibrary['AE030'] = {"name": "Exposure", "girls": ["AE", "BE"], "type": EventTypeEnum.CORE,                             "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "AE031", "obsflags": [],                "conditions": []}
    eventlibrary['AE031'] = {"name": "The Keys to her Heart", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 7,     "next": "AE032", "obsflags": [],                "conditions": []}
    eventlibrary['AE032'] = {"name": "Standardized High Standards", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,     "next": "AE033", "obsflags": [],                "conditions": []}
    eventlibrary['AE033'] = {"name": "Your Secret Told on You", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "hallway",          "priority": PrioEnum.NONE, "sp": 7,     "next": "AE034", "obsflags": [],                "conditions": []}
    eventlibrary['AE034'] = {"name": "O Mio Babbino Caro", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 8,     "next": "AE035", "obsflags": [],                "conditions": []}
    eventlibrary['AE035'] = {"name": "The Black Box", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 8,     "next": "AE036", "obsflags": [],                "conditions": []}
    eventlibrary['AE036'] = {"name": "Out There", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 8,     "next": "AE037", "obsflags": [],                "conditions": []}
    eventlibrary['AE037'] = {"name": "A Walk Through Town", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE038", "obsflags": [],                "conditions": []}
    eventlibrary['AE038'] = {"name": "A Simple Meal", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "town",             "priority": PrioEnum.NONE, "sp": 9,     "next": "AE039", "obsflags": [],                "conditions": []}
    eventlibrary['AE039'] = {"name": "Dawn of Warblade", "girls": ["AE"], "type": EventTypeEnum.CORE,                           "location": "town",             "priority": PrioEnum.NONE, "sp": 9,     "next": "AE040", "obsflags": [],                "conditions": []}
    eventlibrary['AE040'] = {"name": "A Game of Oversized Thrones", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "town",             "priority": PrioEnum.NONE, "sp": 9,     "next": "AE041", "obsflags": [],                "conditions": []}
    eventlibrary['AE041'] = {"name": "Ambush", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "town",             "priority": PrioEnum.NONE, "sp": 9,     "next": "AE042", "obsflags": [],                "conditions": []}
    eventlibrary['AE042'] = {"name": "Chaos Reigns", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "town",             "priority": PrioEnum.NONE, "sp": 10,     "next": "AE043", "obsflags": [],                "conditions": []}
    eventlibrary['AE043'] = {"name": "Rainy Skies, Hot Coffee", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "town",             "priority": PrioEnum.NONE, "sp": 10,     "next": "AE044", "obsflags": [],                "conditions": []}
    eventlibrary['AE044'] = {"name": "From Which The Angel Falls", "girls": ["AE"], "type": EventTypeEnum.CORE,                 "location": "town",             "priority": PrioEnum.NONE, "sp": 10,     "next": "AE045", "obsflags": [],                "conditions": []}
    eventlibrary['AE045'] = {"name": "Let My Prayers Arise", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "clocktower",       "priority": PrioEnum.GIRL, "sp": 10,     "next": "AE046", "obsflags": [],                "conditions": []}
    eventlibrary['AE046'] = {"name": "Perfection in Normality", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "dormAE",           "priority": PrioEnum.NONE, "sp": 11,     "next": "AE047", "obsflags": [],                "conditions": []}
    eventlibrary['AE047'] = {"name": "So Many", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "dormAE",           "priority": PrioEnum.NONE, "sp": 11,     "next": "AE048", "obsflags": [],                "conditions": []}
    eventlibrary['AE048'] = {"name": "Taking it Seriously", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 11,     "next": "AE049", "obsflags": [],                "conditions": []}
    eventlibrary['AE049'] = {"name": "The Wise Thief", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 11,     "next": "AE050", "obsflags": [],                "conditions": []}
    #AE size4
    eventlibrary['AE050'] = {"name": "Nights in White Satin", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",     "priority": PrioEnum.ALL, "sp": 12,     "next": "AE051", "obsflags": [],                "conditions": []}
    eventlibrary['AE051'] = {"name": "Never Reaching the End", "girls": ["AE"], "type": EventTypeEnum.CORE,                     "location": "dormexterior",     "priority": PrioEnum.ALL, "sp": 12,     "next": "AE052", "obsflags": [],                "conditions": []}
    eventlibrary['AE052'] = {"name": "Tristesse", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "library",          "priority": PrioEnum.NONE, "sp": 12,    "next": "AE053", "obsflags": [],                "conditions": []}
    eventlibrary['AE053'] = {"name": "Dressed to Impress", "girls": ["AE", "WG"], "type": EventTypeEnum.CORE,                  "location": "town",             "priority": PrioEnum.NONE, "sp": 12,    "next": "AE054", "obsflags": [],                "conditions": []}
    eventlibrary['AE054'] = {"name": "Molto Allegro", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 13,    "next": "AE055", "obsflags": [],                "conditions": []}
    eventlibrary['AE055'] = {"name": "Ruhe Sanft", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hillroad",         "priority": PrioEnum.NONE, "sp": 13,    "next": "AE056", "obsflags": [],                "conditions": []}
    eventlibrary['AE056'] = {"name": "Hymn of the Cherubim", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "classroom",        "priority": PrioEnum.NONE, "sp": 13,    "next": "AE057", "obsflags": [],                "conditions": []}
    eventlibrary['AE057'] = {"name": "Norwegian Dance", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 13,    "next": "AE058", "obsflags": [],                "conditions": []}
    eventlibrary['AE058'] = {"name": "Waltz of the Flowers", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "library",          "priority": PrioEnum.NONE, "sp": 14,    "next": "AE059", "obsflags": [],                "conditions": []}
    eventlibrary['AE059'] = {"name": "Eye to Eye, Face to Face, Heart to Heart", "girls": ["AE"], "type": EventTypeEnum.CORE,   "location": "hallway",          "priority": PrioEnum.NONE, "sp": 14,    "next": "AE060", "obsflags": [],                "conditions": []}
    eventlibrary['AE060'] = {"name": "Csárdás", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "library",          "priority": PrioEnum.NONE, "sp": 14,    "next": "AE061", "obsflags": [],                "conditions": []}
    eventlibrary['AE061'] = {"name": "Starless", "girls": ["AE"], "type": EventTypeEnum.CORE,                                   "location": "library",          "priority": PrioEnum.NONE, "sp": 14,    "next": "AE062", "obsflags": [],                "conditions": []}
    eventlibrary['AE062'] = {"name": "Gymnopedies", "girls": ["AE", "BE"], "type": EventTypeEnum.CORE,                          "location": "town",             "priority": PrioEnum.NONE, "sp": 15,    "next": "AE063", "obsflags": [],                "conditions": []}
    eventlibrary['AE063'] = {"name": "Ballade No. 1 in G Minor", "girls": ["AE"], "type": EventTypeEnum.CORE,                   "location": "classroom",        "priority": PrioEnum.NONE, "sp": 15,    "next": "AE064", "obsflags": [],                "conditions": []}
    eventlibrary['AE064'] = {"name": "Nocturne no. 2", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "hallway",          "priority": PrioEnum.NONE, "sp": 15,    "next": "AE065", "obsflags": [],                "conditions": []}
    eventlibrary['AE065'] = {"name": "Prelude in C Minor", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 15,    "next": "AE066", "obsflags": [],                "conditions": []}
    eventlibrary['AE066'] = {"name": "Dies Irae", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "hallway",          "priority": PrioEnum.NONE, "sp": 16,    "next": "AE067", "obsflags": [],                "conditions": []}
    eventlibrary['AE067'] = {"name": "Troparion", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "roof",             "priority": PrioEnum.NONE, "sp": 16,    "next": "AE068", "obsflags": [],                "conditions": []}
    eventlibrary['AE068'] = {"name": "Sonata", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 16,    "next": "AE069", "obsflags": [],                "conditions": []}
    eventlibrary['AE069'] = {"name": "The Creed", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "classroom",        "priority": PrioEnum.NONE, "sp": 16,    "next": "AE070", "obsflags": [],                "conditions": []}
    #AE size5
    eventlibrary['AE070'] = {"name": "Lento Placido", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 17,    "next": "AE071", "obsflags": [],                "conditions": []}
    eventlibrary['AE071'] = {"name": "Poco Adagio", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.NONE, "sp": 17,    "next": "AE072", "obsflags": [],                "conditions": []}
    eventlibrary['AE072'] = {"name": "Waltz of the Snowflakes", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "frozenbeach",      "priority": PrioEnum.NONE, "sp": 17,    "next": "AE073", "obsflags": [],                "conditions": []}
    eventlibrary['AE073'] = {"name": "Stichera No. 1", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "hallway",          "priority": PrioEnum.NONE, "sp": 17,    "next": "AE074", "obsflags": [],                "conditions": []}
    eventlibrary['AE074'] = {"name": "The Snow is Dancing", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "field",            "priority": PrioEnum.NONE, "sp": 18,    "next": "AE075", "obsflags": [],                "conditions": []}
    eventlibrary['AE075'] = {"name": "Des Pas Sur la Neige", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 18,    "next": "AE076", "obsflags": [],                "conditions": []}
    eventlibrary['AE076'] = {"name": "Stand by Me", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.NONE, "sp": 18,    "next": "AE077", "obsflags": [],                "conditions": []}
    eventlibrary['AE077'] = {"name": "Pas de Deux", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.NONE, "sp": 18,    "next": "AE078", "obsflags": [],                "conditions": []}
    eventlibrary['AE078'] = {"name": "Méditation", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.ALL, "sp": 19,       "next": "AE079", "obsflags": [],                "conditions": []}
    eventlibrary['AE079'] = {"name": "Metamorphosis", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 19,       "next": "AE080", "obsflags": [],                "conditions": []}
    eventlibrary['AE080'] = {"name": "Pavane for Dead Princess", "girls": ["AE"], "type": EventTypeEnum.CORE,                  "location": "dormtomoko",      "priority": PrioEnum.ALL, "sp": 19,       "next": "AE081", "obsflags": [],                "conditions": []}
    eventlibrary['AE081'] = {"name": "Arabesque No. 1", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "classroom",      "priority": PrioEnum.ALL, "sp": 19,       "next": "AE082", "obsflags": [],                "conditions": []}
    eventlibrary['AE082'] = {"name": "Emperor", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "hallway",      "priority": PrioEnum.NONE, "sp": 20,       "next": "AE083", "obsflags": [],                "conditions": []}
    eventlibrary['AE083'] = {"name": "Gnossienne No.1", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "hallway",      "priority": PrioEnum.NONE, "sp": 20,       "next": "AE084", "obsflags": [],                "conditions": []}
    eventlibrary['AE084'] = {"name": "Ave Verum Corpus", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "classroom",      "priority": PrioEnum.NONE, "sp": 20,       "next": "AE085", "obsflags": [],                "conditions": []}
    eventlibrary['AE085'] = {"name": "Verklärte Nacht", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "clocktower",      "priority": PrioEnum.NONE, "sp": 20,       "next": "AE086", "obsflags": [],                "conditions": []}
    eventlibrary['AE086'] = {"name": "Washington Post March", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 21,       "next": "AE087", "obsflags": [],                "conditions": []}
    eventlibrary['AE087'] = {"name": "Romantic Pieces", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 21,       "next": "AE088", "obsflags": [],                "conditions": []}
    eventlibrary['AE088'] = {"name": "Raymonda", "girls": ["AE"], "type": EventTypeEnum.CORE,                                   "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 21,       "next": "AE089", "obsflags": [],                "conditions": []}
    eventlibrary['AE089'] = {"name": "Corilan Overture", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "dormAE",          "priority": PrioEnum.NONE, "sp": 21,       "next": "AE090", "obsflags": [],                "conditions": []}
    #AE size6
    eventlibrary['AE090'] = {"name": "Adagio for Strings", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "classroom",      "priority": PrioEnum.NONE, "sp": 22,       "next": "AE091", "obsflags": [],                "conditions": []}
    eventlibrary['AE091'] = {"name": "4'33\"", "girls": ["AE"], "type": EventTypeEnum.CORE,                                   "location": "classroom",      "priority": PrioEnum.NONE, "sp": 22,       "next": "AE092", "obsflags": [],                "conditions": []}
    eventlibrary['AE092'] = {"name": "Det er det skønneste jeg ved", "girls": ["AE"], "type": EventTypeEnum.CORE,             "location": "dormhallway",      "priority": PrioEnum.NONE, "sp": 22,       "next": "AE093", "obsflags": [],                "conditions": []}
    eventlibrary['AE093'] = {"name": "Symphony No. 9", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "hallway",      "priority": PrioEnum.NONE, "sp": 22,       "next": "AE094", "obsflags": [],                "conditions": []}
    eventlibrary['AE094'] = {"name": "Pensée des Morts", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "dormhallway",      "priority": PrioEnum.NONE, "sp": 23,       "next": "AE095", "obsflags": [],                "conditions": []}
    eventlibrary['AE095'] = {"name": "Mars, Bringer of War", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "cafeteria",      "priority": PrioEnum.NONE, "sp": 23,       "next": "AE096", "obsflags": [],                "conditions": []}
    eventlibrary['AE095G'] = {"name": "Can't Get No Satisfaction", "girls": ["AE"], "type": EventTypeEnum.CORE,           "location": "dormhallway",      "priority": PrioEnum.NONE, "sp": 23,       "next": "AE096G", "obsflags": [],                "conditions": []}
    eventlibrary['AE096'] = {"name": "Sigfried's Funeral March", "girls": ["AE"], "type": EventTypeEnum.CORE,             "location": "roof",      "priority": PrioEnum.NONE, "sp": 23,       "next": "AE097", "obsflags": [],                "conditions": []}
    eventlibrary['AE096G'] = {"name": "Sympathy for the Devil", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "cafeteria",      "priority": PrioEnum.NONE, "sp": 23,       "next": "AE097G", "obsflags": [],                "conditions": []}
    eventlibrary['AE097'] = {"name": "Silence", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 23,       "next": "AE098", "obsflags": [],                "conditions": []}
    eventlibrary['AE097G'] = {"name": "Gimmie Shelter", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "cafeteria",      "priority": PrioEnum.NONE, "sp": 23,       "next": "AE098G", "obsflags": [],                "conditions": []}
    eventlibrary['AE098'] = {"name": "Give Me Novacaine", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "dormAE",      "priority": PrioEnum.NONE, "sp": 24,       "next": "AE099", "obsflags": [],                "conditions": []}
    eventlibrary['AE098G'] = {"name": "Sister Morphine", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "tokyo",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE099G", "obsflags": [],                "conditions": []}
    eventlibrary['AE098D'] = {"name": "King of the Clouds", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "cafeteria",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE099D", "obsflags": [],                "conditions": []}
    eventlibrary['AE099'] = {"name": "Tannhäuser Overture", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "dormAE",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE100", "obsflags": [],                "conditions": []}
    eventlibrary['AE099G'] = {"name": "War March of the Priests", "girls": ["AE"], "type": EventTypeEnum.CORE,              "location": "tokyo",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE100G", "obsflags": [],                "conditions": []}
    eventlibrary['AE099D'] = {"name": "Dance, Dance", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "tokyo",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE100D", "obsflags": [],                "conditions": []}
    eventlibrary['AE100'] = {"name": "Jupiter, The Bringer Of Jollity", "girls": ["AE"], "type": EventTypeEnum.CORE,        "location": "schoolfront",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE101", "obsflags": [],                "conditions": []}
    eventlibrary['AE100G'] = {"name": "All the Things You Are", "girls": ["AE"], "type": EventTypeEnum.CORE,              "location": "tokyo",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE101", "obsflags": [],                "conditions": []}
    eventlibrary['AE100D'] = {"name": "I Write Sins, Not Tragedies", "girls": ["AE"], "type": EventTypeEnum.CORE,              "location": "tokyo",      "priority": PrioEnum.ALL, "sp": 24,       "next": "AE101", "obsflags": [],                "conditions": []}
    eventlibrary['AE101'] = {"name": "Shiori End", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "dormexterior",     "priority": PrioEnum.NONE,              "next": "", "obsflags": [],                     "conditions": []}

    eventlibrary['AE007b'] = {"name": "Peer Gynt", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hallway",          "priority": PrioEnum.NONE, "sp": 1,    "next": "AE008b", "obsflags": [],                "conditions": []}
    eventlibrary['AE008b'] = {"name": "Made of Stone", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 1,    "next": "AE009b", "obsflags": [],                "conditions": []}
    eventlibrary['AE009b'] = {"name": "Jardins sous la Pluie", "girls": ["AE"], "type": EventTypeEnum.CORE,                     "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 1,    "next": "AE011b", "obsflags": [],                "conditions": []}
    eventlibrary['AE011b'] = {"name": "Symphony No. 92 in G Major", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,    "next": "", "obsflags": [],                     "conditions": []}
    eventlibrary['AE015b'] = {"name": "Symphony No. 92 in G Major", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,    "next": "", "obsflags": [],                     "conditions": []}
    eventlibrary['AE016b'] = {"name": "Shiori End", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "dormexterior",     "priority": PrioEnum.NONE,     "next": "", "obsflags": [],                     "conditions": []}

    #Optional
    eventlibrary['AE005'] = {"name": "Confirmation", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                       "location": "office",          "priority": PrioEnum.NONE, "sp": 1,     "obsflags": ["aftertest"],                      "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['AE010'] = {"name": "Blue Danube", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "obsflags": ["aftersize2"],                     "conditions": [[ConditionEnum.TIMEFLAG, "size2"], [ConditionEnum.FLAG, "AE006_helpinginoffice"]]}

    eventlibrary['AEBE004'] = {"name": "Kâtibim", "girls": ["AE", "BE"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "festival",           "priority": PrioEnum.NONE, "sp": 4,     "obsflags": ["size5"],                     "conditions": [[ConditionEnum.EVENT, "AE050"]]}


    #Core
    eventlibrary['BE001'] = {"name": "Rooftop Reunion", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "roof",             "priority": PrioEnum.NONE, "sp": 0,     "next": "BE003", "obsflags": ["testday"],         "conditions": []}
    eventlibrary['BE002'] = {"name": "Campus Collision", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "BE003", "obsflags": ["testday"],         "conditions": []}
    eventlibrary['BE003'] = {"name": "Cool Drinks with Honoka", "girls": ["BE"], "type": EventTypeEnum.CORE,                            "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "BE004", "obsflags": [],                  "conditions": []}
    eventlibrary['BE004'] = {"name": "Chatting at Soccer Practice", "girls": ["BE"], "type": EventTypeEnum.CORE,                        "location": "track",            "priority": PrioEnum.NONE, "sp": 0,     "next": "BE006", "obsflags": [],                  "conditions": []}
    eventlibrary['BE006'] = {"name": "Meetings and Partings", "girls": ["BE"], "type": EventTypeEnum.CORE,                             "location": "hallway",        "priority": PrioEnum.NONE, "sp": 1,     "next": "BE007", "obsflags": [],                  "conditions": []}
    eventlibrary['BE007'] = {"name": "Lunchtime with Honoka", "girls": ["BE"], "type": EventTypeEnum.CORE,                              "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 1,     "next": "BE008", "obsflags": [],                  "conditions": []}
    eventlibrary['BE008'] = {"name": "Manga Breaktime", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 1,     "next": "BE009", "obsflags": [],                  "conditions": []}
    eventlibrary['BE009'] = {"name": "Goal(s)!", "girls": ["BE"], "type": EventTypeEnum.CORE,                                           "location": "track",            "priority": PrioEnum.NONE, "sp": 1,     "next": "BE011", "obsflags": [],                  "conditions": []}
    #BE size2
    eventlibrary['BE011'] = {"name": "Quitting the Soccer Club", "girls": ["BE"], "type": EventTypeEnum.CORE,                           "location": "track",            "priority": PrioEnum.NONE, "sp": 2,     "next": "BE012", "obsflags": [],                  "conditions": []}
    eventlibrary['BE012'] = {"name": "Action at the Arcade", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "arcade",           "priority": PrioEnum.NONE, "sp": 2,     "next": "BE014", "obsflags": [],                  "conditions": []}
    eventlibrary['BE014'] = {"name": "Bouncing All Over", "girls": ["BE"], "type": EventTypeEnum.CORE,                                  "location": "hallway",          "priority": PrioEnum.NONE, "sp": 2,     "next": "BE015", "obsflags": [],                  "conditions": []}
    eventlibrary['BE015'] = {"name": "Chocolate Study", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "BE016", "obsflags": [],                  "conditions": []}
    eventlibrary['BE016'] = {"name": "Basketboobs", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "auditorium",              "priority": PrioEnum.NONE, "sp": 3,     "next": "BE017", "obsflags": [],                  "conditions": []}
    eventlibrary['BE017'] = {"name": "Shooting Hoops", "girls": ["BE"], "type": EventTypeEnum.CORE,                                     "location": "arcade",           "priority": PrioEnum.NONE, "sp": 3,     "next": "BE018", "obsflags": [],                  "conditions": []}
    eventlibrary['BE018'] = {"name": "Bra Fitting", "girls": ["BE", "PRG"], "type": EventTypeEnum.CORE,                                 "location": "dormBE",           "priority": PrioEnum.NONE, "sp": 3,     "next": "BE019", "obsflags": [],                  "conditions": []}
    eventlibrary['BE019'] = {"name": "The Fabled Skip Day", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "BE020", "obsflags": [],                  "conditions": []}
    eventlibrary['BE020'] = {"name": "Catch of the Day", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "campuscenter",          "priority": PrioEnum.NONE, "sp": 4,     "next": "BE021", "obsflags": [],                  "conditions": []} #affection check maybe?
    eventlibrary['BE021'] = {"name": "Joining the Archery Club", "girls": ["BE"], "type": EventTypeEnum.CORE,                           "location": "woods",            "priority": PrioEnum.NONE, "sp": 4,     "next": "BE022", "obsflags": [],                  "conditions": []}
    eventlibrary['BE022'] = {"name": "A Sneaky Lunch", "girls": ["BE", "WG"], "type": EventTypeEnum.CORE,                              "location": "library",          "priority": PrioEnum.NONE, "sp": 4,     "next": "BE023", "obsflags": [],                  "conditions": []}
    eventlibrary['BE023'] = {"name": "Showdown in Archery", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "track",            "priority": PrioEnum.NONE, "sp": 4,     "next": "BE024", "obsflags": [],                  "conditions": []}
    eventlibrary['BE024'] = {"name": "I Scream, You Cream", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "town",             "priority": PrioEnum.NONE, "sp": 5,     "next": "BE025", "obsflags": [],                  "conditions": []}
    eventlibrary['BE025'] = {"name": "Archery Competition", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "field",            "priority": PrioEnum.NONE, "sp": 5,     "next": "BE026", "obsflags": [],                  "conditions": []}
    eventlibrary['BE026'] = {"name": "Cicada Catching", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "field",            "priority": PrioEnum.NONE, "sp": 5,     "next": "BE027", "obsflags": [],                  "conditions": []}
    eventlibrary['BE027'] = {"name": "Clothes Shopping", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 5,     "next": "BE028", "obsflags": [],                  "conditions": []}
    eventlibrary['BE028'] = {"name": "Arcade Date", "girls": ["BE"], "type": EventTypeEnum.CORE,                                        "location": "arcade",           "priority": PrioEnum.NONE, "sp": 6,     "next": "BE029", "obsflags": [],                  "conditions": []}
    eventlibrary['BE029'] = {"name": "Geology Assignment", "girls": ["BE"], "type": EventTypeEnum.CORE,                                 "location": "classroom",        "priority": PrioEnum.NONE, "sp": 6,     "next": "BE030", "obsflags": [],                  "conditions": []}
    eventlibrary['BE030'] = {"name": "Love Confession", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 6,     "next": "BE031", "obsflags": [],                  "conditions": []}
    eventlibrary['BE031'] = {"name": "Very Special Day", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "dormBE",           "priority": PrioEnum.NONE, "sp": 6,     "next": "BE032", "obsflags": [],                  "conditions": []}
    #BE size3
    eventlibrary['BE032'] = {"name": "The Day After", "girls": ["BE", "AE"], "type": EventTypeEnum.CORE,                                "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BE033", "obsflags": [],                  "conditions": []}
    eventlibrary['BE033'] = {"name": "The Great Debate", "girls": ["BE", "AE"], "type": EventTypeEnum.CORE,                             "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 7,     "next": "BE034", "obsflags": [],                  "conditions": []}
    eventlibrary['BE034'] = {"name": "No More Archery", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "field",            "priority": PrioEnum.NONE, "sp": 7,     "next": "BE035A", "obsflags": [],                 "conditions": []}
    eventlibrary['BE035A'] = {"name": "Just Add Butter", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BE036", "obsflags": [],                  "conditions": []}
    eventlibrary['BE035B'] = {"name": "Pop Flies", "girls": ["BE"], "type": EventTypeEnum.CORE,                                     "location": "track",            "priority": PrioEnum.NONE, "sp": 7,     "next": "BE036", "obsflags": [],                  "conditions": []}
    eventlibrary['BE036'] = {"name": "Flower Gazing", "girls": ["BE", "GTS"], "type": EventTypeEnum.CORE,                               "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 8,     "next": "BE037", "obsflags": [],                  "conditions": []}
    eventlibrary['BE037'] = {"name": "Dock Musing", "girls": ["BE"], "type": EventTypeEnum.CORE,                                        "location": "lakeroad",         "priority": PrioEnum.NONE, "sp": 8,     "next": "BE038A", "obsflags": [],                 "conditions": []}
    eventlibrary['BE038A'] = {"name": "Cooking Club Scene 2", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "classroom",        "priority": PrioEnum.NONE, "sp": 8,     "next": "BE039", "obsflags": [],                  "conditions": []}
    eventlibrary['BE038B'] = {"name": "Based", "girls": ["BE"], "type": EventTypeEnum.CORE,                                      "location": "schoolexterior",    "priority": PrioEnum.NONE, "sp": 8,     "next": "BE039", "obsflags": [],                  "conditions": []}
    eventlibrary['BE039'] = {"name": "Honoka's Roommate", "girls": ["BE"], "type": EventTypeEnum.CORE,                                  "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 8,     "next": "BE041A", "obsflags": [],                  "conditions": []}
    eventlibrary['BE041A'] = {"name": "Cooking Club Scene 3", "girls": ["BE"], "type": EventTypeEnum.CORE,                          "location": "cookingclassroom",     "priority": PrioEnum.NONE, "sp": 9,     "next": "BE042", "obsflags": [],                  "conditions": []}
    eventlibrary['BE041B'] = {"name": "Leaving the Softball Club", "girls": ["BE"], "type": EventTypeEnum.CORE,                         "location": "track",     "priority": PrioEnum.NONE, "sp": 9,     "next": "BE042", "obsflags": [],                  "conditions": []}
    eventlibrary['BE042'] = {"name": "Anything but Yellow Polka Dot", "girls": ["BE"], "type": EventTypeEnum.CORE,                     "location": "hallway",            "priority": PrioEnum.NONE, "sp": 9,     "next": "BE043", "obsflags": [],                  "conditions": []}
    eventlibrary['BE043'] = {"name": "(Insert Movie Here)", "girls": ["BE"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",            "priority": PrioEnum.NONE, "sp": 9,     "next": "BE044", "obsflags": [],                  "conditions": []}
    eventlibrary['BE044'] = {"name": "Beach Day", "girls": ["BE"], "type": EventTypeEnum.CORE,                                       "location": "schoolfront",            "priority": PrioEnum.NONE, "sp": 9,     "next": "BE045", "obsflags": [],                  "conditions": []}
    eventlibrary['BE045'] = {"name": "TomoHono", "girls": ["BE"], "type": EventTypeEnum.CORE,                                       "location": "classroom",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE046", "obsflags": [],                  "conditions": []}
    eventlibrary['BE046'] = {"name": "200m", "girls": ["BE"], "type": EventTypeEnum.CORE,                                       "location": "classroom",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE047", "obsflags": [],                  "conditions": []}
    eventlibrary['BE047'] = {"name": "Pool Floaties", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "businterior",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE048", "obsflags": [],                  "conditions": []}
    eventlibrary['BE048'] = {"name": "Bottom Feeder", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "waterpark",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE049", "obsflags": [],                  "conditions": []}
    eventlibrary['BE049'] = {"name": "To The Stars", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "dormexterior",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE050", "obsflags": [],                  "conditions": []}
    eventlibrary['BE050'] = {"name": "Onward and Outward", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "dormBE",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE051", "obsflags": [],                  "conditions": []}
    #BE size4
    eventlibrary['BE051'] = {"name": "Glad You're Not Dead", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "dormexterior",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE052", "obsflags": [],                  "conditions": []}
    eventlibrary['BE052'] = {"name": "Help Desk", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "classroom",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE053", "obsflags": [],                  "conditions": []}
    eventlibrary['BE053'] = {"name": "Pick a Card", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "dormexterior",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE054", "obsflags": [],                  "conditions": []}
    eventlibrary['BE054'] = {"name": "Unsinkable", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "pool",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE055", "obsflags": [],                  "conditions": []}
    eventlibrary['BE055'] = {"name": "Don't Let Go", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "pool",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE056", "obsflags": [],                  "conditions": []}
    eventlibrary['BE056'] = {"name": "Cramped", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "town",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE057", "obsflags": [],                  "conditions": []}
    eventlibrary['BE057'] = {"name": "Bouncing Back", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "town",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE058", "obsflags": [],                  "conditions": []}
    eventlibrary['BE058'] = {"name": "Pair-esthesia", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "town",            "priority": PrioEnum.NONE, "sp": 10,     "next": "BE059", "obsflags": [],                  "conditions": []}
    eventlibrary['BE059'] = {"name": "Honoka end", "girls": ["BE"], "type": EventTypeEnum.CORE,                                         "location": "classroom",        "priority": PrioEnum.NONE,              "next": "", "obsflags": [],                       "conditions": []}

    #Optional
    eventlibrary['BE005'] = {"name": "Possible Clubs", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,                             "location": "classroom",        "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],                        "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['BE010'] = {"name": "Surprise, Her Boobs are Bigger", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,        "location": "dorminterior",     "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],                       "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['BE013'] = {"name": "Recovering from a Defeat", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,                   "location": "arcade",           "priority": PrioEnum.ALL,               "obsflags": [],                                   "conditions": [[ConditionEnum.FLAG, "BE013_unlock"]]}

    eventlibrary['BEGTS001'] = {"name": "You Make Me Feel Like a Woman", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,        "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.AND, [ConditionEnum.VAR, "BEMode", "Feminine"], [ConditionEnum.EVENT, "BE020"]]]}
    eventlibrary['BEGTS002'] = {"name": "Shining Down", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                         "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": ["size4"],                            "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "global032"], [ConditionEnum.EVENT, "BEGTS001"]]]}
    eventlibrary['BEGTS003'] = {"name": "A Haze of Judgement", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                  "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.EVENT, "BEGTS002"]]}
    eventlibrary['BEGTS004'] = {"name": "Boiling Point", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                        "location": "hallway",          "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.EVENT, "BEGTS003"]]}
    eventlibrary['BEGTS005'] = {"name": "Farewell, My Friend", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                        "location": "lockers",          "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.EVENT, "BEGTS004"]]}

    #Core
    eventlibrary['FMG001'] = {"name": "Tower of Athletics", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                      "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG002", "obsflags": ["testday"],      "conditions": []}
    eventlibrary['FMG002'] = {"name": "Nerd Alert", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "hallway",                      "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG003", "obsflags": [],               "conditions": []}
    eventlibrary['FMG003'] = {"name": "The Agreement", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "library",                  "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG004", "obsflags": [],               "conditions": []}
    eventlibrary['FMG004'] = {"name": "First Time?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "gym",                    "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG007", "obsflags": [],            "conditions": []}
    eventlibrary['FMG007'] = {"name": "Lunch and Hobbies", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "cafeteria",                "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG008", "obsflags": [],               "conditions": []}
    eventlibrary['FMG008'] = {"name": "Everything Hurts", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "dormexterior",             "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG009", "obsflags": [],               "conditions": []}
    eventlibrary['FMG009'] = {"name": "Junk Food Junkie", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                         "location": "cafeteria",                "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG010", "obsflags": [],               "conditions": []}
    #FMG size2
    eventlibrary['FMG010'] = {"name": "The Bigger They Are...", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                     "location": "classroom",            "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG013", "obsflags": [],               "conditions": []}
    eventlibrary['FMG013'] = {"name": "Head Strong", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "gym",                   "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG014", "obsflags": [],               "conditions": []}
    eventlibrary['FMG014'] = {"name": "A Problem Solver", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                         "location": "schoolplanter",            "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG015", "obsflags": [],               "conditions": []}
    eventlibrary['FMG015'] = {"name": "Gifted Gaming", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "town",                     "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG017", "obsflags": [],               "conditions": []}
    eventlibrary['FMG016'] = {"name": "The New Girl", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                             "location": "dorminterior",             "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG017", "obsflags": [],               "conditions": []}
    eventlibrary['FMG017'] = {"name": "Beware... The Curse", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 3,     "next": "FMG018", "obsflags": [],               "conditions": []}
    eventlibrary['FMG018'] = {"name": "IT'S RAW!!!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "cookingclassroom",         "priority": PrioEnum.NONE, "sp": 3,     "next": "FMG019", "obsflags": [],               "conditions": []}
    eventlibrary['FMG019'] = {"name": "You Shine Like the Sun", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                   "location": "roof",                     "priority": PrioEnum.NONE, "sp": 3,     "next": "FMG020", "obsflags": [],               "conditions": []}
    eventlibrary['FMG020'] = {"name": "Fly Me to the Moon", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 3,     "next": "FMG021", "obsflags": [],               "conditions": []}
    eventlibrary['FMG020B'] = {"name": "Yep, You Blew It...", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                     "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG021", "obsflags": [],               "conditions": []}
    eventlibrary['FMG021'] = {"name": "EMUS!", "girls": ["FMG", "AE"], "type": EventTypeEnum.CORE,                                              "location": "library",                  "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG022", "obsflags": [],               "conditions": []}
    eventlibrary['FMG022'] = {"name": "Rock Opera", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "track",                    "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG023", "obsflags": [],               "conditions": []}
    eventlibrary['FMG023'] = {"name": "The Wizard on the Sidewalk", "girls": ["FMG", "GTS"], "type": EventTypeEnum.CORE,                        "location": "town",                     "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG024", "obsflags": [],               "conditions": []}
    eventlibrary['FMG024'] = {"name": "Arcade Run-in", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "arcade",                   "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG026", "obsflags": [],               "conditions": []}
    eventlibrary['FMG026'] = {"name": "Oh No... Cavities", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "town",                   "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG027", "obsflags": [],               "conditions": []}
    eventlibrary['FMG027'] = {"name": "Study Date", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "classroom",                "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG028", "obsflags": [],               "conditions": []}
    eventlibrary['FMG028'] = {"name": "Anything but Golf", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG029", "obsflags": [],               "conditions": []}
    eventlibrary['FMG029'] = {"name": "Man, These Waffles Suck", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG030", "obsflags": [],               "conditions": []}
    #FMG size3
    eventlibrary['FMG030'] = {"name": "Oki", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                      "location": "dormexterior",             "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG031", "obsflags": [],               "conditions": []}
    eventlibrary['FMG031'] = {"name": "What's Your Drive?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "lockers",                  "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG032", "obsflags": [],               "conditions": []}
    eventlibrary['FMG032'] = {"name": "Chumby the Cat", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                           "location": "pool",                     "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG033", "obsflags": [],               "conditions": []}
    eventlibrary['FMG033'] = {"name": "Dress Malfunction", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                                 "location": "classroom",                "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG034", "obsflags": [],               "conditions": []}
    eventlibrary['FMG034'] = {"name": "That's a Huge Bitch!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                    "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG035", "obsflags": [],               "conditions": []}
    eventlibrary['FMG035'] = {"name": "Meet The Mizutanis", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                  "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG036", "obsflags": [],               "conditions": []} 
    eventlibrary['FMG036'] = {"name": "Kamilizard 2000 VS Teen Arachnid", "girls": ["FMG"], "type": EventTypeEnum.CORE,                        "location": "dormFMG",                  "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG037", "obsflags": [],               "conditions": []}
    eventlibrary['FMG037'] = {"name": "Getting Out Of Hand", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "gym",                   "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG038", "obsflags": [],               "conditions": []} 
    eventlibrary['FMG038'] = {"name": "Yokai", "girls": ["FMG", "AE"], "type": EventTypeEnum.CORE,                                              "location": "dorminterior",             "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG039", "obsflags": [],               "conditions": []}
    eventlibrary['FMG039'] = {"name": "Down with the Sickness", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                   "location": "nurseoffice",              "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG040", "obsflags": [],               "conditions": []}
    eventlibrary['FMG040'] = {"name": "Summer Love", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG041", "obsflags": [],               "conditions": []}
    eventlibrary['FMG041'] = {"name": "Lose Yourself", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG042", "obsflags": [],               "conditions": []}
    eventlibrary['FMG042'] = {"name": "Gamer Moment", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                             "location": "dormFMG",                  "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG043", "obsflags": [],               "conditions": []}
    eventlibrary['FMG043'] = {"name": "She Will Be Loved", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "dormFMG",                  "priority": PrioEnum.NONE, "sp": 9,     "next": "FMG044", "obsflags": [],               "conditions": []}
    eventlibrary['FMG044'] = {"name": "Shower Time", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "lockers",                  "priority": PrioEnum.NONE, "sp": 9,     "next": "FMG045", "obsflags": [],               "conditions": []}
    eventlibrary['FMG045'] = {"name": "The Birds and the Bees", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                   "location": "dorminterior",             "priority": PrioEnum.NONE, "sp": 9,     "next": "FMG046", "obsflags": [],               "conditions": []}
    eventlibrary['FMG046'] = {"name": "The Wonders of Cooking", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                            "location": "cookingclassroom",         "priority": PrioEnum.NONE, "sp": 9,     "next": "FMG047", "obsflags": [],               "conditions": []}
    eventlibrary['FMG047'] = {"name": "Kitchen Nightmare", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                                 "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 10,     "next": "FMG048", "obsflags": [],               "conditions": []}
    eventlibrary['FMG048'] = {"name": "What a Twist", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "cafeteria",                "priority": PrioEnum.NONE, "sp": 10,     "next": "FMG049", "obsflags": [],               "conditions": []}
    eventlibrary['FMG049'] = {"name": "Love Hurts", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "dorminterior",                "priority": PrioEnum.NONE, "sp": 10,     "next": "FMG050", "obsflags": [],               "conditions": []}
    #FMG size4
    eventlibrary['FMG050'] = {"name": "What's Good, Shorty?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "dormFMG",                "priority": PrioEnum.NONE, "sp": 10,     "next": "FMG051", "obsflags": [],               "conditions": []}
    eventlibrary['FMG051'] = {"name": "Das a Big Rock", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                           "location": "lockers",                "priority": PrioEnum.NONE, "sp": 11,     "next": "FMG052", "obsflags": [],               "conditions": []}
    eventlibrary['FMG052'] = {"name": "Got That Fresh Fit", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                                  "location": "track",                "priority": PrioEnum.NONE, "sp": 11,     "next": "FMG053", "obsflags": [],               "conditions": []}
    eventlibrary['FMG053'] = {"name": "League of Ancients", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                          "location": "classroom",            "priority": PrioEnum.NONE, "sp": 11,     "next": "FMG054", "obsflags": [],               "conditions": []}
    eventlibrary['FMG054'] = {"name": "The Yang", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                  "location": "gym",                     "priority": PrioEnum.NONE, "sp": 11,     "next": "FMG055", "obsflags": [],               "conditions": []}
    eventlibrary['FMG055'] = {"name": "She Wears Nice Clothes?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                  "location": "supermarket",                "priority": PrioEnum.NONE, "sp": 12,     "next": "FMG056", "obsflags": [],               "conditions": []}
    eventlibrary['FMG056'] = {"name": "Clash of the Titans", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 12,     "next": "FMG057", "obsflags": [],               "conditions": []}
    eventlibrary['FMG057'] = {"name": "It's Fine, Don't Move", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 12,     "next": "FMG058", "obsflags": [],               "conditions": []}
    eventlibrary['FMG058'] = {"name": "Pose For The Fans", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 12,     "next": "FMG059", "obsflags": [],               "conditions": []}
    eventlibrary['FMG059'] = {"name": "Muscles Too Huge", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 13,     "next": "FMG060", "obsflags": [],               "conditions": []}
    eventlibrary['FMG060'] = {"name": "The Truth Revealed", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "roof",                     "priority": PrioEnum.NONE, "sp": 13,     "next": "FMG061", "obsflags": [],               "conditions": []}
    eventlibrary['FMG061'] = {"name": "A Day To Relax", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dormFMG",                     "priority": PrioEnum.NONE, "sp": 13,     "next": "FMG062", "obsflags": [],               "conditions": []}
    eventlibrary['FMG062'] = {"name": "Big Booty Bitches?", "girls": ["FMG", "AE"], "type": EventTypeEnum.CORE,                            "location": "gym",                     "priority": PrioEnum.NONE, "sp": 13,     "next": "FMG063", "obsflags": [],               "conditions": []}
    eventlibrary['FMG063'] = {"name": "A Tough Choice", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "gym",                     "priority": PrioEnum.NONE, "sp": 14,     "next": "FMG064", "obsflags": [],               "conditions": []}
    eventlibrary['FMG064'] = {"name": "I Hate Sand", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                                        "location": "cookingclassroom",    "priority": PrioEnum.NONE, "sp": 14,     "next": "FMG065", "obsflags": [],               "conditions": []}
    eventlibrary['FMG065'] = {"name": "Belly and Abs", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                                        "location": "beach",          "priority": PrioEnum.NONE, "sp": 14,     "next": "FMG066", "obsflags": [],               "conditions": []}
    eventlibrary['FMG066'] = {"name": "Altitude Apprehension", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                          "location": "airport",               "priority": PrioEnum.NONE, "sp": 14,     "next": "FMG067", "obsflags": [],               "conditions": []}
    eventlibrary['FMG067'] = {"name": "Okinawa Bliss", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                                  "location": "okinawa",               "priority": PrioEnum.ALL, "sp": 15,     "next": "FMG068", "obsflags": [],               "conditions": []}
    eventlibrary['FMG068'] = {"name": "Shells By The Shore", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                  "location": "okinawa",                         "priority": PrioEnum.ALL, "sp": 15,     "next": "FMG069", "obsflags": [],               "conditions": []}
    eventlibrary['FMG069'] = {"name": "In Another Life", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "okinawa",                         "priority": PrioEnum.ALL, "sp": 15,     "next": "FMG070", "obsflags": [],               "conditions": []}
    #FMG size5
    eventlibrary['FMG070'] = {"name": "Size Woes", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "okinawa",                         "priority": PrioEnum.ALL, "sp": 15,     "next": "FMG071", "obsflags": [],               "conditions": []}
    eventlibrary['FMG071'] = {"name": "A Big Send-Off", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                                            "location": "airport",      "priority": PrioEnum.ALL, "sp": 16,     "next": "FMG072", "obsflags": [],               "conditions": []}
    eventlibrary['FMG072'] = {"name": "Record Breaking", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dorminterior",               "priority": PrioEnum.NONE, "sp": 16,     "next": "FMG073", "obsflags": [],               "conditions": []}
    eventlibrary['FMG073'] = {"name": "Disaster Zone", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dorminterior",               "priority": PrioEnum.NONE, "sp": 16,     "next": "FMG074", "obsflags": [],               "conditions": []}
    eventlibrary['FMG074'] = {"name": "A Tough Nut to Crack", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dorminterior",               "priority": PrioEnum.ALL, "sp": 16,     "next": "FMG075", "obsflags": [],               "conditions": []}
    eventlibrary['FMG075'] = {"name": "Time to Get Good", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dormexterior",               "priority": PrioEnum.ALL, "sp": 17,     "next": "FMG076", "obsflags": [],               "conditions": []}
    eventlibrary['FMG076'] = {"name": "The Colossus of the Colosseum", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "auditorium",    "priority": PrioEnum.ALL, "sp": 17,     "next": "FMG077", "obsflags": [],               "conditions": []}
    eventlibrary['FMG077'] = {"name": "Huzzah... Sex!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "library",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG079", "obsflags": [],               "conditions": []}
    eventlibrary['FMG079'] = {"name": "The Aftermath", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dormFMG",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG080", "obsflags": [],               "conditions": []}
    eventlibrary['FMG080'] = {"name": "Light Work", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG081", "obsflags": [],               "conditions": []}
    eventlibrary['FMG081'] = {"name": "Date Night", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dormFMG",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG082", "obsflags": [],               "conditions": []}
    eventlibrary['FMG082'] = {"name": "Results May Vary", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "cafeteria",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG083", "obsflags": [],               "conditions": []}
    eventlibrary['FMG083'] = {"name": "Kung Fu Kicking It", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG084", "obsflags": [],               "conditions": []}
    eventlibrary['FMG084'] = {"name": "Master Chef", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                                       "location": "cookingclassroom",   "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG085", "obsflags": [],               "conditions": []}
    eventlibrary['FMG085'] = {"name": "It's Not Kung Fu", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "hallway",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG086", "obsflags": [],               "conditions": []}
    eventlibrary['FMG086'] = {"name": "Parental Meeting", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG087A", "obsflags": [],               "conditions": []}
    eventlibrary['FMG087A'] = {"name": "Thighs That Can Kill", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "cafeteria",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG088", "obsflags": [],               "conditions": []}
    eventlibrary['FMG087B'] = {"name": "Cuddles With Ice Cream and Cocoa", "girls": ["FMG"], "type": EventTypeEnum.CORE,                      "location": "town",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG088", "obsflags": [],               "conditions": []}
    eventlibrary['FMG088'] = {"name": "Snow Fun", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG089", "obsflags": [],               "conditions": []}
    eventlibrary['FMG089'] = {"name": "Protein Overload", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG090", "obsflags": [],               "conditions": []}
    #FMG size6
    eventlibrary['FMG090'] = {"name": "The Big Leagues", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dorminterior",               "priority": PrioEnum.ALL, "sp": 17,     "next": "FMG091", "obsflags": [],               "conditions": []}
    eventlibrary['FMG091'] = {"name": "Imagine Being Too Strong", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "cafeteria",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG092", "obsflags": [],               "conditions": []}
    eventlibrary['FMG092'] = {"name": "Taller But Not Quite Bigger", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "town",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG093A", "obsflags": [],               "conditions": []}
    eventlibrary['FMG093A'] = {"name": "The Final Showdown", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG093B", "obsflags": [],               "conditions": []}
    eventlibrary['FMG093B'] = {"name": "Don't Call it a Comeback", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "track",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG093C", "obsflags": [],               "conditions": []}
    eventlibrary['FMG093C'] = {"name": "All on the Line", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "track",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG094", "obsflags": [],               "conditions": []}
    eventlibrary['FMG094'] = {"name": "Welp, I've Done All I Can", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "field",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG095", "obsflags": [],               "conditions": []}
    eventlibrary['FMG095'] = {"name": "A Man's Greatest Weakness... Titty", "girls": ["FMG"], "type": EventTypeEnum.CORE,                       "location": "dormFMG",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG096", "obsflags": [],               "conditions": []}
    eventlibrary['FMG096'] = {"name": "Regret", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                   "location": "town",               "priority": PrioEnum.NONE, "sp": 17,     "next": "FMG097", "obsflags": [],               "conditions": []}
    eventlibrary['FMG097'] = {"name": "Akira End", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                "location": "hallway",               "priority": PrioEnum.NONE,         "next": "", "obsflags": [],               "conditions": []}

    #Optional
    eventlibrary['FMG005'] = {"name": "Despair in the Hallway", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                           "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 1,     "obsflags": ["aftertest"],                      "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['FMG006'] = {"name": "Crying Over Spilled Milk", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                             "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG011'] = {"name": "Press A to Start", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                              "location": "dormexterior",             "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG010"]]}
    eventlibrary['FMG012'] = {"name": "Rubbing One Out", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                      "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG025'] = {"name": "Disco Queen", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                          "location": "track",                    "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG028"]]}
    eventlibrary['FMG078'] = {"name": "The Holy Grail of Revengeance", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                      "location": "arcade",                    "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG076"]]}
    
    eventlibrary['FMGD001'] = {"name": "Hot Springs and Hotter Women", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                     "location": "lockers",                    "priority": PrioEnum.NONE,              "obsflags": ["size6"],                          "conditions": [[ConditionEnum.AND, [ConditionEnum.AFFECTION, "FMG", ConditionEqualityEnum.GREATERTHANEQUALS, 38], [ConditionEnum.FLAG, "FMG082_Win"]]]}
    
    eventlibrary['FMGGTS001'] = {"name": "Down and Dirty", "girls": ["FMG", "GTS"], "type": EventTypeEnum.OPTIONAL,                         "location": "bakery",                     "priority": PrioEnum.NONE,              "obsflags": ["GTSFMG001"],                                    "conditions": [[ConditionEnum.EVENT, "FMG023"]]}
    eventlibrary['FMGGTS002'] = {"name": "Burger Buddies and Kei", "girls": ["FMG", "GTS"], "type": EventTypeEnum.OPTIONAL,                   "location": "gym",                     "priority": PrioEnum.NONE,              "obsflags": ["size3"],                            "conditions": [[ConditionEnum.EVENT, "FMGGTS001"]]}
    
    eventlibrary['FMGWG001'] = {"name": "Cupcakes or Bust", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                         "location": "library",                     "priority": PrioEnum.NONE,              "obsflags": ["size3" ,"noFMGWG001"],                     "conditions": [[ConditionEnum.OR, [ConditionEnum.EVENT, "WG015"], [ConditionEnum.AND, [ConditionEnum.EVENT, "FMG010"], [ConditionEnum.FLAG, "XX15"]]]]}
    eventlibrary['FMGWG002'] = {"name": "Built like a Gorilla", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                       "location": "hallway",                  "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG033"]]}
    eventlibrary['FMGWG003'] = {"name": "Horā Eiga", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                                   "location": "hallway",                  "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "FMGWG002"], [ConditionEnum.EVENT, "FMG038"]]]}
    eventlibrary['FMGWG004'] = {"name": "An Unstoppable Force", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                        "location": "schoolexterior",           "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "FMGWG003"], [ConditionEnum.EVENT, "FMG064"]]]}
    eventlibrary['FMGWG006'] = {"name": "Fat Woes", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                                 "location": "dormWG",                   "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "FMGWG004"], [ConditionEnum.EVENT, "FMG081"]]]}


    #Core
    eventlibrary['GTS001'] = {"name": "Girl in the Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                  "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 0,          "next": "GTS002", "obsflags": [],       "conditions": []}
    eventlibrary['GTS002'] = {"name": "Planting Seeds", "girls": ["GTS"], "type": EventTypeEnum.CORE,                      "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 0,          "next": "GTS003", "obsflags": [],       "conditions": []}
    eventlibrary['GTS003'] = {"name": "Itadakimasu", "girls": ["GTS"], "type": EventTypeEnum.CORE,                     "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 0,              "next": "GTS004", "obsflags": [],      "conditions": []}
    eventlibrary['GTS004'] = {"name": "Study Buddy", "girls": ["GTS"], "type": EventTypeEnum.CORE,                         "location": "library",          "priority": PrioEnum.NONE, "sp":0,           "next": "GTS006","obsflags": [],        "conditions": []}
    eventlibrary['GTS006'] = {"name": "Puppy Love", "girls": ["GTS"], "type": EventTypeEnum.CORE,                          "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 0,          "next": "GTS007", "obsflags": [],       "conditions": []}
    eventlibrary['GTS007'] = {"name": "Scattered to the Wind", "girls": ["GTS"], "type": EventTypeEnum.CORE,               "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 1,           "next": "GTS008", "obsflags": [],       "conditions": []}
    eventlibrary['GTS008'] = {"name": "Secret Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "roof",             "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS009", "obsflags": [],       "conditions": []}
    eventlibrary['GTS009'] = {"name": "A Tree Between Mountains", "girls": ["GTS", "BE"], "type": EventTypeEnum.CORE,      "location": "town",             "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS011b", "obsflags": [],      "conditions": []}
    #GTS size2
    eventlibrary['GTS011'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS014", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS011_unlock"]]}
    eventlibrary['GTS011b'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS014", "obsflags": [],       "conditions": [[ConditionEnum.NOFLAG, "GTS011_unlock"]]}
    eventlibrary['GTS013'] = {"name": "The Craft of Confection", "girls": ["GTS"], "type": EventTypeEnum.CORE,             "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS015", "obsflags": [],       "conditions": []}
    eventlibrary['GTS014'] = {"name": "A Con or Pro Fession?", "girls": ["GTS"], "type": EventTypeEnum.CORE,               "location": "classroom",        "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS015", "obsflags": [],       "conditions": []}
    eventlibrary['GTS015'] = {"name": "Decisions, Decisions", "girls": ["GTS"], "type": EventTypeEnum.CORE,                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS016", "obsflags": [],       "conditions": []}
    eventlibrary['GTS016'] = {"name": "To Bee or not to Bee", "girls": ["GTS"], "type": EventTypeEnum.CORE,                "location": "schoolplanter",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS017", "obsflags": [],       "conditions": []}
    eventlibrary['GTS017'] = {"name": "Getting Dirty", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "schoolplanter",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS018", "obsflags": [],       "conditions": []}
    eventlibrary['GTS018'] = {"name": "Slam Dunk", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "schoolexterior",   "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS019", "obsflags": [],       "conditions": []}
    eventlibrary['GTS019'] = {"name": "All in the Wrist", "girls": ["GTS"], "type": EventTypeEnum.CORE,                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,          "next": "GTS020", "obsflags": [],       "conditions": []}
    eventlibrary['GTS020'] = {"name": "Confessions of a Lonely Heart", "girls": ["GTS"], "type": EventTypeEnum.CORE,       "location": "roof",             "priority": PrioEnum.NONE, "sp": 3,          "next": "GTS021", "obsflags": [],       "conditions": []}
    eventlibrary['GTS021'] = {"name": "Taking a Breather", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,          "next": "GTS022", "obsflags": [],       "conditions": []}
    eventlibrary['GTS022'] = {"name": "Ya", "girls": ["GTS"], "type": EventTypeEnum.CORE,                                  "location": "library",          "priority": PrioEnum.NONE, "sp": 3,          "next": "GTS023", "obsflags": [],       "conditions": []}
    eventlibrary['GTS023'] = {"name": "Smash Cut", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "schoolexterior",   "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS024", "obsflags": [],       "conditions": []}
    eventlibrary['GTS024'] = {"name": "Splotchy Brown and Curling", "girls": ["GTS"], "type": EventTypeEnum.CORE,          "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS025", "obsflags": [],       "conditions": []}
    eventlibrary['GTS025'] = {"name": "Would it be Okay...?", "girls": ["GTS"], "type": EventTypeEnum.CORE,                "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS027", "obsflags": [],       "conditions": []}
    eventlibrary['GTS026'] = {"name": "Rain Upon the Iris", "girls": ["GTS"], "type": EventTypeEnum.CORE,                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS027", "obsflags": [],       "conditions": []}
    eventlibrary['GTS027'] = {"name": "Knock on Wood", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "roof",             "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": []}
    eventlibrary['GTS028S'] = {"name": "Don't Fear the Rebate", "girls": ["GTS"], "type": EventTypeEnum.CORE,              "location": "town",              "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS015_shopping"]]}
    eventlibrary['GTS028T'] = {"name": "Art of Film", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS015_movie"]]}
    eventlibrary['GTS029'] = {"name": "Growing Pains", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS030", "obsflags": [],       "conditions": []}
    #GTS size3
    eventlibrary['GTS030'] = {"name": "A Change in Scenery", "girls": ["GTS"], "type": EventTypeEnum.CORE,                 "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS031", "obsflags": [],       "conditions": []}
    eventlibrary['GTS031'] = {"name": "Settling In", "girls": ["GTS"], "type": EventTypeEnum.CORE,                         "location": "giantdorminterior","priority": PrioEnum.NONE, "sp": 6,          "next": "GTS032", "obsflags": [],       "conditions": []}
    eventlibrary['GTS032'] = {"name": "Journey of a Thousand Miles", "girls": ["GTS"], "type": EventTypeEnum.CORE,         "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS034", "obsflags": [],       "conditions": []}
    eventlibrary['GTS034'] = {"name": "A Tall Order", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS035", "obsflags": [],       "conditions": []}
    eventlibrary['GTS035'] = {"name": "First Impressions", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS036", "obsflags": [],       "conditions": []}
    eventlibrary['GTS036'] = {"name": "Worth 1000 Words", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS037", "obsflags": [],       "conditions": []}
    eventlibrary['GTS037'] = {"name": "Peak Interest", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS038", "obsflags": [],       "conditions": []}
    eventlibrary['GTS038'] = {"name": "The Faintest Ink ", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "chukanpoint",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS039", "obsflags": [],       "conditions": []} #intended duplicate, temporary until actual gts038 exists
    eventlibrary['GTS039'] = {"name": "Balance", "girls": ["GTS"], "type": EventTypeEnum.CORE,                             "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS040", "obsflags": [],       "conditions": []}
    eventlibrary['GTS040'] = {"name": "Mukashi, Mukashi", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",          "priority": PrioEnum.NONE, "sp": 8,          "next": "GTS041", "obsflags": [],       "conditions": []}
    eventlibrary['GTS041'] = {"name": "The City in the Hills", "girls": ["GTS"], "type": EventTypeEnum.CORE,               "location": "giantdorminterior", "priority": PrioEnum.NONE, "sp": 8,          "next": "GTS042", "obsflags": [],       "conditions": []}
    eventlibrary['GTS042'] = {"name": "It Will Whisper Your Name", "girls": ["GTS"], "type": EventTypeEnum.CORE,           "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 8,          "next": "GTS043", "obsflags": [],       "conditions": []}
    eventlibrary['GTS043'] = {"name": "Powerhouse", "girls": ["GTS", "FMG"], "type": EventTypeEnum.CORE,                   "location": "hallway",          "priority": PrioEnum.NONE, "sp": 8,          "next": "GTS044", "obsflags": [],       "conditions": []}
    eventlibrary['GTS044'] = {"name": "Spéirghealach", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "classroom",        "priority": PrioEnum.NONE, "sp": 9,          "next": "GTS045", "obsflags": [],       "conditions": []}
    eventlibrary['GTS045'] = {"name": "A Legacy to Protect", "girls": ["GTS"], "type": EventTypeEnum.CORE,                 "location": "dormexterior",        "priority": PrioEnum.NONE, "sp": 9,          "next": "GTS046", "obsflags": [],       "conditions": []}
    eventlibrary['GTS046'] = {"name": "The Harder She Falls", "girls": ["GTS"], "type": EventTypeEnum.CORE,                 "location": "giantdorminterior",  "priority": PrioEnum.ALL, "sp": 9,          "next": "GTS047", "obsflags": [],       "conditions": []}
    eventlibrary['GTS047'] = {"name": "Moving the Earth", "girls": ["GTS"], "type": EventTypeEnum.CORE,                     "location": "field",  "priority": PrioEnum.NONE, "sp": 9,          "next": "GTS048", "obsflags": [],       "conditions": []}
    eventlibrary['GTS048'] = {"name": "Placeholder", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "giantdorminterior",  "priority": PrioEnum.NONE, "sp": 10,          "next": "GTS049", "obsflags": [],       "conditions": []}
    eventlibrary['GTS049'] = {"name": "In the Hall of the Mountain Queen", "girls": ["GTS"], "type": EventTypeEnum.CORE,     "location": "giantdorminterior",  "priority": PrioEnum.NONE, "sp": 10,  "next": "GTS050", "obsflags": [],       "conditions": []}
    #GTS size4
    eventlibrary['GTS050'] = {"name": "In the Dead of the Night", "girls": ["GTS"], "type": EventTypeEnum.CORE,     "location": "giantdorminterior",  "priority": PrioEnum.NONE, "sp": 10,  "next": "GTS051", "obsflags": [],       "conditions": []}
    eventlibrary['GTS051'] = {"name": "She Caught the Katy", "girls": ["GTS"], "type": EventTypeEnum.CORE,     "location": "giantdorminterior",  "priority": PrioEnum.NONE, "sp": 10,  "next": "GTS052", "obsflags": [],       "conditions": []}
    eventlibrary['GTS052'] = {"name": "Madwebagaasin", "girls": ["GTS"], "type": EventTypeEnum.CORE,     "location": "field",  "priority": PrioEnum.NONE, "sp": 10,  "next": "GTS053", "obsflags": [],       "conditions": []}
    eventlibrary['GTS053'] = {"name": "Adiós a Jamaica", "girls": ["GTS"], "type": EventTypeEnum.CORE,     "location": "giantdorminterior",  "priority": PrioEnum.NONE, "sp": 10,  "next": "GTS054", "obsflags": [],       "conditions": []}
    eventlibrary['GTS054'] = {"name": "His Good Opinion", "girls": ["GTS"], "type": EventTypeEnum.CORE,     "location": "field",  "priority": PrioEnum.NONE, "sp": 10,  "next": "GTS055", "obsflags": [],       "conditions": []}
    eventlibrary['GTS055'] = {"name": "Sasameyuki", "girls": ["GTS"], "type": EventTypeEnum.CORE,           "location": "field",  "priority": PrioEnum.NONE, "sp": 10,  "next": "GTS056", "obsflags": [],       "conditions": []}
    eventlibrary['GTS056'] = {"name": "Naomi end", "girls": ["GTS"], "type": EventTypeEnum.CORE,               "location": "library",          "priority": PrioEnum.NONE,                   "next": "", "obsflags": [],             "conditions": []}

    #Optional
    eventlibrary['GTS012'] = {"name": "Tea?", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                            "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.EVENT, "GTS011"]]}

    eventlibrary['GTS005'] = {"name": "Rhymes and Reasons", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,             "location": "schoolplanter",    "priority": PrioEnum.GIRL, "sp": 1,          "obsflags": ["aftertest"],              "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['GTS010'] = {"name": "A Head Above the Class", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,      "location": "classroom",        "priority": PrioEnum.GIRL, "sp": 2,          "obsflags": ["aftersize2"],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

    eventlibrary['GTSFMG001'] = {"name": "If You Meet the Buddha...", "girls": ["GTS", "FMG"], "type": EventTypeEnum.OPTIONAL, "location": "campuscenter",    "priority": PrioEnum.NONE,                "obsflags": ["size3", "FMGGTS001"],               "conditions": [[ConditionEnum.OR, [ConditionEnum.EVENT, "FMG016"], [ConditionEnum.EVENT, "GTS010"]]]}

    eventlibrary['GTSPRG001'] = {"name": "A Blooming Opportunity", "girls": ["GTS", "PRG"], "type": EventTypeEnum.OPTIONAL,"location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.OR, [ConditionEnum.EVENT, "GTS013"], [ConditionEnum.EVENT, "PRG013"]]]}

    eventlibrary['GTSWG001'] = {"name": "A Study in Scarlet", "girls": ["GTS", "WG", "PRG"], "type": EventTypeEnum.OPTIONAL,"location": "classroom",    "priority": PrioEnum.NONE,                   "obsflags": ["size3", "WGGTS001", "WGGTS002"],                         "conditions": [[ConditionEnum.EVENT, "GTS013"]]}

    #Core
    eventlibrary['PRG001'] = {"name": "Overtime", "girls": ["PRG"], "type": EventTypeEnum.CORE,                          "location": "classroom",         "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG002", "obsflags": [],       "conditions": []}
    eventlibrary['PRG002'] = {"name": "A Girl in Gray", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                     "location": "hallway",           "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG003", "obsflags": [],       "conditions": []}
    eventlibrary['PRG003'] = {"name": "Mad Skills", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "hallway",           "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG004", "obsflags": [],       "conditions": []}
    eventlibrary['PRG004'] = {"name": "Nature vs Nurture", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "hallway",           "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG006", "obsflags": [],       "conditions": []}
    eventlibrary['PRG006'] = {"name": "Legwork", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG007", "obsflags": [],       "conditions": []}
    eventlibrary['PRG007'] = {"name": "The Koi", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "classroom",         "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG008", "obsflags": [],       "conditions": []}
    eventlibrary['PRG008'] = {"name": "Insane in the Headspace", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG009", "obsflags": [],       "conditions": []}
    eventlibrary['PRG009'] = {"name": "Booked Solid", "girls": ["PRG"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG011", "obsflags": [],       "conditions": []}
    #PRG size2
    eventlibrary['PRG011'] = {"name": "Cups and Measurements", "girls": ["PRG"], "type": EventTypeEnum.CORE,                    "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG012", "obsflags": [],       "conditions": []}
    eventlibrary['PRG012'] = {"name": "Picking the Flower", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                 "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG013", "obsflags": [],       "conditions": []}
    eventlibrary['PRG013'] = {"name": "Go for Gold", "girls": ["PRG"],"type": EventTypeEnum.CORE,                                "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG014", "obsflags": [],       "conditions": []}
    eventlibrary['PRG014'] = {"name": "Major Leagues", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "classroom",         "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG015", "obsflags": [],       "conditions": []}
    eventlibrary['PRG015'] = {"name": "Seal of Approval", "girls": ["PRG"], "type": EventTypeEnum.CORE,                          "location": "classroom",        "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG016", "obsflags": [],       "conditions": []}
    eventlibrary['PRG016'] = {"name": "The First Step", "girls": ["PRG"], "type": EventTypeEnum.CORE,                           "location": "classroom",         "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG017", "obsflags": [],       "conditions": []}
    eventlibrary['PRG017'] = {"name": "Full Bloom", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "schoolplanter",     "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG018", "obsflags": [],       "conditions": []}
    eventlibrary['PRG018'] = {"name": "A Cut Above", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG019", "obsflags": [],       "conditions": []}
    eventlibrary['PRG019'] = {"name": "Cream and Sugar", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                    "location": "classroom",         "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG020", "obsflags": [],       "conditions": []}
    eventlibrary['PRG020'] = {"name": "R&R", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG021", "obsflags": [],       "conditions": []}
    eventlibrary['PRG021'] = {"name": "Back to the Usual", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,            "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG022", "obsflags": [],       "conditions": []}
    eventlibrary['PRG022'] = {"name": "Reality", "girls": ["PRG"], "type": EventTypeEnum.CORE,                              "location": "supermarket",       "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG023", "obsflags": [],       "conditions": []}
    eventlibrary['PRG023'] = {"name": "Healing a Heart", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "library",           "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG024", "obsflags": [],       "conditions": []}
    eventlibrary['PRG024'] = {"name": "Butterflies", "girls": ["PRG"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG025", "obsflags": [],       "conditions": []}
    eventlibrary['PRG025'] = {"name": "Heartfire", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "hallway",      "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG026", "obsflags": [],       "conditions": []}
    eventlibrary['PRG026'] = {"name": "That Which Binds Us", "girls": ["PRG"], "type": EventTypeEnum.CORE,                     "location": "hallway",           "priority": PrioEnum.ALL, "sp": 5,      "next": "PRG027", "obsflags": [],       "conditions": []}
    #PRG size3
    eventlibrary['PRG027'] = {"name": "Rise", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                 "location": "dormPRG",           "priority": PrioEnum.ALL, "sp": 6,     "next": "PRG028", "obsflags": [],       "conditions": []}
    eventlibrary['PRG028'] = {"name": "Two Become One", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",  "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG029", "obsflags": [],       "conditions": []}
    eventlibrary['PRG029'] = {"name": "Procrastination Sensation", "girls": ["PRG"], "type": EventTypeEnum.CORE,         "location": "dormexterior",              "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG0295", "obsflags": [],       "conditions": []}
    eventlibrary['PRG029B'] = {"name": "Double Team", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",              "priority": PrioEnum.ALL, "sp": 6,     "next": "PRG030", "obsflags": [],       "conditions": []}
    eventlibrary['PRG030'] = {"name": "Comfort in Chaos", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",           "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG031", "obsflags": [],       "conditions": []}
    eventlibrary['PRG031'] = {"name": "Seared", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "hallway",              "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG032", "obsflags": [],       "conditions": []}
    eventlibrary['PRG032'] = {"name": "The Charm", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG033", "obsflags": [],       "conditions": []}
    eventlibrary['PRG033'] = {"name": "Hanging Clouds", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG034", "obsflags": [],       "conditions": []}
    eventlibrary['PRG034'] = {"name": "In The Way", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "cookingclassroom",  "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG035", "obsflags": [],       "conditions": []}
    eventlibrary['PRG035'] = {"name": "Black to Blue", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG036", "obsflags": [],       "conditions": []}
    eventlibrary['PRG035B'] = {"name": "In A Nutshell", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dormexterior",      "priority": PrioEnum.ALL, "sp": 8,     "next": "PRG036", "obsflags": [],       "conditions": []}
    eventlibrary['PRG036'] = {"name": "Party Hard", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG037", "obsflags": [],       "conditions": []}
    eventlibrary['PRG037'] = {"name": "Walking Again", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dorminterior",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG038", "obsflags": [],       "conditions": []}
    eventlibrary['PRG038'] = {"name": "Game Night", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG039", "obsflags": [],       "conditions": []}
    eventlibrary['PRG039'] = {"name": "Counselling", "girls": ["PRG"], "type": EventTypeEnum.CORE,               "location": "classroom",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG040", "obsflags": [],       "conditions": []}
    eventlibrary['PRG040'] = {"name": "Box Office", "girls": ["PRG"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG041", "obsflags": [],       "conditions": []}
    eventlibrary['PRG041'] = {"name": "Whispering Reflection", "girls": ["PRG"], "type": EventTypeEnum.CORE,                "location": "dorminterior",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG042", "obsflags": [],       "conditions": []}
    eventlibrary['PRG042'] = {"name": "Just Add Water", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "dorminterior",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG043", "obsflags": [],       "conditions": []}
    eventlibrary['PRG043'] = {"name": "Double Play", "girls": ["PRG"], "type": EventTypeEnum.CORE,                   "location": "dormexterior",         "priority": PrioEnum.NONE, "sp": 10,     "next": "PRG043B", "obsflags": [],       "conditions": []}
    eventlibrary['PRG043B'] = {"name": "Snag", "girls": ["PRG"], "type": EventTypeEnum.CORE,                   "location": "hallway",         "priority": PrioEnum.ALL, "sp": 10,     "next": "PRG044", "obsflags": [],       "conditions": []}
    eventlibrary['PRG044'] = {"name": "For the Dream", "girls": ["PRG"], "type": EventTypeEnum.CORE,              "location": "dorminterior",         "priority": PrioEnum.NONE, "sp": 10,     "next": "PRG045", "obsflags": [],       "conditions": []}
    #PRG size4
    eventlibrary['PRG045'] = {"name": "Downtown Girls", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,              "location": "dormexterior",         "priority": PrioEnum.NONE, "sp": 10,     "next": "PRG046", "obsflags": [],       "conditions": []}
    eventlibrary['PRG046'] = {"name": "Disembark", "girls": ["PRG"], "type": EventTypeEnum.CORE,                    "location": "dorminterior",         "priority": PrioEnum.NONE, "sp": 10,     "next": "PRG047", "obsflags": [],       "conditions": []}
    eventlibrary['PRG047'] = {"name": "More to Learn", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "town",         "priority": PrioEnum.NONE, "sp": 11,     "next": "PRG047B", "obsflags": [],       "conditions": []}
    eventlibrary['PRG047B'] = {"name": "Welcome Home", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "town",         "priority": PrioEnum.NONE, "sp": 11,     "next": "PRG048", "obsflags": [],       "conditions": []}
    eventlibrary['PRG048'] = {"name": "The Kodama Life", "girls": ["PRG"], "type": EventTypeEnum.CORE,                              "location": "town",         "priority": PrioEnum.NONE, "sp": 11,     "next": "PRG049", "obsflags": [],       "conditions": []}
    eventlibrary['PRG049'] = {"name": "Out of the Park", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "town",      "priority": PrioEnum.NONE, "sp": 11,     "next": "PRG050", "obsflags": [],       "conditions": []}
    eventlibrary['PRG050'] = {"name": "Her Voice", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "town",      "priority": PrioEnum.ALL, "sp": 11,     "next": "PRG051", "obsflags": [],       "conditions": []}
    eventlibrary['PRG051'] = {"name": "Derail", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "town",      "priority": PrioEnum.ALL, "sp": 12,     "next": "PRG051B", "obsflags": [],       "conditions": []}
    eventlibrary['PRG051B'] = {"name": "Time Will Tell", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 12,     "next": "PRG052", "obsflags": [],       "conditions": []}
    eventlibrary['PRG052'] = {"name": "Shattered", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 12,     "next": "PRG053", "obsflags": [],       "conditions": []}
    eventlibrary['PRG053'] = {"name": "A Beautiful Morning", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dorminterior",           "priority": PrioEnum.ALL, "sp": 12,     "next": "PRG054", "obsflags": [],       "conditions": []}
    eventlibrary['PRG054'] = {"name": "One Heart", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG055", "obsflags": [],      "conditions": []}
    eventlibrary['PRG055'] = {"name": "Icebreaker", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG056", "obsflags": [],      "conditions": []}
    eventlibrary['PRG056'] = {"name": "Substitutions", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dormPRG",      "priority": PrioEnum.NONE, "sp": 13,    "next": "PRG057", "obsflags": [],      "conditions": []} 
    eventlibrary['PRG057'] = {"name": "Down for a Nap", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "classroom",      "priority": PrioEnum.NONE, "sp": 13,    "next": "PRG057B", "obsflags": [],      "conditions": []}
    eventlibrary['PRG057B'] = {"name": "Crunchtime", "girls": ["PRG"], "type": EventTypeEnum.CORE,                     "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 13,    "next": "PRG058", "obsflags": [],       "conditions": []}
    eventlibrary['PRG058'] = {"name": "Fallen Angel", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "classroom",      "priority": PrioEnum.NONE, "sp": 13,    "next": "PRG059", "obsflags": [],       "conditions": []}
    eventlibrary['PRG059'] = {"name": "Girl Time", "girls": ["PRG"], "type": EventTypeEnum.CORE,                     "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 14,    "next": "PRG060", "obsflags": [],       "conditions": []}
    eventlibrary['PRG060'] = {"name": "The Appetizer", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 14,    "next": "PRG061", "obsflags": [],       "conditions": []}
    eventlibrary['PRG061'] = {"name": "Utterly Attached", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",       "priority": PrioEnum.NONE, "sp": 14,    "next": "PRG062", "obsflags": [],       "conditions": []}
    #PRG size5
    eventlibrary['PRG062'] = {"name": "Echoes of Lunacy", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 14,    "next": "PRG063", "obsflags": [],       "conditions": []}
    eventlibrary['PRG063'] = {"name": "Autumn Rains", "girls": ["PRG"], "type": EventTypeEnum.CORE,                             "location": "hallway",           "priority": PrioEnum.NONE, "sp": 15,    "next": "PRG064", "obsflags": [],       "conditions": []}
    eventlibrary['PRG064'] = {"name": "Where the Fairies Play", "girls": ["PRG"], "type": EventTypeEnum.CORE,                   "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 15,    "next": "PRG065", "obsflags": [],       "conditions": []}
    eventlibrary['PRG065'] = {"name": "All Out", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "hallway",           "priority": PrioEnum.NONE, "sp": 15,    "next": "PRG066", "obsflags": [],       "conditions": []}
    eventlibrary['PRG066'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                 "location": "library",           "priority": PrioEnum.NONE,             "obsflags": [],                         "conditions": []}

    eventlibrary['PRGend_nofather'] = {"name": "Guiding Hand", "girls": ["PRG"], "type": EventTypeEnum.CORE,                    "location": "dorminterior",       "priority": PrioEnum.NONE, "sp": 15,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG027Z'] = {"name": "Guiding Hand", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",       "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG028Z'] = {"name": "Head Case", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                         "location": "hallway",           "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG029Z'] = {"name": "Patchwork", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "hallway",           "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG030Z'] = {"name": "Memoric Gazes", "girls": ["PRG"], "type": EventTypeEnum.CORE,                           "location": "hallway",           "priority": PrioEnum.NONE, "sp": 6,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG031Z'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "library",           "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": []}

    #Optional
    eventlibrary['PRG001b'] = {"name": "Tongue Twister", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                      "location": "schoolexterior",   "priority": PrioEnum.NONE,              "obsflags": ["testday"],                "conditions": [[ConditionEnum.EVENT, "PRG001"]]}
    eventlibrary['PRG005'] = {"name": "Camouflage", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                       "location": "auditorium",       "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],              "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['PRG010'] = {"name": "Buckle Up", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "hallway", "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

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
    #WG size2
    eventlibrary['WG010'] = {"name": "ABC: Always Be Clothing", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 2,     "next": "WG012",  "obsflags": [],                                "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['WG012'] = {"name": "Risky Business", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 2,     "next": "WG015", "obsflags": [],                                "conditions": []}
    eventlibrary['WG015'] = {"name": "This is the Stealth Section", "girls": ["WG", "AE"], "type": EventTypeEnum.CORE,                                                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "WG016", "obsflags": [],                               "conditions": []}
    eventlibrary['WG016'] = {"name": "Game Time Interrupted", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                            "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "WG019", "obsflags": [],                               "conditions": []}
    eventlibrary['WG019'] = {"name": "Helpful Muscle", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                            "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 3,     "next": "WG020", "obsflags": [],                               "conditions": []}
    eventlibrary['WG020'] = {"name": "It Can Be Found Anywhere", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                         "location": "classroom",        "priority": PrioEnum.NONE, "sp": 3,     "next": "WG022", "obsflags": [],                              "conditions": []} #\/ disabled due to affection not being very grindable right now
    eventlibrary['WG022'] = {"name": "The Trial of Smarts", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "classroom",        "priority": PrioEnum.NONE, "sp": 3,     "next": "WG024", "obsflags": [],                               "conditions": []}
    eventlibrary['WG024'] = {"name": "What's She Got That I Haven't Got More Of?", "girls": ["WG"], "type": EventTypeEnum.CORE,                                       "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "WG025", "obsflags": [],                               "conditions": []}
    eventlibrary['WG025'] = {"name": "I Like Big...?", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                            "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 4,     "next": "WG026", "obsflags": [],                               "conditions": []}
    eventlibrary['WG026'] = {"name": "The Lady in the Pool", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "pool",             "priority": PrioEnum.NONE, "sp": 4,     "next": "WG027", "obsflags": [],                               "conditions": []}
    eventlibrary['WG027'] = {"name": "Interoffice Romance", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "WG028", "obsflags": [],                               "conditions": []} #"conditions": [[ConditionEnum.AFFECTION, "WG", ConditionEqualityEnum.GREATERTHANEQUALS, 6]]}
    eventlibrary['WG027A'] = {"name": "Second Chance", "girls": ["WG"], "type": EventTypeEnum.OPTIONALCORE,                                                           "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 4,     "next": "WG028", "obsflags": [],                               "conditions": [[ConditionEnum.AND, [ConditionEnum.AFFECTION, "WG", ConditionEqualityEnum.GREATERTHANEQUALS, 10], [ConditionEnum.FLAG, "WG027A_unlock"]]]}
    eventlibrary['WG028'] = {"name": "Sick Day", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 4,     "next": "WG029", "obsflags": [],                               "conditions": [[ConditionEnum.FLAG, "WG_dating"]]}
    #WG size3
    eventlibrary['WG029'] = {"name": "No \"Big Day\" Puns, Please", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "WG030", "obsflags": [],                               "conditions": []}
    eventlibrary['WG030'] = {"name": "Who Are the Ad Wizards...", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 5,     "next": "WG031", "obsflags": [],                               "conditions": []}
    eventlibrary['WG031'] = {"name": "Future Prospects", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                 "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "WG033", "obsflags": [],                               "conditions": []}
    eventlibrary['WG033'] = {"name": "Smells Like Team Spirit", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                          "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "WG034", "obsflags": [],                               "conditions": []}
    eventlibrary['WG034'] = {"name": "Styling and Profiling", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                            "location": "town",             "priority": PrioEnum.NONE, "sp": 6,     "next": "WG035", "obsflags": [],                               "conditions": []}
    eventlibrary['WG035'] = {"name": "It's Showtime", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                    "location": "auditorium",       "priority": PrioEnum.NONE, "sp": 6,     "next": "WG036", "obsflags": [],                                "conditions": []}
    eventlibrary['WG036'] = {"name": "A Meeting with the Boss", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                          "location": "auditorium",       "priority": PrioEnum.NONE, "sp": 6,     "next": "WG037", "obsflags": [],                                "conditions": []}
    eventlibrary['WG037'] = {"name": "A Pleasant Day in Pleasant Town", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                  "location": "dorminterior",        "priority": PrioEnum.NONE, "sp": 6,     "next": "WG038", "obsflags": [],                               "conditions": []}
    eventlibrary['WG038'] = {"name": "Beck and Call", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "WG039", "obsflags": [],                               "conditions": []}
    eventlibrary['WG039'] = {"name": "Helping Hands", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                   "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "WG041", "obsflags": [],                               "conditions": []} # >=20 affection
    eventlibrary['WG041'] = {"name": "Carnival of Delights", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "festival",        "priority": PrioEnum.NONE, "sp": 7,     "next": "WG042", "obsflags": [],                               "conditions": []}
    eventlibrary['WG042'] = {"name": "Carnival of Sins", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                 "location": "festival",        "priority": PrioEnum.ALL, "sp": 7,      "next": "WG043", "obsflags": [],                                "conditions": []}
    eventlibrary['WG043'] = {"name": "Pool Sharks", "girls": ["WG", "PRG", "BE", "FMG"], "type": EventTypeEnum.CORE,                                                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 8,     "next": "WG044", "obsflags": [],                               "conditions": []}
    eventlibrary['WG044'] = {"name": "A Totally Fitting Meeting", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 8,     "next": "WG045", "obsflags": [],                               "conditions": []}
    eventlibrary['WG045'] = {"name": "A Regrettable Rendezvous", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                 "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 8,     "next": "WG046", "obsflags": [],                               "conditions": []}
    eventlibrary['WG046'] = {"name": "Arrival and Unpacking", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                            "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 8,     "next": "WG047", "obsflags": [],                               "conditions": []}
    eventlibrary['WG047'] = {"name": "Full Coverage", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                             "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 9,    "next": "WG048", "obsflags": [],                               "conditions": []}
    eventlibrary['WG048'] = {"name": "Dinner is Served", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                          "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 9,    "next": "WG049", "obsflags": [],                               "conditions": []}
    eventlibrary['WG049'] = {"name": "Going the Distance", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                       "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 9,    "next": "WG050", "obsflags": [],                               "conditions": []}
    eventlibrary['WG050'] = {"name": "A Feast for the Eyes", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                     "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 9,    "next": "WG051", "obsflags": [],                               "conditions": []}
    eventlibrary['WG051'] = {"name": "Serve's Up!", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                              "location": "summer-beach",     "priority": PrioEnum.ALL, "sp": 10,      "next": "WG052", "obsflags": [],                               "conditions": []}
    eventlibrary['WG052'] = {"name": "Departure", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                        "location": "summer-beach",     "priority": PrioEnum.ALL, "sp": 10,      "next": "WG053", "obsflags": [],                               "conditions": []}
    #WG size4
    eventlibrary['WG053'] = {"name": "The Music of the Night", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG054", "obsflags": [],                               "conditions": []}
    eventlibrary['WG054'] = {"name": "Sweet Dreams (Are made of what?)", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 10,     "next": "WG055", "obsflags": [],                               "conditions": []}
    eventlibrary['WG055'] = {"name": "Music in the Garden", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 11,     "next": "WG056", "obsflags": [],                               "conditions": []}
    eventlibrary['WG056'] = {"name": "A Sisterly Bond", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 11,     "next": "WG057", "obsflags": [],                               "conditions": []}
    eventlibrary['WG057'] = {"name": "Chef Boyhairdee", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 11,     "next": "WG059", "obsflags": [],                               "conditions": []}
    eventlibrary['WG059'] = {"name": "Puff Pastry and Pears", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 11,     "next": "WG060", "obsflags": [],                               "conditions": []}
    eventlibrary['WG059S'] = {"name": "A Fattening Proposition", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                         "location": "dormWG",            "priority": PrioEnum.NONE, "sp": 11,     "next": "WG060S", "obsflags": [],                               "conditions": []}
    eventlibrary['WG060'] = {"name": "Bedside Manner", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                  "location": "classroom",        "priority": PrioEnum.NONE, "sp": 12,     "next": "WG061", "obsflags": [],                               "conditions": []}
    eventlibrary['WG060S'] = {"name": "Pushing Bounds and Buttons", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                     "location": "dorminterior",     "priority": PrioEnum.ALL, "sp": 12,     "next": "WG061S", "obsflags": [],                               "conditions": []}
    eventlibrary['WG061'] = {"name": "Bon Appetite", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                           "location": "cookingclassroom",     "priority": PrioEnum.NONE, "sp": 12,     "next": "WG062", "obsflags": [],                               "conditions": []}
    eventlibrary['WG061S'] = {"name": "Through Thick and Thicker", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                      "location": "dormWG",            "priority": PrioEnum.ALL, "sp": 12,     "next": "WG062", "obsflags": [],                               "conditions": []}
    eventlibrary['WG061D'] = {"name": "A False Impression", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",        "priority": PrioEnum.ALL, "sp": 12,     "next": "WG062", "obsflags": [],                               "conditions": []}
    eventlibrary['WG062'] = {"name": "Breast Friend, Biggest Ally", "girls": ["WG", "BE"], "type": EventTypeEnum.CORE,                                              "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 12,     "next": "WG063", "obsflags": [],                               "conditions": []}
    eventlibrary['WG063'] = {"name": "A Very Unfitting Meeting", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 12,     "next": "WG064", "obsflags": [],                               "conditions": []}
    eventlibrary['WG064'] = {"name": "The Sorceress and the Seamstress", "girls": ["WG"], "type": EventTypeEnum.CORE,                                              "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 13,     "next": "WG066", "obsflags": [],                               "conditions": []}
    eventlibrary['WG066'] = {"name": "Sister Golden Hair Surmised", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                      "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 13,     "next": "WG067", "obsflags": [],                               "conditions": []}
    eventlibrary['WG067'] = {"name": "Down to the Letter", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "dormWG",             "priority": PrioEnum.NONE, "sp": 13,     "next": "WG068", "obsflags": [],                               "conditions": []}
    eventlibrary['WG068'] = {"name": "The Lady in Waiting", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 13,     "next": "WG069", "obsflags": [],                               "conditions": []}
    eventlibrary['WG069'] = {"name": "Having a Ball", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 14,     "next": "WG070", "obsflags": [],                               "conditions": []}
    eventlibrary['WG070'] = {"name": "The Businessman and the Ballroom", "girls": ["WG"], "type": EventTypeEnum.CORE,                                           "location": "ballroom",      "priority": PrioEnum.ALL, "sp": 14,     "next": "WG071", "obsflags": [],                               "conditions": []}
    eventlibrary['WG071'] = {"name": "Made it to the Big Time", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                    "location": "ballroom",      "priority": PrioEnum.ALL, "sp": 14,     "next": "WG072", "obsflags": [],                               "conditions": []}
    eventlibrary['WG072'] = {"name": "In the Morning Light", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                       "location": "ballroom",      "priority": PrioEnum.ALL, "sp": 14,     "next": "WG073", "obsflags": [],                               "conditions": []}
    #WG size5
    eventlibrary['WG073'] = {"name": "A Weighty Issue", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                       "location": "dormWG",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG074", "obsflags": [],                               "conditions": []}
    eventlibrary['WG074'] = {"name": "Mix it Up", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                       "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG075", "obsflags": [],                               "conditions": []}
    eventlibrary['WG075'] = {"name": "Mutual Admiration", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "dormWG",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG076", "obsflags": [],                               "conditions": []}
    eventlibrary['WG076'] = {"name": "A Tight Fit", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                     "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG077", "obsflags": [],                               "conditions": []}
    eventlibrary['WG077'] = {"name": "Chef Boy Hairdee Part Deux", "girls": ["WG"], "type": EventTypeEnum.CORE,                                "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG078", "obsflags": [],                               "conditions": []}
    eventlibrary['WG078'] = {"name": "Party Time", "girls": ["WG", "PRG", "BE"], "type": EventTypeEnum.CORE,                                    "location": "hallway",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG079", "obsflags": [],                               "conditions": []}
    eventlibrary['WG079'] = {"name": "Drawn Together", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "hallway",      "priority": PrioEnum.ALL, "sp": 15,     "next": "WG080", "obsflags": [],                               "conditions": []}
    eventlibrary['WG080'] = {"name": "Counselor Busybody", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "classroom",      "priority": PrioEnum.ALL, "sp": 15,     "next": "WG081", "obsflags": [],                               "conditions": []}
    eventlibrary['WG081'] = {"name": "The Mother Load", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "schoolexterior",      "priority": PrioEnum.ALL, "sp": 15,     "next": "WG082", "obsflags": [],                               "conditions": []}
    eventlibrary['WG082'] = {"name": "Signs of Change", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "dormWG",              "priority": PrioEnum.NONE, "sp": 15,     "next": "WG084", "obsflags": [],                               "conditions": []}
    eventlibrary['WG084'] = {"name": "The Discordant Duo", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "musicclassroom",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG085", "obsflags": [],                               "conditions": []}
    eventlibrary['WG085'] = {"name": "Fat Floats", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "lockers",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG086", "obsflags": [],                               "conditions": []}
    eventlibrary['WG086'] = {"name": "Don't Fill Up On Bread", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "dormWG",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG087", "obsflags": [],                               "conditions": []}
    eventlibrary['WG087'] = {"name": "Movie Night", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "dormWG",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG088", "obsflags": [],                               "conditions": []}
    eventlibrary['WG088'] = {"name": "Music With A Side Of Donuts", "girls": ["WG"], "type": EventTypeEnum.CORE,                                     "location": "musicclassroom",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG089", "obsflags": [],                               "conditions": []}
    eventlibrary['WG089'] = {"name": "The Sundering", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                  "location": "dormWG",      "priority": PrioEnum.NONE, "sp": 15,     "next": "WG090", "obsflags": [],                               "conditions": []}
    eventlibrary['WG090'] = {"name": "Pillars of Support", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                  "location": "classroom",      "priority": PrioEnum.ALL, "sp": 15,     "next": "WG091", "obsflags": [],                               "conditions": []}
    eventlibrary['WG091'] = {"name": "Take a Load Off", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "town",          "priority": PrioEnum.ALL,     "next": "WG092", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG092'] = {"name": "Dinner and a Show", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "town",          "priority": PrioEnum.ALL,     "next": "WG093", "obsflags": [],                                     "conditions": []}
    #WG size6
    eventlibrary['WG093'] = {"name": "Larger Than Life", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dormWG",          "priority": PrioEnum.NONE,     "next": "WG094", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG094'] = {"name": "A Big Impression", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "summer-beach",          "priority": PrioEnum.NONE,     "next": "WG095", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG095'] = {"name": "The Better Man", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dormWG",          "priority": PrioEnum.NONE,     "next": "WG096", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG096'] = {"name": "Expanding Her Empire", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "classroom",          "priority": PrioEnum.NONE,     "next": "WG097", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG097'] = {"name": "Time for a Do-Over", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "town",          "priority": PrioEnum.NONE,     "next": "WG098", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG098'] = {"name": "It Ain't Over Til'...", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dormWG",          "priority": PrioEnum.NONE,     "next": "WG099", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG099'] = {"name": "Made it to the Big Time", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "campuscenter",          "priority": PrioEnum.NONE,     "next": "WG100", "obsflags": [],                                     "conditions": []}
    eventlibrary['WG100'] = {"name": "Alice end", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "library",          "priority": PrioEnum.NONE,     "next": "", "obsflags": [],                                     "conditions": []}

    #Optional
    eventlibrary['WG009'] = {"name": "Between a Soft and a Hard Place", "girls": ["WG", "PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                "location": "pool",             "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.EVENT, "WG008"]]}
    eventlibrary['WG011'] = {"name": "True Romance", "girls": ["WG", "PRG"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],               "conditions": [[ConditionEnum.EVENT, "WG008"]]}
    eventlibrary['WG001M'] = {"name": "Practice Makes Passable", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                   "location": "musicclassroom",          "priority": PrioEnum.NONE,              "obsflags": [],           "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG010"], [ConditionEnum.SKILL, "Art", ConditionEqualityEnum.GREATERTHANEQUALS, 3]]]}
    eventlibrary['WG013'] = {"name": "The Elephant In The Room", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                     "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],               "conditions": [[ConditionEnum.EVENT, "WG012"]]}
    eventlibrary['WG014'] = {"name": "Silence Can Be Heavy", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                         "location": "auditorium",              "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.EVENT, "WG012"]]}
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
    eventlibrary['WG083'] = {"name": "An Unexpected Guest", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                            "location": "dorminterior",            "priority": PrioEnum.NONE,              "obsflags": [],      "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG082"], [ConditionEnum.NOEVENT, "WG089"]]]}
    eventlibrary['WG004M'] = {"name": "To Play the Fool", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                             "location": "musicclassroom",    "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG003M"], [ConditionEnum.AND, [ConditionEnum.EVENT, "WG075"], [ConditionEnum.SKILL, "Art", ConditionEqualityEnum.GREATERTHANEQUALS, 14]]]]}
    eventlibrary['WG005M'] = {"name": "Practice Pays Dividends", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                             "location": "musicclassroom",    "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.NOEVENT, "WG102"], [ConditionEnum.AND, [ConditionEnum.EVENT, "WG004M"], [ConditionEnum.AND, [ConditionEnum.EVENT, "WG093"], [ConditionEnum.SKILL, "Art", ConditionEqualityEnum.GREATERTHANEQUALS, 20]]]]]}

    eventlibrary['WGAE001'] = {"name": "Butting Into Her Business", "girls": ["WG", "AE"], "type": EventTypeEnum.OPTIONAL,                                        "location": "hallway",        "priority": PrioEnum.NONE,              "obsflags": ["size3"],            "conditions": [[ConditionEnum.EVENT, "WG012"]]}

    eventlibrary['WGBE001'] = {"name": "So Bad It's Good", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.AND, [ConditionEnum.FLAG, "DormWG_Seen"], [ConditionEnum.NOEVENT, "WG044"]]]}
    eventlibrary['WGBE002'] = {"name": "Fashion Faux Pas", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "schoolexterior",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG035"], [ConditionEnum.NOEVENT, "WG044"]]]}
    eventlibrary['WGBE003'] = {"name": "It's a Miracle!", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "dormWG",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.EVENT, "WG062"]]}
    eventlibrary['WGBE004A'] = {"name": "Beat 'Em Ups & Brownies", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "dormWG",        "priority": PrioEnum.NONE,              "obsflags": ["size6"],            "conditions": [[ConditionEnum.EVENT, "WG082"]]}
    eventlibrary['WGBE004B'] = {"name": "A Bad Batch", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "cookingclassroom",        "priority": PrioEnum.ALL,              "obsflags": [],            "conditions": [[ConditionEnum.EVENT, "WGBE004A"]]}
    #eventlibrary['WGBE005'] = {"name": "Something Old, Something New", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                            "location": "cafeteria",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG094"], [ConditionEnum.AND, [ConditionEnum.FLAG, "WGBE2"], [ConditionEnum.FLAG, "WGGTS2"]]]]}
    eventlibrary['WGBE005'] = {"name": "Something Old, Something New", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                            "location": "cafeteria",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.EVENT, "WG094"]]}

    eventlibrary['WGFMG001'] = {"name": "Afraid of a Little Fun?", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                             "location": "gym",               "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.NOEVENT, "WG043"], [ConditionEnum.OR, [ConditionEnum.EVENT, "WG032"], [ConditionEnum.EVENT, "WG037"]]]]}
    eventlibrary['WGFMG002'] = {"name": "Tamer of Dragons", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                   "location": "dorminterior",     "priority": PrioEnum.NONE,              "obsflags": [],                  "conditions": [[ConditionEnum.EVENT, "WG043"]]}
    eventlibrary['WGFMG003'] = {"name": "An Immovable Object", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "schoolexterior",     "priority": PrioEnum.NONE,              "obsflags": ["size5"],        "conditions": [[ConditionEnum.EVENT, "WG063"]]}
    eventlibrary['WGFMG004A'] = {"name": "Tropical Getaway", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "dormexterior",     "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.AND, [ConditionEnum.NOEVENT, "WG079"], [ConditionEnum.AND, [ConditionEnum.FLAG, "WGFMG001_3"], [ConditionEnum.EVENT, "WG074"]]]]}
    eventlibrary['WGFMG004B'] = {"name": "Soba Shop Showdown", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "okinawa",     "priority": PrioEnum.ALL,              "obsflags": [],                "conditions": [[ConditionEnum.EVENT, "WGFMG004A"]]}
    eventlibrary['WGFMG005'] = {"name": "Rearrangement", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "dormWG",     "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.EVENT, "WG084"]]}

    eventlibrary['WGGTS001'] = {"name": "Off to a Bad Start", "girls": ["WG", "GTS"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": ["size3", "GTSWG001"],            "conditions": [[ConditionEnum.EVENT, "WG005"]]}
    eventlibrary['WGGTS002'] = {"name": "Aggressive Expansion", "girls": ["WG", "GTS"], "type": EventTypeEnum.OPTIONAL,                                               "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": ["size3"],           "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG012"], [ConditionEnum.NOEVENT, "WGAE001"]]]}
    eventlibrary['WGGTS003'] = {"name": "Delivery Boy Debacle", "girls": ["WG", "GTS"], "type": EventTypeEnum.OPTIONAL,                                               "location": "dormexterior",     "priority": PrioEnum.NONE,              "obsflags": ["size4"],           "conditions": [[ConditionEnum.EVENT, "WG022"]]}
    eventlibrary['WGGTS004'] = {"name": "A Growing Business", "girls": ["WG", "GTS"], "type": EventTypeEnum.OPTIONAL,                                                "location": "dormexterior",     "priority": PrioEnum.NONE,              "obsflags": ["size5"],           "conditions": [[ConditionEnum.AND, [ConditionEnum.TIMEFLAG, "size4"], [ConditionEnum.EVENT, "WG054"]]]}
    eventlibrary['WGGTS005'] = {"name": "A Peace of Clothing", "girls": ["WG", "GTS", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "dorminterior",        "priority": PrioEnum.ALL,              "obsflags": [],            "conditions": [[ConditionEnum.EVENT, "WGBE005"]]}