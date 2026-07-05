import csv
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "version2"
OUT = ROOT / "output" / "pdf" / "norveg_magyar_nyomtathato_terv.pdf"
FONT_DIR = Path(
    r"C:\Users\varga\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\share\fonts"
)

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 1.25 * cm
MARGIN_Y = 1.2 * cm
ACCENT = colors.HexColor("#1E7D73")
DARK = colors.HexColor("#24343D")
MID = colors.HexColor("#68777D")
LIGHT = colors.HexColor("#EEF5F3")
LINE = colors.HexColor("#CBD7D5")
WARN = colors.HexColor("#8A5A00")


pdfmetrics.registerFont(TTFont("Guide", str(FONT_DIR / "Ubuntu-R.ttf")))
pdfmetrics.registerFont(TTFont("Guide-Bold", str(FONT_DIR / "Ubuntu-B.ttf")))


DESCRIPTIONS = {
    "Bergen Airport": (
        "Bergen repülőtere, a túra autós kezdő- és zárópontja.",
        "Számolj időt az autófelvételre, csomagokra, első bevásárlásra és a végén a töltöttségi elvárásra.",
    ),
    "Bergen": (
        "Nyugat-Norvégia kapuja, esős, hangulatos kikötőváros hegyekkel és régi faházas részekkel.",
        "Ha marad energiátok, rövid esti séta és vacsora elég; a hosszú út másnap kezdődik.",
    ),
    "Wergeland Cozy Apartment": (
        "Első éjszakai szállás Bergenben, jó pihenőpont az érkezés után.",
        "Érkezéskor jegyezd fel a parkolást és készíts képernyőképet a bejutási információkról.",
    ),
    "Voss": (
        "Praktikus hegyi-völgyi megálló Bergen és a fjordvidék között, szolgáltatásokkal és töltési lehetőséggel.",
        "Kávé, mosdó, gyors bevásárlás vagy EV-töltés miatt érdemes betervezni.",
    ),
    "Tvindefossen": (
        "Könnyen elérhető vízesés az út mellett, jó rövid fotómegálló.",
        "Ne nyújtsátok hosszúra, ha a Laerdalsoyri felé tartó nap késésben van.",
    ),
    "Gudvangen": (
        "Fjordparti település a Naeroyfjord környékén, látványos, de nyáron forgalmas.",
        "Rövid panorámaszünetnek jó, hosszabb programra csak akkor, ha bőven van idő.",
    ),
    "Aurland": (
        "Csendesebb fjordbázis Flam közelében, jó kiindulópont Aurlandsfjordhoz és Stegasteinhez.",
        "Tartsátok rugalmasan: séta, fotó, étkezés vagy töltés is beleférhet.",
    ),
    "Otthon, Laerdalsoyri": (
        "Két éjszakás bázis Laerdalsoyriben, innen kényelmesen bejárható Aurland, Flam és Stegastein.",
        "Önellátó szállásnál előre legyen bevásárlás; a kulcsszéf adatait mentsétek offline.",
    ),
    "Stegastein Viewpoint": (
        "Magasan az Aurlandsfjord felett futó kilátó, a környék egyik legerősebb panorámája.",
        "Menjetek korán vagy későn, mert júliusban a parkolás és a tömeg könnyen időt visz el.",
    ),
    "Aurlandsfjord": (
        "Mélykék fjordág meredek hegyoldalakkal, Aurland és Flam környékének fő látványa.",
        "A legjobb élmény gyakran egy nyugodt parti séta vagy kilátópont, nem a túlzsúfolt program.",
    ),
    "Flam": (
        "Népszerű fjordfalu, hajók, szolgáltatások, étkezési és programlehetőségek központja.",
        "Számíts turistaforgalomra; ha zsúfolt, kezeld praktikus megállóként, ne egész napos célként.",
    ),
    "Undredal": (
        "Kis fjordfalu csendesebb hangulattal, jó opcionális kitérő.",
        "Akkor válaszd, ha nem siettek és nem vállaltatok be már fjordhajózást vagy hosszabb programot.",
    ),
    "Laerdal": (
        "A Sognefjord térségének praktikus átmeneti pontja, innen indul a Stryn felé vezető transzfer.",
        "Indulás előtt legyen tiszta a komp- és töltési terv.",
    ),
    "Fodnes Ferry": (
        "Kompátkelés a Laerdalsoyri - Sogndal - Stryn útvonalon.",
        "A várakozást kalkuláld bele; ne az utolsó percre időzíts fontos programot utána.",
    ),
    "Fodnes-Mannheller Ferry": (
        "Rövid, hasznos komp a Sognefjord térségében, Stryn felé menet.",
        "Menetrendet indulás reggelén ellenőrizz, főleg ha sok megállót terveztek.",
    ),
    "Sogndal": (
        "Jó szolgáltatási és töltési bázis a hosszabb transzfernapokon.",
        "Ebéd, bevásárlás és fő EV-töltés szempontból az egyik legpraktikusabb megálló.",
    ),
    "Boyabreen": (
        "Könnyen elérhető gleccsernéző pont Fjaerland környékén.",
        "Rövid, látványos megálló; ne csináljatok belőle hosszú túrát a transzfernapon.",
    ),
    "Boyabreen Glacier Viewpoint": (
        "Könnyen elérhető gleccsernéző pont Fjaerland környékén.",
        "Rövid, látványos megálló; ne csináljatok belőle hosszú túrát a transzfernapon.",
    ),
    "Loen": (
        "Látványos fjord- és hegyvidéki település Stryn közelében.",
        "Jó időben erős panorámapontok vannak a környéken, rossz időben inkább alacsonyabb útvonalat válasszatok.",
    ),
    "Lodgen Stryn": (
        "Három éjszakás Stryn környéki bázis, a Lovatnet, Briksdal és Geiranger-opció kiindulópontja.",
        "A reggelit és parkolást használjátok ki; hosszú nap előtt töltsetek és pakoljatok időben.",
    ),
    "Lovatnet": (
        "Türkiz tó meredek hegyek között, az egyik legszebb, mégis alacsony stresszű program.",
        "Ideális pihenősebb napra. Esőben is hangulatos, de óvatosan vezessetek a keskenyebb részeken.",
    ),
    "Briksdal Glacier": (
        "Rövid túrával elérhető gleccserkörnyék, klasszikus Nordfjord-program.",
        "Akkor legyen a nap fő aktív programja, ha az időjárás és az energiaszint is jó.",
    ),
    "Loen Skylift": (
        "Felvonó magas panorámára Loen felett.",
        "Csak tiszta időben éri meg igazán; felhőben inkább Lovatnet vagy alacsonyabb scenic drive.",
    ),
    "Olden": (
        "Fjordparti település Loen és Briksdal közelében, jó rövid átmeneti megálló.",
        "Étkezésre vagy rövid sétára jó, de ne vigye el a gleccseres nap fókuszát.",
    ),
    "Stryn": (
        "Praktikus bázis település a Nordfjord környékén, szolgáltatásokkal.",
        "Tankolás/töltés, bolt és időjárás-újratervezés miatt hasznos.",
    ),
    "Djupvatnet": (
        "Magashegyi tó Geiranger felé, gyors és látványos időjárásfüggő megálló.",
        "Ha ködös vagy nagyon hideg-szeles, elég pár fotó, majd tovább.",
    ),
    "Dalsnibba": (
        "Magashegyi, fizetős kilátóút Geiranger felett, tiszta időben nagyon erős panorámával.",
        "Ködben, alacsony felhőben vagy szoros időterv mellett hagyjátok ki.",
    ),
    "Flydalsjuvet": (
        "Klasszikus Geiranger-kilátópont, rövid megállóval nagy látvánnyal.",
        "Jó fotópont, de parkolásra és buszokra számítsatok júliusban.",
    ),
    "Geiranger": (
        "Ikonikus fjordfalu, nagyon látványos, de főszezonban zsúfolt.",
        "Legyen rövid falumegálló; a fő érték a kilátópontok és a Geiranger - Hellesylt komp.",
    ),
    "Geiranger Ferry Pier": (
        "A Geiranger - Hellesylt fjordkomp indulási pontja.",
        "Júliusban érdemes előre foglalni, és legalább 30 perccel indulás előtt ott lenni.",
    ),
    "Geiranger-Hellesylt Ferry": (
        "Kb. 65 perces fjordkomp, önmagában is látványprogram.",
        "A járműves helyet ellenőrizzétek előre; rossz időben is szép, de késésre legyen tartalék.",
    ),
    "Geiranger-Hellesylt Ferry Start": (
        "A Geiranger - Hellesylt fjordkomp indulási pontja.",
        "Júliusban érdemes előre foglalni, és legalább 30 perccel indulás előtt ott lenni.",
    ),
    "Hellesylt Ferry Pier": (
        "A Geiranger-komp érkezési oldala, innen Stryn felé lehet visszafordulni.",
        "Érkezés után ne tervezzetek túl sok plusz megállót, ez már hosszú nap.",
    ),
    "Hellesylt Ferry Arrival": (
        "A Geiranger-komp érkezési oldala, innen Stryn felé lehet visszafordulni.",
        "Érkezés után ne tervezzetek túl sok plusz megállót, ez már hosszú nap.",
    ),
    "Skei": (
        "Hasznos pihenő- és töltési pont Stryn és Sogndal között.",
        "Jó hely rövid szünetre, mielőtt a hosszú visszaút sűrűbb részei jönnek.",
    ),
    "Hella Ferry Pier": (
        "A Hella - Vangsnes komp indulási oldala a scenic Vikafjell visszaúton.",
        "A komp miatt a nap tempója kevésbé kiszámítható; legyen víz, snack és töltött telefon.",
    ),
    "Hella-Vangsnes Ferry": (
        "Rövid kompátkelés, amely változatosabbá teszi a visszautat Vik és Vikafjell felé.",
        "Csak akkor válasszátok, ha az időjárás és az útviszonyok jók a hegyi szakaszhoz.",
    ),
    "Vangsnes Ferry Pier": (
        "A Hella - Vangsnes komp érkezési oldala, innen Vik felé vezet az út.",
        "Érkezés után ellenőrizzétek újra a Vikafjell időjárását, ha bizonytalan.",
    ),
    "Vangsnes Ferry Arrival": (
        "A Hella - Vangsnes komp érkezési oldala, innen Vik felé vezet az út.",
        "Érkezés után ellenőrizzétek újra a Vikafjell időjárását, ha bizonytalan.",
    ),
    "Vik i Sogn": (
        "Kis település a scenic visszaúton, rövid pihenőre alkalmas.",
        "Tartsátok röviden, mert a nap vége Vaksdalig még hosszú.",
    ),
    "Vikafjellsvegen (Rv13) / Vikafjellet": (
        "Látványos hegyi útvonal Vik és Voss között, jó időben emlékezetes.",
        "Rossz látási viszonyoknál, erős esőnél vagy fáradtságnál váltsatok az E39 backup útvonalra.",
    ),
    "Hopperstad Stave Church": (
        "Történelmi fatemplom Vik környékén, opcionális kulturális megálló.",
        "Csak akkor férjen bele, ha a visszaút nincs késésben.",
    ),
    "Otthon, Vaksdal kommune": (
        "Utolsó éjszakai szállás Bergen közelében, kényelmesebb repülőtéri visszatéréshez.",
        "Este készítsétek elő a csomagokat és az autó leadási/töltési tervét.",
    ),
    "Forde": (
        "Praktikus szolgáltatási megálló az E39 backup útvonalon.",
        "Használjátok töltésre vagy ebédre, ha a Vikafjell helyett biztonságosabb útvonal kell.",
    ),
    "Lavik Ferry Pier": (
        "Az E39 backup útvonal kompindulási pontja Laviknál.",
        "Menetrend és várakozás miatt legyen tartalék a napi tervben.",
    ),
    "Lavik-Oppedal Ferry": (
        "Backup komp az E39-es, kevésbé hegyi visszaúton.",
        "Jó választás, ha a scenic hegyi út rossz időben kockázatos lenne.",
    ),
    "Oppedal Ferry Pier": (
        "Az E39 backup komp érkezési oldala Bergen/Vaksdal felé.",
        "Innen még számoljatok vezetéssel; ne hagyjátok túl későre a nap végét.",
    ),
    "Oppedal Ferry Arrival": (
        "Az E39 backup komp érkezési oldala Bergen/Vaksdal felé.",
        "Innen még számoljatok vezetéssel; ne hagyjátok túl későre a nap végét.",
    ),
    "Bergen EV Hub": (
        "Kiinduló töltési pont Bergenben.",
        "Hosszabb út előtt induljatok magas töltöttséggel.",
    ),
    "Voss EV Hub": (
        "Két irányban is hasznos töltő- és szolgáltatási pont.",
        "Ha bizonytalan a hatótáv, itt érdemes rátölteni.",
    ),
    "Aurland EV Hub": (
        "Helyi töltési lehetőség Aurland környékén.",
        "Ne erre legyen az egyetlen terv, ellenőrizzétek a foglaltságot.",
    ),
    "Flam EV Hub": (
        "Turistás térség töltőkkel és szolgáltatásokkal.",
        "Főszezonban zsúfolt lehet, legyen alternatíva.",
    ),
    "Sogndal EV Hub": (
        "Az egyik legjobb fő töltési pont transzfernapokra.",
        "Ebéd és bolt mellé jól időzíthető.",
    ),
    "Skei EV Hub": (
        "Hasznos tartalék töltési és pihenőpont.",
        "A Stryn - Sogndal szakaszon adhat biztonsági tartalékot.",
    ),
    "Stryn EV Hub": (
        "Praktikus töltőbázis a Nordfjord/Geiranger napokhoz.",
        "Hosszú Geiranger-nap előtt különösen fontos.",
    ),
    "Loen EV Hub": (
        "Helyi töltési lehetőség Loen környékén.",
        "Ne számítsatok egyetlen töltőre; legyen Stryn alternatíva.",
    ),
    "Geiranger EV Hub": (
        "Kis falusi/turisztikai töltési lehetőség.",
        "Backupként kezeld, ne fő töltési tervként.",
    ),
    "Vik EV Hub": (
        "Tartalék töltési pont a scenic visszaúton.",
        "A fő töltést inkább Sogndalban vagy Vossban tervezzétek.",
    ),
    "Bergen Airport EV Hub": (
        "Repülőtéri töltési lehetőség autóleadás előtt.",
        "Ellenőrizd a bérlés feltételeit: milyen töltöttséggel kell visszaadni az autót.",
    ),
}


