import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    exclude: ["lucide-react", "axios"], // Exclude axios from optimization
  },
  build: {
    rollupOptions: {
      external: ["axios"], // Make axios external in the build process
    },
  },
});
