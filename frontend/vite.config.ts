import react from "@vitejs/plugin-react"
import { defineConfig, type UserConfig } from "vite"

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: "jsdom",
  },
} as UserConfig)
