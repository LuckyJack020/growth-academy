init python:
    #LIST OF DATES SHOULD BE IN REVERSE ORDER (LAST EVENT IS FIRST IN LIST)
    #name: (string) Name of character
    #affection: (string or None) Affection index of character, if tracked. If not, then "None"
    #DOB: (string) Birthday of character
    #height: (list of tuple<string, int>) Height of character. String in tuple corresponds to date code, integer corresponds to height in cm.
    #weight: (list of tuple<string, int>) Weight of character. String in tuple corresponds to date code, integer corresponds to weight in kg.
    #factor: (string) Description of factor. Hidden until flag "<key>_factor" is raised, or date code of Factorlimit has been passed.
    #factorlimit: (string) Datecode, after which Factor (above) is revealed. If empty (""), then this functionality is ignored.
    #pimgdates: (list of string or None) List of datecodes for size changes to make updating profile images work. If none, then profile image does not update.
    #desc: (list of tuple<list of tuple<string, boolean>, string>)
    #Outer list is a list of description lines, each description line being a list of conditions and a line added to the description if all the conditions pass.
    #Condition list is a list of tuples, the first string in the tuple being a flag, and the second being a boolean value for whether the flag should exist or not if the condition passes.

    profiles = {"MC":
        {
            "name": "Keisuke Hotsure",
            "affection": None,
            "sex": True,
            "DOB": "1/1/2000",
            "height": [("day_0", 100)],
            "weight": [("day_0", 100)],
            "factor": "Hair growth",
            "factorlimit": "",
            "pimgdates": None,
            "desc": [
                ([], "It's Kei-kun. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae lacinia sapien, at eleifend mauris. Fusce molestie egestas dui a faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec lacinia rutrum condimentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ex lacus, pellentesque vitae mattis sed, sollicitudin eu leo. Sed sed mauris aliquam, sollicitudin eros sit amet, tempor felis. Nunc erat nunc, pellentesque vitae fringilla id, commodo quis orci. Praesent vitae augue vitae ex vehicula congue. Vestibulum vel venenatis enim, vitae vestibulum erat."),
                ([("test", True)], "Hello this is a second line.")]
        },
        "BE":
        {
            "name": "Honoka Inoue",
            "affection": "BE",
            "sex": False,
            "DOB": "1/1/2000",
            "height": [("day_0", 100)],
            "weight": [("BE_size_2", 200), ("day_0", 100)],
            "BWH": [("BE_size_2", [9999, 50, 50]), ("day_0", [999, 50, 50])],
            "factor": "Breast growth",
            "factorlimit": "BE_size_3",
            "pimgdates": ["BE_size_2", "day_0"],
            "desc": [
                ([], "Graduated from Otenba High School after moving to the school district at the end of her Elementary School career. Member of multiple clubs, but never one for very long. No notable scholastic achievements. Excels in athletic activities, with her most prominent hobby being soccer. Currently has no inclination towards an occupation after leaving Seichou Academy."),
                ([("test", False)], "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae lacinia sapien, at eleifend mauris. Fusce molestie egestas dui a faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec lacinia rutrum condimentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ex lacus, pellentesque vitae mattis sed, sollicitudin eu leo. Sed sed mauris aliquam, sollicitudin eros sit amet, tempor felis. Nunc erat nunc, pellentesque vitae fringilla id, commodo quis orci. Praesent vitae augue vitae ex vehicula congue. Vestibulum vel venenatis enim, vitae vestibulum erat."),
                ([("test", True)], "Hello this is a replacement line.")]
        },
        "AE":
        {
            "name": "Shiori Matsumoto",
            "affection": "AE",
            "sex": False,
            "DOB": "1/1/2000",
            "height": [("day_0", 100)],
            "weight": [("AE_size_2", 200), ("day_0", 100)],
            "BWH": [("AE_size_2", [50, 50, 9999]), ("day_0", [50, 50, 999])],
            "factor": "Butt growth",
            "factorlimit": "AE_size_3",
            "pimgdates": ["AE_size_2", "day_0"],
            "desc": [
                ([], "Graduated Summa Cum Laude from the Tokyo Provincial Highschool with exemplary status, despite not receiving prior private education on record. President of the Student Council, Disciplinary Committee and Class President from enrollment to graduation; non-electorate. Came highly recommended for compulsory election into the Seichou Student Council based on effectiveness of position. Prior to enrollment into Seichou, received a scholarship to study law with beyond sufficient placement examination; on hold until graduation."),
                ([("test", True)], "Hello this is a second line.")]
        },
        "GTS":
        {
            "name": "Naomi Yamazaki",
            "affection": "GTS",
            "sex": False,
            "DOB": "1/1/2000",
            "height": [("GTS_size_2", 9999), ("day_0", 1000)],
            "weight": [("GTS_size_2", 200), ("day_0", 100)],
            "BWH": [("day_0", [999, 50, 50])],
            "factor": "Height growth",
            "factorlimit": "GTS_size_3",
            "pimgdates": ["GTS_size_2", "day_0"],
            "desc": [
                ([], "Graduated from Kyoto Cultural Private School with high marks. Was often praised for never missing an assignment or even a day of class, while also never receiving disciplinary action. Partook in International and Cultural Studies Courses while enrolled with a promising future in business. Prior to enrollment into Seichou, was believed to have been seeking admission into Senzai University of Arts and Science like her parents before her."),
                ([("test", True)], "Hello this is a second line.")]
        },
        "FMG":
        {
            "name": "Akira Mizutani",
            "affection": "FMG",
            "sex": False,
            "DOB": "1/1/2000",
            "height": [("day_0", 100)],
            "weight": [("FMG_size_2", 200), ("day_0", 100)],
            "BWH": [("day_0", [50, 50, 999])],
            "factor": "Muscle growth",
            "factorlimit": "FMG_size_3",
            "pimgdates": ["FMG_size_2", "day_0"],
            "desc": [
                ([], "It's Akira-kun. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae lacinia sapien, at eleifend mauris. Fusce molestie egestas dui a faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec lacinia rutrum condimentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ex lacus, pellentesque vitae mattis sed, sollicitudin eu leo. Sed sed mauris aliquam, sollicitudin eros sit amet, tempor felis. Nunc erat nunc, pellentesque vitae fringilla id, commodo quis orci. Praesent vitae augue vitae ex vehicula congue. Vestibulum vel venenatis enim, vitae vestibulum erat."),
                ([("test", True)], "Hello this is a second line.")]
        },
        "BBW":
        {
            "name": "Alice Nikumaru",
            "affection": "BBW",
            "sex": False,
            "DOB": "1/1/2000",
            "height": [("day_0", 100)],
            "weight": [("BBW_size_2", 1500), ("day_0", 100)],
            "BWH": [("BBW_size_2", [50, 9999, 50]), ("day_0", [50, 999, 50])],
            "factor": "Fat growth",
            "factorlimit": "BBW_size_3",
            "pimgdates": ["BBW_size_3", "BBW_size_2", "day_0"],
            "desc": [
                ([], "Graduated from Golden Chrysanthemum Academy in Tokyo with high marks. Previous time spent at Langdon Hills Academy in America. No disciplinary record. Member of Future Business Leaders club. Spent two years as class treasurer. Was on shortlist for admission to Tokyo University, as well as other high-ranking institutions outside Japan, prior to enrollment at Seichou."),
                ([("test", True)], "Hello this is a second line.")]
        },
        "PRG":
        {
            "name": "Aida Kodama",
            "affection": "PRG",
            "sex": False,
            "DOB": "1/1/2000",
            "height": [("day_0", 100)],
            "weight": [("PRG_size_2", 200), ("day_0", 100)],
            "BWH": [("PRG_size_2", [50, 9999, 50]), ("day_0", [50, 999, 50])],
            "factor": "Fertility growth",
            "factorlimit": "PRG_size_3",
            "pimgdates": ["PRG_size_2", "day_0"],
            "desc": [
                ([], "It's Aida-kun. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae lacinia sapien, at eleifend mauris. Fusce molestie egestas dui a faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec lacinia rutrum condimentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ex lacus, pellentesque vitae mattis sed, sollicitudin eu leo. Sed sed mauris aliquam, sollicitudin eros sit amet, tempor felis. Nunc erat nunc, pellentesque vitae fringilla id, commodo quis orci. Praesent vitae augue vitae ex vehicula congue. Vestibulum vel venenatis enim, vitae vestibulum erat."),
                ([("test", True)], "Hello this is a second line.")]
        },
        "RM":
        {
            "name": "Daichi Kuuchibiru",
            "affection": "RM",
            "sex": True,
            "DOB": "1/1/2000",
            "height": [("day_0", 100)],
            "weight": [("day_0", 100)],
            "factor": "None",
            "factorlimit": "",
            "pimgdates": None,
            "desc": [
                ([], "It's Daichi."),
                ([("test", True)], "Hello this is a second line.")]
        }
    }
    profilepages = {"main": ["MC", None, "BE", None, "AE", None, "GTS", None, "FMG", None, "BBW", None, "PRG", None],
        "minor": ["RM", None, None, None, None, None, None, None, None, None, None, None, None, None]}
    activeprofile = ""
    activepage = "main"

    def getProfileStat(key, stat):
        if stat == "BWH":
            for t in profiles[key][stat]:
                if gametime > datelibrary[t[0]]:
                    return str(t[1][0]) + " / " + str(t[1][1]) + " / " + str(t[1][2])
        elif stat == "factor":
            if getFlag(key + "_factor") or (profiles[key]["factorlimit"] != "" and gametime > datelibrary[profiles[key]["factorlimit"]]):
                return profiles[key]["factor"]
            else:
                return "???"
        else:
            for t in profiles[key][stat]:
                if gametime > datelibrary[t[0]]:
                    return str(t[1])
        return ""

    def getDescription(key):
        d = ""
        for desc in profiles[key]["desc"]:
            useDesc = True
            for flag in desc[0]:
                if getFlag(flag[0]) != flag[1]:
                    useDesc = False
                    break
            if useDesc:
                d += desc[1] + " "
        return d

    def getProfileString(key):
        if profiles[key]["pimgdates"] == None:
            return "Graphics/ui/profiles/" + key + "-pimg.webp"
        else:
            i = len(profiles[key]["pimgdates"])
            for d in profiles[key]["pimgdates"]:
                if gametime > datelibrary[d]:
                    return "Graphics/ui/profiles/" + key + "-pimg-" + str(i) + ".webp"
                i -= 1

