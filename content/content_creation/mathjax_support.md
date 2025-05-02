Title: Mathjax support in VS Code and Pelican
Date: 2025-5-2 15:20
Category: Content Creation
Tags: pelican, markdown, webpage, mathjax, vs code, equation
Slug: mathjax_support
Authors: Yunchi Zhang
Summary: Describe how to support Mathjax in VS Code and Pelican.
Keywords: Mathjax, Equation, Pelican, Markdown

[TOC]

## Mathjax

MathJax is an open-source JavaScript display engine for LaTeX, MathML, and AsciiMath notation that
works in all modern browsers. Please refer to [Mathjax](https://www.mathjax.org/){: class="ampl"}
for details.

## Mathjax in VS Code

[VS Code](https://code.visualstudio.com/download) uses *KaTeX* by default as the math rendering
engine. VS Code extension [Markdown Preview Enhanced
(MPE)](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) is
the best option in VS Code if you want full MathJax support including equation numbering and
cross-referencing.

After the installation of MPE extension, one can go to its setting to change `Math Rending Option`
to `Mathjax`. For equation numbering and cross-referencing, press:

- `Ctrl+Shift+P` → **Markdown Preview Enhanced: Open Config Script (Global)**

Copy the following json configuration into the opened `config.js` file:

```json
{
  "mathjaxConfig": {
    "tex": {
      "inlineMath": [["$", "$"], ["\\(", "\\)"]],
      "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
      "tags": "ams"
    }
  }
}
```


## Mathjax Support in Pelican

Pelican plugin [render-math](https://github.com/pelican-plugins/render-math) can be installed to
render mathematics in the generated pages. It accomplishes this by using the MathJax JavaScript
engine.

To support equation numbering and cross-referencing, modify your theme’s HTML template to include
the correct MathJax config before the MathJax script:

```html
<script>
window.MathJax = {
  tex: {
    tags: 'ams',  // Enable automatic equation numbering
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  }
};
</script>
<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
```

## Equation Numbering and Cross-Referencing

In your Markdown file, write

```md
$$
\begin{equation}
E = mc^2 \label{eq:einstein}
\end{equation}
$$
```

It will result in:

$$
\begin{equation}
E = mc^2 \label{eq:einstein}
\end{equation}
$$

The equation number will be automatically generated as long as `\begin{equation}` and
`\end{equation}` are used. The numbered equation can be referenced with its name indicated by
`\label{name}`. To reference the above equation, `\ref{}` can be used. One can write:

```md
Equation [\ref{eq:einstein}] can be used for ...
```

It will result in:

Equation [\ref{eq:einstein}] can be used for ...
