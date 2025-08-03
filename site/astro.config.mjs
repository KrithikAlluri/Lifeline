import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import icon from "astro-icon";

// https://astro.build/config
export default defineConfig({
  site: "https://lifeline.dev",
  integrations: [mdx(), sitemap(), icon()],
  output: 'server',
  vite: {
    plugins: [tailwindcss()],
  },
});
