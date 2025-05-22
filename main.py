import os
import csv_parser

# TODO: Write Main which prompts user and does things (ask if we want to create final ranking or just rank discipline)

"""
    Erfragt Disziplin, die berechnet werden soll und führt die Berechnung auf den csv Dateien durch
"""
def calculateDiscipline():
    print("Select discipline: 'b' - Biathlonstaffel, 'h1' - Hindernissprint U8/U10, 'h2' - Hindernissprint U12, 'k' - Stoßen, 'p' - Stabweitsprung")
    discipline = input("Enter discipline: ").strip()
    # discipline = input("Enter discipline: 's' - Schlagwurf, 'd' - Drehwurf, 'f' - Fünfsprung, 'c' - Stadioncross\n").strip()
    input_file = os.path.normpath(input("Enter path to the input file:\n").strip())
    output_file = os.path.normpath(input("Enter path to the desired output file:\n").strip())

    csv_parser.writeFileRankingCSV(input_file, discipline, "output_files/out_test.csv")
    csv_parser.writeTop6PerTeamCSV("output_files/out_test.csv", output_file, discipline)

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
