import random
cht=["is Absentminded", "is Arrogant", "is Boorish", "Chews something", "is Clumsy", "is Curious", "is Dim-witted", "Fiddles and fidgets nervously", "Frequently uses the wrong word", "is Friendly", "is Irritable", "is Prone to predictions of certain doom", "has a Pronounced scar", "Slurs words, lisps or stutters", "Speaks loudly or whispers", "Squints", "Stares into distance", "is Suspicious", "Uses colorful oaths and exclamations", "Uses flowerly speech or long words"]
idl=["Aspiration", "Charity", "Community", "Creativity", "Discovery", "Fairness", "Freedom", "Glory", "Greater Good", "Greed", "Honor", "Independence", "Knowledge", "Life", "Live and let live", "Might", "Nation", "People", "Power", "Redemption"]
bnd=["Personal goals", "Family", "Colleagues", "Patron or Employer", "Romantic interest", "Special place", "Keepsake", "Valuable possession", "Revenge"]
flw=["Forbidden love", "Decadence", "Arrogance", "Envy", "Greed", "Quickness to rage", "Powerful enemy", "Specific phobia", "Shameful or scandalous history", "Secret crime or misdeed", "Posession of forbidden lore", "Foolhardy bravery"]
mn=["Adrik","Alberich","Baern","Barendd","Brottor","Bruenor","Oain","Oarrak","Oelg","Eberk","Einkil","Fargrim","Flint","Gardain","Harbek","Kildrak","Morgran","Orsik",
"Oskar","Rangrim","Rurik","Taklinn","Thoradin","Thorin","Tordek","Traubon","Travok","Ulfgar","Veit","Vondal","Adran","Aelar","Aramil","Arannis","Aust","Beizro","Berrian",
"Carrie","Enialis","Erdan","Erevan","Galinndan","Hadarai","Heian","Himo","Immeral","Ivellios","Laucian","Mindartis","Paelias","Peren","Quarion","Riardon","Rolen",
"Soveliss","Thamior","Tharivol","Theren","Varis","Ara","Bryn","Del","Eryn","Faen","Innil","Lael","Mella","Naill","Naeris","Phann","Rael","Rinn","Sai","Syllin","Thia",
"Vali","Alton","Ander","Cade","Corrin","Eldon","Errich","Finnan","Garret","Lindal","Lyle","Merric","Milo","Osborn","Perrin","Reed","Roscoe","Wellby","Arjhan","Balasar",
"Bharash","Donaar","Ghesh","Heskan","Kriv","Medrash","Mehen","Nadarr","Pandjed","Patrin","Rhogar","Shamash","Shedinn","Tarhun","Torinn","Alston","Alvyn","Boddynock",
"Brocc","Burgell","Dimble","Eldon","Erky","Fonkin","Frug","Gerbo","Gimble","Glim","Jebeddo","Kellen","Namfoodle","Orryn","Roondar","Seebo","Sindri","Warryn","Wrenn",
"Zook","Deneh","Feng","Gell","Henk","Holg","Imsh","Kelh","Krusk","Mhurren","Ront","Shump","Thokk","Akmenos","Amnon","Barakas","Damakos","Ekemon","lados","Kairon",
"Leucis","Melech","Mordai","Morthos","Pelaios","Skamos","Therai"]
fn=["Amber","Artin","Audhild","Bardryn","Oagnal","Oiesa","Eldeth","Falkrunn","Finellen","Gunnloda","Gurdis","Helja","Hlin","Kathra","Kristryd","lide","Liftrasa",
"Mardred","Riswynn","Sannl","Torbera","Torgga","Vistra","Ara","Bryn","Del","Eryn","Faen","Innil","Lael","Mella","Naill","Naeris","Phann","Rael","Rinn","Sai","Syllin",
"Thia","Vali","Adrie","Althaea","Anastrianna","Andraste","Antinua","Bethrynna","Birel","Caelynn","Orusilia","Enna","Felosial","lelenia","jelenneth","Keyleth","Leshanna",
"Lia","Meriele","Mialee","Naivara","Quelenna","Quillathe","Sariel","Shanairra","Shava","Silaqui","Theirastra","Thia","Vadania","Valanthe","Xanaphia","Andry","Bree",
"Callie","Cora","Euphemia","jillian","Kithri","Lavinia","Lidda","Merla","Nedda","Paela","Portia","Seraphina","Shaena","Trym","Vani","Verna","Akra","Biri","Daar",
"Farideh","Harann","HaviJar","Jheri","Kava","Korinn","Mishann","NaJa","Perra","Raiann","Sora","Surina","Thava","Uadjit","Bimpnollin","Breena","Caramip","Carlin",
"Donella","Duvamil","ElIa","ElIyjobell","ElIywick","Lilli","Loopmottin","Lorilla","Mardnab","Nissa","Nyx","Oda","Orla","Roywyn","Shamil","Tana","Waywocket","Zanna",
"Baggi","Emen","Engong","Kansif","Myev","Neega","Ovak","Ownka","Shaulha","Sulha","Vola","Volen","Yevelda","Akta","Anakis","Bryseis","Criella","Damaia","Ea","Kallista",
"Lerissa","Makaria","Nemeia","Orianna","Phelaia","Rieta"]
ln=["Balderk","Battlehammer","Brawnanvil","Oankil","Fireforge","Frostbeard","Gorunn","Holderhek","Ironfist","Loderr","Lutgehr","Rumnaheim","Strakeln","Torunn","Ungart",
"Amakiir","Amastacia","Galanodel","Holimion","Ilphelkiir","Liadon","Meliamne","Nailo","Siannodel","Xiloscient","Brushgather","Goodbarrel","Greenbottle","Highhill",
"Hilltopple","Leagallow","Tealeaf","Thorngage","Tosscobble","Underbough","Clethtinthiallor","Daardendrian","Delmirev","Drachedandion","Fenkenkabradon","Kepeshkmolik",
"Kerrhylon","Kimbatuul","Linxakasendalor","Myastan","Nemmonis","Norixius","Ophinshtalajiir","Prexijandilin","Shestendeliath","Turnuroth","Verthisathurgiesh","Yarjerit",
"Beren","Daergel","Folkor","Garrick","Nackle","Murnig","Ningel","Raulnor","Scheppen","Timbers","Turen","Aleslosh","Ashhearlh","Badger","Cloak","Doublelock","Filchbatler",
"Fnipper","Ku","Nim","Oneshoe","Pock","Sparklegem","Stumbleduck"]
rac=["Dwarf","Elf","Halfling","Human","Dragonborn","Gnome","Half-Elf","Half-Orc","Tiefling","Aarakocra","Genasi","Goliath","Aasimar","Bugbear","Firbolg","goblin", "hobgoblin","kenku","kobold","lizardfolk","orc","tabaxi","triton","Yuan-ti Pureblood", "Tortle", "Gith","Changeling","Kalashtar","Shifter","Warforged","Centaur", "Loxodon","minotaur","Simic hybrid","Vedalken","Grung","Dwarf","Elf","Halfling","Human","Gnome","Aarakocra","Genasi","Goliath","Bugbear","Firbolg","goblin", "hobgoblin","kenku","kobold","lizardfolk","orc","tabaxi","Yuan-ti Pureblood", "Tortle", "Gith","Centaur", "Loxodon","minotaur","Vedalken","Grung","Dwarf","Elf","Halfling","Human","Gnome","Aarakocra","Genasi","Goliath","Bugbear","Firbolg","goblin", "hobgoblin","kenku","kobold","lizardfolk","orc","tabaxi","Yuan-ti Pureblood", "Tortle", "Gith","Centaur", "Loxodon","minotaur","Vedalken","Grung","Dwarf","Elf","Halfling","Human","Gnome","Aarakocra","Genasi","Goliath","Bugbear","Firbolg","goblin", "hobgoblin","kenku","kobold","lizardfolk","orc","tabaxi","Yuan-ti Pureblood", "Tortle", "Gith","Centaur", "Loxodon","minotaur","Vedalken","Grung"]
cls=["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
bgd=["Acolyte","Charlatan","Criminal","Entertainer","Folk Hero","Guild Artisen","Hermit","Noble","Outlander","Sage","Sailor","Soldier","Urchin"]

def generator():
    global cht
    global idl
    global bnd
    global flw
    global mn
    global fn
    global ln
    global cls
    global rac
    global bgd
    character=cht[random.randint(0,len(cht)-1)]
    ideal=idl[random.randint(0,len(idl)-1)]
    bond=bnd[random.randint(0,len(bnd)-1)]
    flaw=flw[random.randint(0,len(flw)-1)]
    male=mn[random.randint(0,len(mn)-1)]
    female=fn[random.randint(0,len(fn)-1)]
    last=ln[random.randint(0,len(ln)-1)]
    job=cls[random.randint(0,len(cls)-1)]
    race=rac[random.randint(0,len(rac)-1)]
    background=bgd[random.randint(0,len(bgd)-1)]
    if(random.randint(0,1)==0):
        print (female, last, "is a ", race, job, background, "\nShe", character, "\nShe idealizes", ideal, "\nShe is bonded with her", bond, "\nShe is flawed in her", flaw)
    else:
        print (male, last, "is a ", race, job, background, "\nHe", character, "\nHe idealizes", ideal, "\nHe is bonded with his", bond, "\nHe is flawed in his", flaw)

generator()


