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

# Separate formulas for age groups due to differences in race length
"""
    Berechne Punktzahl des Hindernissprints
    
    :param leistung: Leistung in Sekunden, Zehntel Hundertstel (2 Nachkommastellen)
    :return: abgerundete Punktzahl
"""
def calculateHindernissprintU12(leistung):
    a = 20.5173
    b = 16.9 # Basis 0 Wert (18)
    c = 1.64 # 1.74
    float(leistung)

    return math.floor(a * ((b - leistung)**c))

def calculateHindernissprintU10(leistung):
    a = 20.5173
    b = 16
    c = 1.65 # 1.74 / 1.69
    float(leistung)

    return math.floor(a * ((b - leistung)**c))

def calculateHindernissprintU8(leistung):
    a = 20.5173
    b = 14
    c = 1.63
    float(leistung)

    return math.floor(a * ((b - leistung)**c))
"""
    Berechne Punktzahl des Stabweitsprungs
    
    :param leistung: Leistung i n Punkten (1p == 25cm)
    :return: abgerundete Punktzahl
"""
def calculateStabweitsprung(leistung):
    float(leistung)

    return math.floor(leistung*18.5)

"""
    Berechne Punktzahl des Stoßens
    
    :param leistung: Leistung in Metern
    :return: abgerundete Punktzahl
"""
def calculateStoss(leistung):
    a = 51.39
    c = 1.05
    float(leistung)

    return math.floor((leistung**c) * a)

"""
    Berechne Punktzahl der Biathlonstaffel
    
    :param leistung: Leistung des Teams in Sekunden
    :return: abgerundete Punktzahl
"""
def calculateBiathlonstaffel(leistung):
    return math.floor(leistung*0.75) # Change factor depending on times

"""3. Wettkampf Ost"""

"""
    Values for a, b, and c are women's 60m
"""
def calculateSprintU12(leistung): # 50m
   a = 40.0849 # original 46.0849 for ~ [444, 1100]
   b = 13
   c = 1.81
   return math.floor(a*(b - leistung)**c)

def calculateSprintU10(leistung):  # 40m
    a = 38.5
    b = 13.0
    c = 1.81
    return math.floor(a * (b - leistung)**c)

def calculateSprintU8(leistung):   # 30m
    a = 34.0
    b = 12.5
    c = 1.81
    return math.floor(a * (b - leistung)**c)

def calculateHighJumpU8U10(leistung):  # Shared formula for U8 & U10
    a = 2.12
    b = 24
    c = 1.35
    return math.floor(a * (leistung - b)**c)

def calculateHighJumpU12(leistung):
    a = 1.70
    b = 30
    c = 1.4
    return math.floor(a * (leistung - b) ** c)
