import csv

import calculations

""""
old read and process data
"""""

def read_and_process_data(csv_file, discipline):
    data = []
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["result"] = float(row["result"])
            data.append(row)

    reverse_sort = discipline in ['s', 'd', 'f', 'k', 'p', 'j1', 'j2', 'sg1', 'sg2', 'sg3', 'wg1', 'wg2', 'wg3', 'sw1', 'sw2', 'sw3'] # New 9 disciplines
    sorted_data = sorted(data, key=lambda x: x["result"], reverse=reverse_sort)
    if discipline in ['c', 'h1', 'h2', 'h3', 'b', 's1', 's2', 's3']:
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
        elif discipline == 's1':
            entry['points'] = calculations.calculateSprintU8(entry['result'])
        elif discipline == 's2':
            entry['points'] = calculations.calculateSprintU10(entry['result'])
        elif discipline == 's3':
            entry['points'] = calculations.calculateSprintU12(entry['result'])
        elif discipline == 'j1':
            entry['points'] = calculations.calculateHighJumpU8U10(entry['result'])
        elif discipline == 'j2':
            entry['points'] = calculations.calculateHighJumpU12(entry['result'])
        elif discipline == 'sg1':
            entry['points'] = calculations.calculateSprintgeschwindigkeitU8(entry['result'])
        else:
            print("Not a valid discipline")
            return []

    return sorted_data


"""
old write discipline
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
    elif discipline == 's1':
        print("Ranking for Sprint U8 completed. The Top Teams are in the output file.")
    elif discipline == 's2':
        print("Ranking for Sprint U10 completed. The Top Teams are in the output file.")
    elif discipline == 's3':
        print("Ranking for Sprint U12 completed. The Top Teams are in the output file.")
    elif discipline == 'j1':
        print("Ranking for Hoch-Weit-Sprung U8/U10 completed. The Top Teams are in the output file.")
    elif discipline == 'j2':
        print("Ranking for Hochsprung U12 completed. The Top Teams are in the output file.")
    else:
        print("Ranking completed. The Top Teams are in the output file.")
    # TODO: Lindehalle aesthetics
