# Nollte iterationen - Frontend i Python

Detta är en grundläggande webbaserad frontend för projektet, byggd med
TypeScript och React. Den visar kort hur man kan organisera sina filer, en enkel
komponent och några API-anrop med `fetch`.

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

---

## Alternativ: Starta projektet från grunden

Om du inte vill klona exemplet kan du sätta upp projektet själv genom att följa
stegen nedan.

### 1. Installera Node.js

Du behöver ha **Node.js** installerat. Ladda ner och installera från:

👉 [https://nodejs.org/](https://nodejs.org/)

Kontrollera att det fungerar:

```bash
node -v
npm -v
```

### 2. Skapa nytt Vite-projekt med React + TypeScript

```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
```

> Detta skapar en katalog `frontend/` med ett grundprojekt.

### 3. Installera beroenden

Installera först de paket som Vite-projektet behöver:

```bash
npm install
```

### 4. Lägg till ytterligare beroenden

#### React Router (för navigering)

```bash
npm install react-router-dom
```

#### ESLint och Vitest (för testning och kodstil)

```bash
npm install --save-dev \
  eslint @eslint/js eslint-plugin-react-hooks eslint-plugin-react-refresh \
  vitest @testing-library/react @testing-library/jest-dom \
  typescript typescript-eslint @types/react @types/react-dom \
  jest jsdom globals
```

> Du kan förstås välja till/bort paket efter behov.

### 5. Starta utvecklingsservern

```bash
npm run dev
```

Öppna [http://localhost:5173](http://localhost:5173) för att se appen i
webbläsaren.
