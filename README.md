Herzlich willkommen zur Auswertung des Münchner Kindl Cups!

Im Folgenden wird das grundlegende Konzept der Berechnung erklärt. Außerdem finden sich hier die exakten Ergebnisse aller Athleten für den ersten Stopp der Wettkampfserie am 30.03.2025 am PSV München.

# Berechnung
Das gesamte Tool besteht im Wesentlichen aus einem [Python Script](./csv_parser.py), welches Daten aus den Ergebnislisten (.csv) liest und die Punkte mithilfe vorher aufgestellter Formeln berechnet.
Die genauen Werte der Formeln lassen sich in [calculations.py](./calculations.py) nachvollziehen. Die Faktoren der Formeln orientieren sich an den offiziellen Berechnungen der Punktzahlen im Zehnkampf, wobei jeweils die Disziplin mit der besten vergleichbarkeit gewählt wurde (z.B. $\text{Drehwurf}\Leftrightarrow\text{Diskuswurf}$).

Nachdem jeder Leistung eine Punktzahl zugewiesen wurde, werden pro Disziplin die besten 6 Leistungen jedes Teams verwendet, um die Punktzahl des Teams für die jeweilige Disziplin zu berechnen. Aktuell endet die automatische Berechnung hier und für die finalen Punkte müssen die Punkte aller Teams über die 4 Disziplinen händisch aufsummiert werden. In Zukunft kann dieser Schritt noch in den Code eingebaut werden.

Der hier verwendete Code bietet viele Vorteile zu z.B. einer Berechnung mit Excel, da er einfacher an andere Disziplinen anpassbar ist, flexibler und stabiler läuft und schnell und selbstständig auf mehreren Dateien arbeiten kann. Der Code kann einfach getestet werden, indem z.B. über eine Shell die Datei [main.py](./main.py) ausgeführt wird und den Anweisungen auf der Konsole gefolgt wird. 

# Ergebnisse
Für jedes Kind floß bei den technischen Disziplinen der beste aus drei Versuchen in die Berechnung ein. Die Ergebnisse sind nach Jahrgängen und Disziplinen sortiert (nicht nach Teams). In den Top 6 Ergebnislisten sind die Teams absteigend nach erreichter Punktesumme sortiert.

Im Ordner [resultlists](./resultlists/) finden sich alle Ergebnisse aus den einzelnen Wettkämpfen. Die Dateien können direkt hier im Browser eingesehen und heruntergeladen werden.
Die tatsächlichen Ergebnisse mit den Top 6 Leistungen pro Team finden sich in gleichem Format im Verzeichnis [output_files](./output_files/). Außerdem findet sich hier pro Altersklasse eine .txt Datei mit den Endergebnissen. Die Spalte `name` entspricht hier übrigens immer der Startnummer des Athleten. 

**Nachtrag Datenformat:** Das angegebene `result` ist immer der beste Versuch des Athleten. Folgende Datenformate wurden verwendet: Wurf - Meter (gerundet), Sprung - Zentimeter, Stadioncross - Sekunden (gerundet). Somit ergibt sich die Notation in der .csv Datei bestehend aus `name` (Startnummer), `team` und `result` (bester Versuch im oben genannten Format).

Zum Testen des Programms finden sich im Ordner [resultlists/test](./resultlists/test) und im dazugehörigen Ordner [output_files/test](./output_files/test) ein beispielhafter Datensatz mit ca. 500 Einträgen.

---

Bei allgemeinen Fragen zur Berechnung, dem Code und der Verwendung, stehe ich unter [kian27@outlook.de](mailto:kian27@outlook.de) gerne zur Verfügung. 

Hoffe alles ist soweit verständlich :)
