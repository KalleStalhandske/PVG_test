// src/router.tsx
import { createBrowserRouter } from "react-router-dom"
import App from "./App"
import Reg from "./pages/Reg"

/*
  Detta är routerkonfigurationen för vår React-applikation. Den definierar hur
  olika sidor och komponenter ska renderas baserat på URL:en. Vi använder
  createBrowserRouter från react-router-dom för att skapa en router.
  main.tsx importerar denna router.
*/

const router = createBrowserRouter([
  {
    path: "/",
    // App är vår "layout" komponent som innehåller navigering och Outlet.
    // Outlet används för att rendera underliggande children routes.
    element: <App />,
    children: [
      {
        index: true, // path: ""
        element: <h2>Välkommen till startsidan!</h2>,
      },
      {
        path: "reg",
        element: <Reg/>,
      }
    ],
  },
])

export default router