ACCOMMODATION_DETAILS = {
    "Wergeland Cozy Apartment": "Booking.com: 6303.112.352, PIN 5555. Július 6-7, 1 éj. Check-in 15:00-23:00, check-out 07:00-11:00. 3 felnőtt, ingyenes privát parkoló és Wi-Fi, étkezés nélkül.",
    "Otthon, Laerdalsoyri": "Airbnb: HMA9TY5QWC, host: Aleksander. Július 7-9, 2 éj. Kulcsszéfes önálló check-in, 3 vendég, max. 4 fő, kisállat engedélyezett. Check-out július 9. 11:00.",
    "Lodgen Stryn": "Booking.com: 6091.836.791, PIN 9761. Július 9-12, 3 éj. Check-in 15:00-23:00, check-out 07:00-11:00. Reggeli benne van, privát parkoló és Wi-Fi.",
    "Otthon, Vaksdal kommune": "Airbnb: HMBHADWXQB, host: Truls. Július 12-13, 1 éj. Kulcsszéfes önálló check-in, 3 vendég, kisállat engedélyezett. Check-out július 13. 11:00.",
}


DAY_TIPS = {
    "Day 1": [
        "Fő cél: megérkezés, autófelvétel, pihenés.",
        "Ne tervezzetek nagy városnézést, ha késik a gép vagy lassú az autóátvétel.",
    ],
    "Day 2": [
        "Ez az első hosszabb vezetési nap. A Voss - Gudvangen - Aurland szakaszon legyen rugalmas megállóterv.",
        "Ha az idő csúszik, Tvindefossen és Gudvangen opcionális.",
    ],
    "Day 3": [
        "Helyi fjordnap Laerdalsoyriből. Stegastein legyen a nap biztos pontja.",
        "Flam zsúfolt lehet, ezért legyen B-terv: Aurland parti séta vagy Undredal.",
    ],
    "Day 4": [
        "Transzfer Stryn felé. Fodnes komp, Sogndal és Boyabreen adja a nap ritmusát.",
        "A gleccsernéző pont legyen rövid, hogy kényelmesen érjetek Strynbe.",
    ],
    "Day 5": [
        "Pihenősebb scenic nap. Válasszatok egy fő programot: Lovatnet vagy Briksdal.",
        "Loen Skylift csak tiszta időben jó befektetés.",
    ],
    "Day 6": [
        "Geiranger opcionális, de hosszú nap. Csak jó időben és jó energiaszinttel vágjatok bele.",
        "A kompra érkezzetek időben, és ne hagyjátok a töltést Geirangerre.",
    ],
    "Day 7": [
        "Hosszú visszaút Vaksdal felé. Jó időben Vikafjell szép, rossz időben az E39 backup okosabb.",
        "Sogndal vagy Voss legyen fő töltési pont, ne a kisebb tartalékok.",
    ],
    "Day 7 Backup": [
        "Biztonságosabb, kevésbé scenic visszaút rossz idő esetére.",
        "A Lavik - Oppedal komp miatt itt is kell időtartalék.",
    ],
    "Day 8": [
        "Repülőtéri nap. A cél a stresszmentes autóleadás és elegendő puffer.",
        "Indulás előtt ellenőrizzétek a csomagokat, töltöttséget és a check-out időt.",
    ],
}


