import math

"""
    Die Zahlen der Berechnung entsprechen denen der offiziellen Mehrkampfberechnungen (oder orientieren sich daran)
"""


"""
    Berechne Punktzahl des Schlagwurf

    :param leistung: Leistung in Metern
    :return: abgerundete Punktzahl
"""
def calculateSchlagwurf(leistung):
    c = 1.08
    a = 10.14
    float(leistung)

    return math.floor((leistung**c) * a)

"""
    Berechne Punktzahl des Drehwurf

    :param leistung: Leistung in Metern
    :return: abgerundete Punktzahl 
"""
def calculateDrehwurf(leistung):
    c = 1.10
    a = 12.91
    float(leistung)

    return math.floor((leistung**c) * a)

"""
    Berechne Punktzahl des Fünfsprungs

    :param leistung: Leistung in Zentimetern
    :return: abgerundete Punktzahl 
"""
def calculateFuenfSprung(leistung):
    c = 1.40
    a = 0.14354
    float(leistung)

    return math.floor((leistung**c) * a)

"""
    Berechne Punktzahl des Stadioncross

    :param leistung: Leistung in Sekunden
    :return: abgerundete Punktzahl 
"""
def calculateStadioncross(leistung):
    a = 100
    b = 300  # Basiswert für die Berechnung
    c = 1.85
    float(leistung)

    return math.floor((a * (b / leistung) ** c) * 0.8) # Balancing 80% during competition

"""2.Wettkampf TS Jahn"""

# TODO: Separate formulas for age groups due to differences in race length

"""
    Berechne Punktzahl des Hindernissprints
    
    :param leistung: Leistung in Sekunden, Zehntel Hundertstel (2 Nachkommastellen)
    :return: abgerundet e Punktzahl
"""
def calculateHindernissprintU12(leistung):
    a = 20.5173
    c = 1.92
    float(leistung)

    return math.floor(a * (leistung**c))

leistungS = float(input("Leistung: "))
print(calculateHindernissprintU12(leistungS))