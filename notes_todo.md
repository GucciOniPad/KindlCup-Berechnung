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

---

# Event 2
1. Hindernissprint - Drei Formeln wegen Distanz
2. Biathlonstaffel - Eine Berechnung evtl. pro Team (im Fall einf Wert als Wert)
3. Stabweitsprung - Eine Formel fur alle (Weitsprung
   -> Alle 25cm ein Punkt extra (Zonen System). Daher punktzahl multiplizieren, um vergleichbare Werte zu erhalten
4. Stoßen - Eine Formel fur alle (Kugelstoßen)

## Stabweit Überlegungen
- Weiten zwischen 0 und 5 Metern erwartet
  -> max. Punkte hier 20
- Fünfsprung Punkte am PSV waren in den Top 6 ca. zwischen 150 und 350
  - 350 / 20 = 17.5 (preliminary factor)

-> Punkte für Punktwerte [0, 20] in [0,350]. Im Schnitt haben wir eine Leistung von 11.25 Punkten (281cm), was 175 Punkten entspricht.
-> Evtl. Faktor etwas erhöhen. Mit 18.5 erhalten wir im Schnitt 208 Punkte. Im Vergleich Funfsprung U10 hatte im Schnitt 237 Punkte.