label profileselect:
    scene black
    $activepage = "main"
    window hide None
    call screen profileselect
    window show None

screen profileselect():
    grid 2 7:
        for pk in profilepages[activepage]:
            if pk == None:
                text ""
            else:
                $pv = profiles[pk]
                button action [SetVariable("activeprofile", pk), Jump("profileview")]:
                    hbox:
                        image "Graphics/ui/profiles/" + pk + "-picon.webp"
                        text pv["name"] yalign .5
                        if pv["affection"] != None:
                            image "Graphics/ui/profiles/heartsmall.webp"

    hbox:
        yalign .9
        textbutton "Main" action[SetVariable("activepage", "main")]
        textbutton "Minor" action[SetVariable("activepage", "minor")]

    textbutton "Back" action Jump("daymenu_noadvance") yalign .95

label profileview:
    scene black
    window hide None
    call screen profileview
    window show None

screen profileview():
    hbox:
        vbox:
            image crop(getProfileString(activeprofile), (50, 0, 300, 400))
            text "Name:" + profiles[activeprofile]["name"]
            text "DOB: " + profiles[activeprofile]["DOB"]
            hbox:
                spacing 16
                text "Height:" + getProfileStat(activeprofile, "height") + " cm"
                text "Weight:" + getProfileStat(activeprofile, "weight") + " kg"
            text "Factor: " + getProfileStat(activeprofile, "factor")
            if not profiles[activeprofile]["sex"]:
                text "BWH: " + getProfileStat(activeprofile, "BWH")
        text getDescription(activeprofile)

    textbutton "Back" action Jump("profileselect") yalign .95
