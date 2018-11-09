import textdistance
from unidecode import unidecode

def porownaj_tekst(a, b, threshold=0.78     ):
    a = unidecode(a.lower()) # cast diacrytical to ascii characters
    b = unidecode(b.lower())
    similarity = textdistance.levenshtein.normalized_similarity(a, b)
    return True if similarity > threshold else False

