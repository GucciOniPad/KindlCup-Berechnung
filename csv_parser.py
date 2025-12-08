import csv
import os
from csv import DictWriter

import calculations

DISCIPLINE_MAP = {
    's': calculations.calculateSchlagwurf,
    'd': calculations.calculateDrehwurf,
    'f': calculations.calculateFuenfSprung,
    'c': calculations.calculateStadioncross,
    'k': calculations.calculateStoss,
    'p': calculations.calculateStabweitsprung,
    'b': calculations.calculateBiathlonstaffel,
    'h1': calculations.calculateHindernissprintU8,
    'h2': calculations.calculateHindernissprintU10,
    'h3': calculations.calculateHindernissprintU12,
    's1': calculations.calculateSprintU8,
    's2': calculations.calculateSprintU10,
    's3': calculations.calculateSprintU12,
    'j1': calculations.calculateHighJumpU8U10,
    'j2': calculations.calculateHighJumpU12,
    'sg1': calculations.calculateSprintgeschwindigkeitU8,
    'sg2': calculations.calculateSprintgeschwindigkeitU10,
    'sg3': calculations.calculateSprintgeschwindigkeitU12,
    'wg1': calculations.calculateWurfgeschwindigkeitU8,
    'wg2': calculations.calculateWurfgeschwindigkeitU10,
    'wg3': calculations.calculateWurfgeschwindigkeitU12,
    'sw1': calculations.calculateStandweitsprungU8,
    'sw2': calculations.calculateStandweitsprungU10,
    'sw3': calculations.calculateStandweitsprungU12,
}


"""
    Eine simple Funktion mit lediglich ästhetischem Zweck. Gibt an, welche Disziplin gerankt wurde.
    
    :param discipline: bearbeitete Disziplin
    :return: printed Finish Text auf stdout
"""
def writeDiscipline(discipline):
   discipline = DISCIPLINE_MAP.get(discipline, "Unknown Discipline")

   if discipline == "Unknown Discipline":
       print("Ranking completed. The Top Teams are in the output file.")
   else:
       print(f"Ranking for {discipline} completed. The Top Teams are in the output file.")

"""
    Erstellt ein Ranking der einzelnen Leistungen und berechnet die Punktzahl für die gewollte Disziplin
    
    :param csv_file: file path
    :param discipline: char für Disziplin 
    :return: sorted data
"""
def read_and_process_data(csv_file, discipline):
    data = []
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["result"] = float(row["result"])
            data.append(row)

    calc_func = DISCIPLINE_MAP.get(discipline)
    if not calc_func:
        print("Invalid discipline")
        return []

    REVERSE_MAP = {
        's', 'd', 'f', 'k', 'p', 'j1', 'j2', 'sg1', 'sg2', 'sg3',
        'wg1', 'wg2', 'wg3', 'sw1', 'sw2', 'sw3'
    }

    is_reversed = discipline in REVERSE_MAP
    sorted_data = sorted(data, key=lambda x: x["result"], reverse=is_reversed)

    for entry in sorted_data:
        entry["points"] = calc_func(entry["result"])

    return sorted_data

"""
    Erstellt auf Basis einer Input Datei die gerankte Datei (read_and_process_data()) und schreibt diese in ein .csv file
    
    :param csv_file: input file path
    :param discipline: char für Disziplin 's' (Schlagwurf), 'd' (Drehwurf), 'f' (Fünfsprung), 'c' (Stadioncross)
    :param output_file: output file path
    :return: fertige .csv + Bestätigung auf stdout
"""
def writeFileRankingCSV(csv_file, discipline, output_file):
    sorted_data = read_and_process_data(csv_file, discipline)
    if not sorted_data:
        return

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    fieldnames = ["name", "team", "result", "points"]
    with open(output_file, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)

    print(f"Results successfully written to {output_file}")

"""
    Erstellt, basierend auf einer .csv Datei mit berechneten Punkten ein Ranking der einzelnen Teams, wobei jeweils die Top 6 Punktzahlen pro Team addiert werden
    Mit dieser Methode ist die Bearbeitung einer Disziplin jeweils abgeschlossen. 
    
    :param csv_file: input file path
    :param output_file: output file path
    :param discipline: bearbeitete Disziplin (für finalen print)
    :return: fertige .csv + Bestätigung auf stdout 
"""
def writeTop6PerTeamCSV(csv_file, output_file, discipline):
    data = []
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["result"] = float(row["result"])
            row["points"] = float(row["points"])
            data.append(row)

    teams = {}
    for entry in data:
        team = entry["team"]
        if team not in teams:
            teams[team] = []
        teams[team].append(entry)

    top6_per_team = {}
    for team, entries in teams.items():
        sorted_entries = sorted(entries, key=lambda x: x["points"], reverse=True)[:6]
        top6_per_team[team] = {
            "entries": sorted_entries,
            "sum": sum(e["points"] for e in sorted_entries)
        }

    sorted_teams = sorted(top6_per_team.items(), key=lambda x: x[1]["sum"], reverse=True)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    fieldnames = ["team", "name", "result", "points"]
    with open(output_file, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for team, data in sorted_teams:
            for entry in data["entries"]:
                writer.writerow({"team": team, "name": entry["name"], "result": entry["result"], "points": entry["points"]})
            writer.writerow({"team": "", "name": "SUM", "result": "", "points": data["sum"]})
