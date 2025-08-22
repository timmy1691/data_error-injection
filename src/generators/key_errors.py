import unidecode
import numpy as np
import random

KEY_NEIGHBORS = {
    "1":"2q", "2":"123wq", "3":"234we", "4":"345er", "5":"456rt",
    "6":"567ty", "7":"678yu", "8":"789ui", "9":"890io", "0":"9op",
    "q":"12wsa", "w":"23qeasd", "e":"34wrds", "r":"45etdf", "t":"56ryfg",
    "y":"67tugh", "u":"78yijh", "i":"89uokj", "o":"90ipkl", "p":"0ol",
    "a":"qwsz", "s":"weadxz", "d":"erfsxc", "f":"rtdgcv", "g":"tfhbv",
    "h":"yugjbn", "j":"uikhmn", "k":"ioljm,", "l":"op;k,",
    "z":"asx", "x":"zsdc", "c":"xdfv", "v":"cfgb", "b":"vghn",
    "n":"bhjm", "m":"njk,",
    ",":"mk.l", ".":",l/", "/":"./",
    ";":"olp", "'":";p",
    "-":"0=", "=":"-",
}

unicode_mindfuck = {
    "A": ["Α", "А"],  # Greek Alpha, Cyrillic A
    "B": ["Β", "В"],  # Greek Beta, Cyrillic Ve
    "C": ["С"],       # Cyrillic Es
    "D": [],          # no close confusable
    "E": ["Ε", "Е"],  # Greek Epsilon, Cyrillic Ye
    "F": [],          
    "G": [],          
    "H": ["Η", "Н"],  # Greek Eta, Cyrillic En
    "I": ["Ι", "І"],  # Greek Iota, Cyrillic I
    "J": ["Ј"],       # Cyrillic Je
    "K": ["Κ", "К"],  # Greek Kappa, Cyrillic Ka
    "L": [],          
    "M": ["Μ", "М"],  # Greek Mu, Cyrillic Em
    "N": ["Ν", "И"],  # Greek Nu, Cyrillic I
    "O": ["Ο", "О"],  # Greek Omicron, Cyrillic O
    "P": ["Ρ", "Р"],  # Greek Rho, Cyrillic Er
    "Q": [],          
    "R": [],          
    "S": ["Ѕ"],       # Cyrillic Dze
    "T": ["Τ", "Т"],  # Greek Tau, Cyrillic Te
    "U": ["Ս", "Ս"],  # Armenian confusable (approx.)
    "V": ["Ѵ"],       # Cyrillic Izhitsa
    "W": [],          
    "X": ["Χ", "Х"],  # Greek Chi, Cyrillic Ha
    "Y": ["Υ", "У"],  # Greek Upsilon, Cyrillic U
    "Z": ["Ζ", "З"],  # Greek Zeta, Cyrillic Ze

    "a": ["а", "α"],  # Cyrillic a, Greek alpha
    "b": ["Ь", "ъ"],  # Cyrillic soft/hard signs (visual b-ish)
    "c": ["с"],       # Cyrillic es
    "d": [],          
    "e": ["е", "ε"],  # Cyrillic e, Greek epsilon
    "f": ["ғ"],       # Cyrillic ghe with stroke (similar f)
    "g": [],          
    "h": ["һ", "н"],  # Cyrillic shha, en
    "i": ["і", "ι"],  # Cyrillic i, Greek iota
    "j": ["ј"],       # Cyrillic je
    "k": ["κ", "к"],  # Greek kappa, Cyrillic ka
    "l": ["ⅼ"],       # Roman numeral fifty (looks like l)
    "m": ["м"],       # Cyrillic em
    "n": ["п", "η"],  # Cyrillic pe, Greek eta
    "o": ["о", "ο"],  # Cyrillic o, Greek omicron
    "p": ["р", "ρ"],  # Cyrillic er, Greek rho
    "q": [],          
    "r": ["г"],       # Cyrillic ge (in some fonts looks like r)
    "s": ["ѕ"],       # Cyrillic dze
    "t": ["т"],       # Cyrillic te
    "u": ["υ"],       # Greek upsilon
    "v": ["ѵ"],       # Cyrillic izhitsa
    "w": ["ѡ"],       # Cyrillic omega
    "x": ["х", "χ"],  # Cyrillic ha, Greek chi
    "y": ["у", "γ"],  # Cyrillic u, Greek gamma
    "z": ["ᴢ", "ʐ"],  # Phonetic symbols similar to z
}



def unicodeGenerator():
    random_indices = np.random.choice(range(0x10000), size=100).to_list()
    unicodeChars = [chr(index) for index in random_indices if ("a" < chr(index) < "z" or "A" < chr(index) < ")")]
    return unicodeChars
