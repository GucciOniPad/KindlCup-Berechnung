import csv
import os
import calculations

"""
    Eine simple Funktion mit lediglich ästhetischem Zweck. Gibt an, welche Disziplin gerankt wurde.
    
    :param discipline: bearbeitete Disziplin
    :return: printed Finish Text auf stdout
"""
def writeDiscipline(discipline):
    if discipline == 's':
        print("Ranking for Schlagwurf completed. The Top Teams are in the output file.")
    elif discipline == 'd':
        print("Ranking for Drehwurf completed. The Top Teams are in the output file.")
    elif discipline == 'f':
        print("Ranking for Fünfsprung completed. The Top Teams are in the output file.")
    elif discipline == 'c':
        print("Ranking for Stadioncross completed. The Top Teams are in the output file.")
    elif discipline == 'b':
        print("Ranking for Biathlonstaffel completed. The Top Teams are in the output file.")
    elif discipline == 'h1':
        print("Ranking for Hürdensprint U8 completed. The Top Teams are in the output file.")
    elif discipline == 'h2':
        print("Ranking for Hürdensprint U10 completed. The Top Teams are in the output file.")
    elif discipline == 'h3':
        print("Ranking for Hürdensprint U12 completed. The Top Teams are in the output file.")
    elif discipline == 'k':
        print("Ranking for Kugelstoß completed. The Top Teams are in the output file.")
    elif discipline == 'p':
        print("Ranking for Stabweitsprung completed. The Top Teams are in the output file.")
    else:
        print("Ranking completed. The Top Teams are in the output file.")

"""
    Erstellt ein Ranking der einzelnen Leistungen und berechnet die Punktzahl für die gewollte Disziplin
    
    :param csv_file: file path
    :param discipline: char für Disziplin 's' (Schlagwurf), 'd' (Drehwurf), 'f' (Fünfsprung), 'c' (Stadioncross)
    :return: sorted data
"""
def read_and_process_data(csv_file, discipline):
    data = []
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["result"] = float(row["result"])
            data.append(row)

    reverse_sort = discipline in ['s', 'd', 'f', 'k', 'p']
    sorted_data = sorted(data, key=lambda x: x["result"], reverse=reverse_sort)
    if discipline in ['c', 'h1', 'h2', 'h3', 'b']:
        sorted_data = sorted(data, key=lambda x: x["result"])

    for entry in sorted_data:
        if discipline == 's':
            entry['points'] = calculations.calculateSchlagwurf(entry['result'])
        elif discipline == 'd':
            entry['points'] = calculations.calculateDrehwurf(entry['result'])
        elif discipline == 'f':
            entry['points'] = calculations.calculateFuenfSprung(entry['result'])
        elif discipline == 'c':
            entry['points'] = calculations.calculateStadioncross(entry['result'])
        elif discipline == 'k':
            entry['points'] = calculations.calculateStoss(entry['result'])
        elif discipline == 'p':
            entry['points'] = calculations.calculateStabweitsprung(entry['result'])
        elif discipline == 'b':
            entry['points'] = calculations.calculateBiathlonstaffel(entry['result'])
        elif discipline == 'h1':
            entry['points'] = calculations.calculateHindernissprintU8(entry['result'])
        elif discipline == 'h2':
            entry['points'] = calculations.calculateHindernissprintU10(entry['result'])
        elif discipline == 'h3':
            entry['points'] = calculations.calculateHindernissprintU12(entry['result'])
        else:
            print("Not a valid discipline")
            return []

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
