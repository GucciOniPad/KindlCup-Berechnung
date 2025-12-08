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

"""

4. Wettkampf Lindehalle

"""

def calculateWurfgeschwindigkeit(leistung):
    return leistung * 50

def calculateSprintgeschwindigkeit(leistung):
    return leistung * 90

def calculateStandweitsprung(leistung):
    return leistung

def calculateStaffelrhythmus(leistung):
    return leistung

"""
SPRINTGESCHWINDIGKEIT
"""

def calculateSprintgeschwindigkeitU8(leistung):
    # Leistung in km/h. B = 14.0 km/h ergibt 0 Punkte.
    a = 10.0
    b = 10.0
    c = 2.00
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

def calculateSprintgeschwindigkeitU10(leistung):
    # Leistung in km/h. B = 16.0 km/h ergibt 0 Punkte.
    a = 11.0
    b = 12.0
    c = 1.90
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

def calculateSprintgeschwindigkeitU12(leistung):
    # Leistung in km/h. B = 18.0 km/h ergibt 0 Punkte.
    a = 12.0
    b = 14.0
    c = 1.80
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

"""
WURFGESCHWINDIGKEIT
"""

def calculateWurfgeschwindigkeitU8(leistung):
    # Leistung in km/h. B = 15.0 km/h ergibt 0 Punkte.
    a = 1.5
    b = 15.0
    c = 2.00
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

def calculateWurfgeschwindigkeitU10(leistung):
    # Leistung in km/h. B = 18.0 km/h ergibt 0 Punkte.
    a = 1.8
    b = 18.0
    c = 1.90
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

def calculateWurfgeschwindigkeitU12(leistung):
    # Leistung in km/h. B = 22.0 km/h ergibt 0 Punkte.
    a = 2.0
    b = 22.0
    c = 1.80
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

"""
STANDWEIT
"""

def calculateStandweitsprungU8(leistung):
    # Leistung in Zentimetern. B = 70 cm ergibt 0 Punkte.
    a = 0.35
    b = 50.0
    c = 1.60
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

def calculateStandweitsprungU10(leistung):
    # Leistung in Zentimetern. B = 90 cm ergibt 0 Punkte.
    a = 0.25
    b = 70.0
    c = 1.70
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

def calculateStandweitsprungU12(leistung):
    # Leistung in Zentimetern. B = 110 cm ergibt 0 Punkte.
    a = 0.18
    b = 100.0
    c = 1.80
    if leistung <= b: return 0
    return math.floor(a * ((leistung - b)**c))

"""
TESTING
"""
# 1. 10m fliegend (km/h)
leistung_10m_fliegend_u8 = [14.0, 14.5, 15.1, 15.8, 16.5, 17.3, 18.1, 19.0, 20.0, 21.0]
leistung_10m_fliegend_u10 = [16.0, 16.5, 17.2, 18.0, 18.8, 19.7, 20.6, 21.6, 22.8, 24.0]
leistung_10m_fliegend_u12 = [18.0, 18.7, 19.4, 20.2, 21.1, 22.1, 23.2, 24.4, 25.7, 27.0]
# 2. 80g-Ballwurf (km/h)
leistung_ballwurf_u8 = [15.0, 16.5, 18.0, 20.0, 22.5, 25.0, 28.0, 31.5, 35.0, 38.0]
leistung_ballwurf_u10 = [18.0, 20.0, 22.0, 24.5, 27.5, 30.5, 34.0, 38.0, 42.5, 47.0]
leistung_ballwurf_u12 = [22.0, 25.0, 28.0, 31.5, 35.0, 38.5, 42.0, 46.0, 50.5, 55.0]
# 3. Standweitsprung (cm)
leistung_weitsprung_u8 = [70, 85, 100, 115, 130, 145, 160, 175, 190, 205]
leistung_weitsprung_u10 = [90, 105, 120, 135, 150, 165, 180, 195, 210, 225]
leistung_weitsprung_u12 = [110, 125, 140, 160, 180, 200, 220, 240, 260, 280]

def testU8():
    print("SPRINT")
    for leistung in leistung_10m_fliegend_u8:
        print(calculateSprintgeschwindigkeitU8(leistung))
    print("WURF")
    for leistung in leistung_ballwurf_u8:
        print(calculateWurfgeschwindigkeitU8(leistung))
    print("WEIT")
    for leistung in leistung_weitsprung_u8:
        print(calculateStandweitsprungU8(leistung))

def testU10():
    print("SPRINT")
    for leistung in leistung_10m_fliegend_u10:
        print(calculateSprintgeschwindigkeitU10(leistung))
    print("WURF")
    for leistung in leistung_ballwurf_u10:
        print(calculateWurfgeschwindigkeitU10(leistung))
    print("WEIT")
    for leistung in leistung_weitsprung_u10:
        print(calculateStandweitsprungU10(leistung))

def testU12():
    print("SPRINT")
    for leistung in leistung_10m_fliegend_u12:
        print(calculateSprintgeschwindigkeitU12(leistung))
    print("WURF")
    for leistung in leistung_ballwurf_u12:
        print(calculateWurfgeschwindigkeitU12(leistung))
    print("WEIT")
    for leistung in leistung_weitsprung_u12:
        print(calculateStandweitsprungU12(leistung))

def TEST_FULL():
    print("U8")
    testU8()
    print("U10")
    testU10()
    print("U12")
    testU12()

# TEST_FULL()