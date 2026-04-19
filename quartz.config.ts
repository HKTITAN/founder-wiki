import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Founder Wiki",
    enableSPA: true,
    enablePopovers: true,
    locale: "en-US",
    baseUrl: "founderwiki.co",
    ignorePatterns: ["private", "templates", ".obsidian", "_*.md", "_*.json"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#fffefc",
          lightgray: "#f2f0eb",
          gray: "#b9b2a6",
          darkgray: "#5b5143",
          dark: "#1f1a14",
          secondary: "#b2551a",
          tertiary: "#8b6f47",
          highlight: "rgba(178, 85, 26, 0.10)",
          textHighlight: "#f5df8d",
        },
        darkMode: {
          light: "#18130f",
          lightgray: "#31291f",
          gray: "#8a7b66",
          darkgray: "#d2c8ba",
          dark: "#f6f1e9",
          secondary: "#f0965f",
          tertiary: "#c5a67d",
          highlight: "rgba(240, 150, 95, 0.18)",
          textHighlight: "#8c6f14",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