HUNGARIAN_TITLES = {
    "Bergen Arrival": "Bergeni érkezés",
    "Bergen to Laerdalsoyri": "Bergen - Laerdalsoyri",
    "Laerdalsoyri Local": "Laerdalsoyri környéke",
    "Laerdalsoyri to Stryn": "Laerdalsoyri - Stryn",
    "Stryn Local": "Stryn környéke",
    "Optional Geiranger": "Opcionális Geiranger-nap",
    "Stryn to Vaksdal via Vikafjell": "Stryn - Vaksdal Vikafjellen át",
    "E39 to Vaksdal": "Backup útvonal E39-en Vaksdalba",
    "Vaksdal to Bergen Airport": "Vaksdal - Bergen repülőtér",
}


def read_csv(name):
    with (DATA_DIR / name).open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def clean_layer_title(layer, day):
    title = layer.replace("Route ", "")
    if day and title.startswith(day):
        title = title[len(day):].strip(" -:")
    return HUNGARIAN_TITLES.get(title, title)


def route_files():
    return sorted(DATA_DIR.glob("[0-9][0-9]_Route_*.csv"))


def normalize_stop(name):
    aliases = {
        "Bergen Airport, Flesland, Bergen, Norway": "Bergen Airport",
    }
    return aliases.get(name, name)


