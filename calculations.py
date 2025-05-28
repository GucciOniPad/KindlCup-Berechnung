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
    
    :param leistung: Leistung in Punkten (1p == 25cm)
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

"""
TESTING
"""
leistungen_stab = [3, 17, 0, 12, 8, 20, 14, 6, 9, 1, 19, 7, 5, 13, 2, 18, 10, 4, 16, 11]
leistungen_sprint = [8.67, 9.22, 9.26, 9.43, 9.43, 9.82, 9.87, 9.88, 9.93, 9.99, 10.03, 10.07, 10.25, 10.27, 10.35, 10.36, 10.41, 10.68, 11.19, 11.30, 11.77]
leistungen_wurf = [2.3, 3.1, 3.8, 4.0, 4.5, 4.9, 5.2, 5.5, 5.9, 6.2, 6.6, 6.9, 7.1, 7.4, 7.7]

u8_times = [7.0, 7.5, 8.5, 9.0] # [549, 840]
u10_times = [9.3, 9.5, 9.8, 10.0, 10.2, 10.5, 10.7, 10.9, 11.2, 11.5, 11.8, 12.0, 12.3, 12.5, 12.9] # [138, 423]
u12_times = [10.0, 10.2, 10.5, 10.7, 10.9, 11.2, 11.5, 11.8, 12.0, 12.3, 12.5, 12.9]

# print("-- U8 --")
# for i in u8_times:
#     print(calculateHindernissprintU8(i))

# print("-- U10 --")
# for i in u10_times:
#     print(calculateHindernissprintU10(i))

# print("-- U12 --")
# for i in u12_times:
#     print(calculateHindernissprintU12(i))