1. Ergebnisse kommen per Liste (Papier)

   → Gibt es ein Tool, das das automatisch zu einer csv macht?
2. Einzelwertung?? Am Ende Top Athleten be stimmen?

---

## Roadmap:
- Final Ranking out of singular discipline files
- Top ranked athlete per / over all disciplines
- Evtl: Force inclusion of female athlete per ranking

### calculateFormalScoring:
In den finalen output files sind immer top6 + score (mind. 6 pro Team, also immer 6)
Loop über die alle 6. Zeilen des Files gibt scores zurück

Wir brauchen pro File die scores sowie den Teamnamen, der den jeweiligen Score hat
- Loop bekommt die 4 Ergebnislisten
- Geht durch die einzelnen Files und erstellt initial eine output Datei mit allen Teams und dem finalen score
- Nach iteration über alle files und aller Zeilen pro File haben wir die finalen Scores in einer Datei
- Berechnet wird pro Disziplin. 1p Platz 1, 2p Platz 2, usw.

-> Geringste Summe gewinnt (evtl. zwischenspeichern mit Map <teamname, punkte>?)