def hu_day(day):
    text = (day or "").replace("Day", "Nap").replace("Night", "Éj")
    replacements = [
        ("All", "Mind"),
        ("Optional Geiranger", "opcionális Geiranger"),
        ("Return via Vikafjell", "visszaút Vikafjellen át"),
        ("Backup E39", "E39 backup"),
        ("or", "vagy"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def hu_priority(value):
    replacements = {
        "Must": "Kötelező",
        "Recommended": "Ajánlott",
        "Optional": "Opcionális",
        "Backup": "Tartalék",
        "Backup only": "Csak tartalék",
        "Useful": "Hasznos",
        "Safest": "Legbiztonságosabb",
        "Confirmed": "Visszaigazolt",
        "Weather dependent": "Időjárásfüggő",
        "Must if doing Geiranger": "Kötelező Geiranger esetén",
    }
    return replacements.get(value or "", value or "")


def hu_time(value):
    text = value or ""
    replacements = [
        ("Arrival", "érkezés"),
        ("Start early", "korai indulás"),
        ("Start", "indulás"),
        ("Return", "visszaérkezés"),
        ("Flexible", "rugalmas"),
        ("depending traffic", "forgalomtól függően"),
        ("driving/ferry plus breaks", "vezetés/komp szünetekkel"),
        ("driving plus stops", "vezetés megállókkal"),
        ("driving + 65 min ferry + stops", "vezetés + 65 perc komp + megállók"),
        ("with ferry/charging/stops", "komppal/töltéssel/megállókkal"),
        ("with ferry/charging/stops", "komppal/töltéssel/megállókkal"),
        ("with car return", "autóleadással"),
        ("Short crossing + waiting time", "rövid átkelés + várakozás"),
        ("Short crossing + wait", "rövid átkelés + várakozás"),
        ("After 65 min sailing", "65 perc hajózás után"),
        ("65 min sailing + 30 min check-in", "65 perc hajózás + 30 perc check-in"),
        ("65 min ferry", "65 perc komp"),
        ("Arrive 30 min before ferry", "érkezz 30 perccel korábban"),
        ("Check in 30 min before sailing", "érkezz 30 perccel indulás előtt"),
        ("Continue toward Vik", "tovább Vik felé"),
        ("Continue toward Bergen/Vaksdal", "tovább Bergen/Vaksdal felé"),
        ("Break if needed", "pihenő, ha kell"),
        ("Break/charge if needed", "pihenő/töltés, ha kell"),
        ("Charge/lunch break", "töltés/ebédszünet"),
        ("Coffee, groceries or EV charging.", "kávé, bevásárlás vagy EV-töltés"),
        ("Scenic Rv13 section; weather dependent", "látványos Rv13 szakasz, időjárásfüggő"),
        ("Scenic section on return toward Vaksdal", "látványos szakasz Vaksdal felé"),
        ("from Laerdalsoyri/Aurland area", "Laerdalsoyri/Aurland térségéből"),
        ("Extra detour", "extra kitérő"),
        ("total day", "teljes napi táv"),
        ("local driving", "helyi vezetés"),
        ("return", "oda-vissza"),
        ("incl. detour", "kitérővel"),
        ("stop", "megálló"),
        ("walk/photos", "séta/fotók"),
        ("hours", "óra"),
        ("hr", "óra"),
        ("min", "perc"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def describe(name):
    clean = normalize_stop(name)
    if clean in DESCRIPTIONS:
        return DESCRIPTIONS[clean]
    if clean.endswith(" EV Hub"):
        return (
            "EV-töltési és szolgáltatási pont a tervben.",
            "Indulás előtt ellenőrizd az elérhetőséget és legyen tartalék töltőpont.",
        )
    return (
        "A CSV-tervben szereplő célpont vagy megálló.",
        "Ellenőrizd térképen, időjárásban és napi tempóban, mielőtt fix programként kezeled.",
    )


def para(text, style):
    text = "" if text is None else str(text)
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )
    return Paragraph(escaped, style)


styles = getSampleStyleSheet()
for style in styles.byName.values():
    style.fontName = "Guide"

styles.add(
    ParagraphStyle(
        "CoverTitle",
        parent=styles["Title"],
        fontName="Guide-Bold",
        fontSize=27,
        leading=32,
        textColor=DARK,
        alignment=TA_LEFT,
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        "SubTitle",
        parent=styles["Normal"],
        fontName="Guide",
        fontSize=10.5,
        leading=14,
        textColor=MID,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Guide-Bold",
        fontSize=15.5,
        leading=19,
        textColor=DARK,
        spaceBefore=5,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Guide-Bold",
        fontSize=11,
        leading=14,
        textColor=ACCENT,
        spaceBefore=7,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        "Cell",
        parent=styles["Normal"],
        fontName="Guide",
        fontSize=6.85,
        leading=8.7,
        textColor=DARK,
    )
)
styles.add(
    ParagraphStyle(
        "CellSmall",
        parent=styles["Cell"],
        fontSize=6.35,
        leading=8.0,
    )
)
styles.add(
    ParagraphStyle(
        "CellBold",
        parent=styles["Cell"],
        fontName="Guide-Bold",
    )
)
styles.add(
    ParagraphStyle(
        "Note",
        parent=styles["Normal"],
        fontName="Guide",
        fontSize=8.2,
        leading=11.2,
        textColor=DARK,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        "Footer",
        parent=styles["Normal"],
        fontName="Guide",
        fontSize=7,
        leading=8,
        textColor=MID,
        alignment=TA_CENTER,
    )
)


def draw_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_X, PAGE_HEIGHT - 0.85 * cm, PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 0.85 * cm)
    canvas.setFont("Guide-Bold", 8)
    canvas.setFillColor(ACCENT)
    canvas.drawString(MARGIN_X, PAGE_HEIGHT - 0.62 * cm, "Norvégia - magyar nyomtatható terv")
    canvas.setFont("Guide", 7)
    canvas.setFillColor(MID)
    canvas.drawRightString(PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 0.62 * cm, "CSV terv alapján")
    canvas.setStrokeColor(LINE)
    canvas.line(MARGIN_X, 0.82 * cm, PAGE_WIDTH - MARGIN_X, 0.82 * cm)
    canvas.setFont("Guide", 7)
    canvas.drawCentredString(PAGE_WIDTH / 2, 0.48 * cm, f"{doc.page}. oldal")
    canvas.restoreState()


def draw_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_HEIGHT - 4.0 * cm, PAGE_WIDTH, 4.0 * cm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Guide-Bold", 10)
    canvas.drawString(MARGIN_X, PAGE_HEIGHT - 1.25 * cm, "Bergen - Aurland - Stryn - Geiranger - Vaksdal")
    canvas.setStrokeColor(colors.white)
    canvas.setLineWidth(1)
    canvas.line(MARGIN_X, PAGE_HEIGHT - 3.6 * cm, PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 3.6 * cm)
    canvas.restoreState()


def make_table(headers, rows, widths, small=False):
    cell_style = styles["CellSmall"] if small else styles["Cell"]
    data = [[para(h, styles["CellBold"]) for h in headers]]
    for row in rows:
        data.append([para(value, cell_style) for value in row])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("GRID", (0, 0), (-1, -1), 0.32, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3.8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3.8),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFCFC")]),
            ]
        )
    )
    return table


