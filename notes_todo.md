## Roadmap / Possible additions:
- Final Ranking out of singular discipline files
- Top ranked athlete per / over all disciplines
- Evtl.: Force inclusion of female athlete per ranking

### calculateFinalScoring:
In den finalen output files sind immer top6 + score (mind. 6 pro Team, also immer 6)
Loop über alle 6. Zeilen des Files gibt scores zurück

Wir brauchen pro File die scores sowie den Teamnamen, der den jeweiligen Score hat
- Loop bekommt die Ergebnislisten
- Geht durch die einzelnen Files und erstellt initial eine output Datei mit allen Teams und dem finalen score
- Nach iteration über alle files und aller Zeilen pro File haben wir die finalen Scores in einer Datei
