# Nollte iterationen - Backend i Python

Detta är en grundläggande webbaserad frontend för projektet, byggd med
TypeScript och React.

## Projektstruktur

Ni kommer att ha **ett** repository som innehåller både frontend och backend, i
katalogerna `frontend/` och `backend/`. Detta repo är endast frontend-delen av
projektet. Ni ska lägga in denna frontend i ert eget projektrepo, i en undermapp
som heter `frontend/`.

## Steg för steg

1. **Klona ert eget repo (om ni inte redan gjort det):**

```bash
git clone git@coursegit.cs.lth.se:edaf45/htXX-vtXX/projects/teamNN.git
cd teamNN
```

Byt ut `htXX-vtXX` mot rätt kursomgång (t.ex. `ht25-vt26`) och `teamNN` mot ert
teamnummer (t.ex. `team07`).

2. **Lägg till frontend som en extra remote och hämta koden:**

```bash
git remote add frontend git@coursegit.cs.lth.se:edaf45/samples/nollte_frontend_ts_react.git
git fetch frontend
```

3. **Checka ut frontend-koden i en ny branch:**

```bash
git checkout -b frontend-import frontend/main
```

4. **Gå tillbaka till main-branchen och slå ihop:**

```bash
git checkout main
git merge frontend-import
```

Nu finns frontend-koden i mappen `frontend/` i ert eget repo!

5. **Ta bort den temporära branchen och remoten:**

```bash
git branch -d frontend-import
git remote remove frontend
```