def callout(title, lines, color=ACCENT):
    data = [[para(title, styles["CellBold"])]]
    data.extend([[para(line, styles["Note"])] for line in lines])
    t = Table(data, colWidths=[PAGE_WIDTH - 2 * MARGIN_X], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.65, color),
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 5.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
            ]
        )
    )
    return t


def notes_block():
    rows = [["Jegyzet", ""]]
    for _ in range(3):
        rows.append(["", ""])
    t = Table(rows, colWidths=[2.0 * cm, PAGE_WIDTH - 2 * MARGIN_X - 2.0 * cm], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("SPAN", (0, 1), (0, -1)),
                ("FONTNAME", (0, 0), (0, 0), "Guide-Bold"),
                ("TEXTCOLOR", (0, 0), (0, 0), MID),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#D8E1DF")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F7FAF9")),
                ("ROWHEIGHT", (0, 1), (-1, -1), 0.68 * cm),
            ]
        )
    )
    return t


def route_snapshot(names):
    unique = []
    for name in names:
        if name not in unique:
            unique.append(name)
    if len(unique) <= 5:
        return " -> ".join(unique)
    return " -> ".join(unique[:2] + ["..."] + unique[-2:])


def build_story():
    accommodations = read_csv("01_Accommodation.csv")
    ferries = read_csv("04_Ferries.csv")
    ev = read_csv("05_EV_Hubs.csv")
    must = read_csv("02_Must_See_Points.csv")
    optional = read_csv("03_Optional_Points.csv")
    routes = []
    for file in route_files():
        rows = read_csv(file.name)
        if rows:
            routes.append((file.name, rows[0]["Layer"], rows[0]["Day"], rows))

    story = [NextPageTemplate("Normal")]
    story.append(Spacer(1, 4.2 * cm))
    story.append(para("Norvégia - magyar nyomtatható útiterv", styles["CoverTitle"]))
    story.append(para("2026. július 6-13. | Bergen, Aurland, Laerdalsoyri, Stryn, Geiranger-opció, Vaksdal, Bergen repülőtér", styles["SubTitle"]))
    story.append(
        callout(
            "Használati tipp",
            [
                "A távolságok és időtartamok tervezési becslések a CSV-kből. Élő navigáció, kompmenetrend, útlezárás, időjárás és EV-töltő státusz indulás előtt mindig ellenőrizendő.",
                "Minden napnál a Must és Recommended pontok legyenek a váz, az Optional pontokat csak jó időben és laza tempó mellett tartsátok meg.",
                "A 7. napnál két terv van: jó időben scenic Vikafjell, rossz időben E39 backup.",
            ],
        )
    )
    story.append(Spacer(1, 0.28 * cm))
    overview_rows = []
    for _, layer, day, rows in routes:
        overview_rows.append(
            [
                hu_day(day),
                clean_layer_title(layer, day),
                route_snapshot([r["Name"] for r in rows]),
                hu_time(rows[-1].get("Approx_Time", "")),
            ]
        )
    story.append(make_table(["Nap", "Terv", "Útvonalváz", "Időtartam / zárás"], overview_rows, [1.7 * cm, 4.2 * cm, 7.6 * cm, 4.2 * cm], small=True))
    story.append(PageBreak())

    story.append(para("Szállások és fontos adatok", styles["H1"]))
    acc_rows = []
    for a in accommodations:
        desc, tip = describe(a["Name"])
        details = ACCOMMODATION_DETAILS.get(a["Name"], "")
        acc_rows.append([hu_day(a["Day"]), a["Name"], a["Address"], hu_time(a["Approx_Time"]), f"{desc} Tipp: {tip} {details}"])
    story.append(make_table(["Éj", "Szállás", "Cím", "Hossz", "Leírás / fontos"], acc_rows, [1.4 * cm, 3.0 * cm, 4.0 * cm, 1.55 * cm, 7.75 * cm], small=True))
    story.append(Spacer(1, 0.25 * cm))
    story.append(
        callout(
            "Szállás elhagyása előtt",
            [
                "Kulcs, útlevél, pénztárca, gyógyszer, töltőkábelek, parkolás, offline bejutási instrukciók.",
                "Hosszú vezetési nap előtt legyen víz, snack, teljes telefon és előre kiválasztott töltőpont.",
            ],
        )
    )
    story.append(PageBreak())

    for _, layer, day, rows in routes:
        title = clean_layer_title(layer, day)
        story.append(KeepTogether([para(f"{hu_day(day)}: {title}", styles["H1"])]))
        first, last = rows[0], rows[-1]
        tips = DAY_TIPS.get(day, [])
        summary = [
            f"Kezdés: {first['Name']} | Érkezés: {last['Name']}",
            f"Napi időkeret: {hu_time(last.get('Approx_Time', ''))}",
        ] + tips
        is_backup = "Backup" in day or "Backup" in layer
        story.append(callout("Napi fókusz", summary, WARN if is_backup else ACCENT))
        story.append(Spacer(1, 0.16 * cm))

        route_rows = []
        for r in rows:
            desc, tip = describe(r["Name"])
            km_time = " / ".join(x for x in [r.get("Approx_Km", ""), r.get("Approx_Time", "")] if x)
            km_time = hu_time(km_time)
            route_rows.append(
                [
                    r["Order"],
                    r["Name"],
                    hu_priority(r["Priority"]),
                    km_time,
                    f"{desc} Tipp: {tip}",
                ]
            )
        story.append(make_table(["#", "Célpont", "Prioritás", "Km / idő", "Rövid leírás és tipp"], route_rows, [0.65 * cm, 3.3 * cm, 2.35 * cm, 2.8 * cm, 8.6 * cm], small=True))
        story.append(Spacer(1, 0.22 * cm))
        story.append(notes_block())
        story.append(PageBreak())

    story.append(para("Kompok és EV-töltés", styles["H1"]))
    story.append(callout("Fontos", ["A komp- és töltőadatok tervezési kapaszkodók. Indulás előtt ellenőrizd az aktuális menetrendet, foglalást, várakozást és töltőfoglaltságot."]))
    story.append(Spacer(1, 0.2 * cm))
    ferry_rows = []
    for f in ferries:
        desc, tip = describe(f["Name"])
        ferry_rows.append([hu_day(f["Day"]), f["Name"], hu_priority(f["Priority"]), hu_time(f["Approx_Time"]), f"{desc} Tipp: {tip}"])
    story.append(make_table(["Nap", "Komp", "Prioritás", "Idő", "Leírás / tipp"], ferry_rows, [2.7 * cm, 3.8 * cm, 2.2 * cm, 2.7 * cm, 6.3 * cm], small=True))
    story.append(Spacer(1, 0.3 * cm))
    ev_rows = []
    for e in ev:
        desc, tip = describe(e["Name"])
        ev_rows.append([hu_day(e["Day"]), e["Name"], hu_priority(e["Priority"]), f"{desc} Tipp: {tip}"])
    story.append(make_table(["Nap", "EV-pont", "Prioritás", "Megjegyzés"], ev_rows, [3.0 * cm, 4.0 * cm, 2.2 * cm, 8.5 * cm], small=True))
    story.append(PageBreak())

    story.append(para("Célpont-kislexikon", styles["H1"]))
    story.append(para("Rövid magyarázat minden kiemelt és opcionális célponthoz.", styles["SubTitle"]))
    seen = set()
    lex_rows = []
    for row in must + optional:
        if row["Name"] in seen:
            continue
        seen.add(row["Name"])
        desc, tip = describe(row["Name"])
        lex_rows.append([hu_day(row["Day"]), row["Name"], hu_priority(row["Priority"]), hu_time(row["Approx_Time"]), f"{desc} Tipp: {tip}"])
    story.append(make_table(["Nap", "Célpont", "Prioritás", "Idő", "Leírás / tipp"], lex_rows, [2.8 * cm, 3.6 * cm, 2.4 * cm, 2.4 * cm, 6.5 * cm], small=True))

    return story


def build_pdf():
    frame = Frame(
        MARGIN_X,
        MARGIN_Y,
        PAGE_WIDTH - 2 * MARGIN_X,
        PAGE_HEIGHT - 2.2 * MARGIN_Y,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
        id="main",
    )
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        rightMargin=MARGIN_X,
        leftMargin=MARGIN_X,
        topMargin=MARGIN_Y,
        bottomMargin=MARGIN_Y,
        title="Norvégia magyar nyomtatható útiterv",
        author="Codex",
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="Cover", frames=[frame], onPage=draw_cover),
            PageTemplate(id="Normal", frames=[frame], onPage=draw_header_footer),
        ]
    )
    doc.build(build_story())


if __name__ == "__main__":
    build_pdf()
    print(OUT)
