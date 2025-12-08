import os
from pathlib import Path
from unittest import case

import csv_parser

# TODO: Write Main which prompts user and does things (ask if we want to create final ranking or just rank discipline)

"""
    Erfragt Disziplin, die berechnet werden soll und führt die Berechnung auf den csv Dateien durch
"""
def calculateDiscipline():
    # print("Select discipline: 'b' - Biathlonstaffel, 'h1' - Hindernissprint U8, 'h2' - Hindernissprint U10, 'h3' - Hindernissprint U12, 'k' - Stoßen, 'p' - Stabweitsprung")
    # discipline = input("Enter discipline: 's' - Schlagwurf, 'd' - Drehwurf, 'f' - Fünfsprung, 'c' - Stadioncross\n").strip()
    # print("Select discipline: 's1' - Sprint U8, 's2' - Sprint U10, 's3' - Sprint U12, 'j1' - Hoch-Weit-Sprung U8/U10, 'j2' - Hochsprung U12")
    age_group = input("Select Age Group 'u8', 'u10', 'u12': ").strip()
    match age_group:
        case 'u8': print("Select u8 discipline: 'sg1' - Sprintgeschwindkeit, 'wg1' - Wurfgeschwindigkeit, 'sw1' - Standweitsprung")
        case 'u10': print("Select u10 discipline: 'sg2' - Sprintgeschwindkeit, 'wg2' - Wurfgeschwindigkeit, 'sw2' - Standweitsprung")
        case 'u12': print("Select u12 discipline: 'sg3' - Sprintgeschwindkeit, 'wg3' - Wurfgeschwindigkeit, 'sw3' - Standweitsprung")
    discipline = input("Enter discipline: ").strip()

    input_path = input("Enter path to the input file:\n").strip()
    output_path = input("Enter path to the desired output file:\n").strip()

    # Normalize paths (hopefully better way)
    input_file = Path(input_path).resolve()
    output_file = Path(output_path).resolve()

    csv_parser.writeFileRankingCSV(str(input_file), discipline, "output_files/out_test.csv")
    csv_parser.writeTop6PerTeamCSV("output_files/out_test.csv", str(output_file), discipline)

"""
    Berechnet das finale ranking basierend auf den einzelnen Disziplinsrankings
"""
def calculateFinalScoring():
    output_files = input("Enter path to directory of output files:\n")
    # Loop through files in dir and perform ranking
    # Write Final scoring in output file

"""
    Diese Funktion startet, je nach User input, die Berechnung für eine Disziplin oder die finale Auswertung
"""
def checkCalculation():
    operation = input("Select operation: 'd' to get ranking for discipline, 'f' to get final results\n")
    if operation == 'd':
        calculateDiscipline()
    elif operation == 'f':
        print("Not yet supported")
    else:
        print("Unsupported Operation. Please provide either 'd' or 'f'")

# checkCalculation()
calculateDiscipline()
# nice
