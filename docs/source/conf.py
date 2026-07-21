# Configuration file for the Sphinx documentation builder.

project = "Introducción a la Inteligencia Artificial"
copyright = "2026, Juan Montiel"
author = "Juan Montiel"
release = "2026"

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

language = "es"

html_theme = "furo"
html_title = "Introducción a la Inteligencia Artificial"

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2563eb",
        "color-brand-content": "#2563eb",
        "color-background-primary": "#f8fafc",
        "color-background-secondary": "#eef2ff",
        "color-foreground-primary": "#0f172a",
        "color-foreground-secondary": "#475569",
        "color-link": "#2563eb",
        "color-link--hover": "#7c3aed",
        "font-stack": "Inter, Segoe UI, Roboto, Arial, sans-serif",
        "font-stack--monospace": "Consolas, Monaco, monospace",
    },

    "dark_css_variables": {
        "color-brand-primary": "#22d3ee",
        "color-brand-content": "#60a5fa",
        "color-background-primary": "#070b14",
        "color-background-secondary": "#0f172a",
        "color-foreground-primary": "#f8fafc",
        "color-foreground-secondary": "#cbd5e1",
        "color-link": "#60a5fa",
        "color-link--hover": "#22d3ee",
    },
}
