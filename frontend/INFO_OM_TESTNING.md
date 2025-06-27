# Testning i frontendprojekt

Testning i frontendprojekt med TypeScript och React är lite annorlunda än
backendtestning, men ofta väldigt kraftfullt och väl värt att göra, särskilt för
komponenter och API-logik.

## Var lägger jag testerna?

Standardpraxis är att lägga testfiler nära den kod de testar, med samma namn men
filändelsen .test.tsx eller .test.ts. Du kan också samla alla testfiler i en
tests/-mapp om du föredrar, men den närliggande modellen är vanligare i
React-världen.

## Vad kan (och bör) jag testa?

| Vad du vill testa                         | Hur du testar det                            | Verktyg                          |
| ----------------------------------------- | -------------------------------------------- | -------------------------------- |
| Komponenters rendering och innehåll       | Rendera dem och kontrollera resultatet       | `@testing-library/react`         |
| Användarinteraktioner (klick, input etc.) | Simulera händelser och kontrollera effekter  | `user-event` via Testing Library |
| API-funktioner                            | Kalla funktioner och kontrollera returvärden | `vitest`, `jest`                 |
| Navigering med router                     | Rendera med `MemoryRouter` eller liknande    | Testing Library                  |
| Tillstånd (loading, error etc.)           | Kontrollera olika renderingstillstånd        | Testing Library                  |

## Exempel på test

Se existerande testfiler:

- `frontend/src/pages/Sida1.test.tsx`
- `frontend/src/pages/Sida2.test.tsx`
- `frontend/src/components/ExamplePost.test.tsx`
- `frontend/src/api/example_api.test.ts`

## Kör testerna

Liksom du kan starta developmentservern med `npm run dev`, kan du köra testerna
med `npm run test`. Detta kommer att köra alla testfiler som matchar
`*.test.tsx` eller `*.test.ts`. `npm` kommer sedan att fortsätta lyssna efter
ändringar i dina filer och köra testerna igen automatiskt när du sparar.
