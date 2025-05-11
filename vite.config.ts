import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    exclude: ["lucide-react"], // DO NOT exclude axios
  },
  // REMOVE rollupOptions.external — let Vite bundle axios
});
