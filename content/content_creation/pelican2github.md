Title: Publish Pelican Webpages to Github Pages
Date: 2024-09-29 10:46
Modified: 2025-5-2 12:44
Category: Content Creation
Tags: pelican, github, python, webpage
Slug: pelican_on_github
Authors: Yunchi Zhang
Summary: Describe how to publish Pelican generated webpages to Github pages.
Keywords: Pelican, Github

[TOC]

# Pelican and Github Pages

You can publish [Pelican](https://getpelican.com/) generated site to [GitHub
Pages](https://pages.github.com/) for free. Your site will be published to `https://yourusername.github.io`.

[Pelican document](https://docs.getpelican.com/en/latest/){: class="ampl"} should be referenced for
[Pelican](https://getpelican.com/) installation and usages.

Please refer to [GitHub Pages](https://pages.github.com/){: class="ampl"} for details.

# HowTo

There are two ways to publish a site to GitHub Pages:

1. **Publish from a branch:** run `pelican` locally and push the output directory to a special branch
   of your GitHub repo.
2. **Publishing with a custom GitHub Actions Workflow:** just push the source files of your Pelican
   site to your GitHub repo's default branch and have a custom GitHub Actions workflow run
   `pelican` to generate the output directory and publish to GitHub pages site.

The first method will be discussed in this article.

## Github User Page

To publish your Pelican website to `https://yourusername.github.io` (i.e., user site rather than
project site), GitHub requires the `gh-pages` branch to be the root of the repository – no
subdirectory. The following procedure utilizes two branches in the repository.

**Configure GitHub Page**

On GitHub, create `yourusername.github.io` repository with two branches.

   - `main` branch → for published site (HTML only)
   - `pelican` branch → for your Pelican source files

Go to **Repo → Settings → Pages**. Under **Source**, select:

   - Branch: `main`
   - Folder: `/(root)`

GitHub will serve from: `https://yourusername.github.com`.


**Clone the `yourusername.github.io`:**

```bash
git clone https://github.com/yourusername.github.io.git
cd yourusername.github.io
```

**Create and switch to the `pelican` branch:**

```bash
git checkout --orphan pelican
git rm -rf .
```

## Pelican Webpage Generation

**Install Pelican and Tools**

```bash
pip install pelican[markdown] ghp-import
```

**Initialize Pelican**

```bash
pelican-quickstart
```

Choose:

- Site URL: `https:\\yourusername.github.io`
- Use relative URLs: Yes
- Generate Makefile: Yes

**Commit and Push**

Add `.gitignore`. Then,

```bash
git add .
git commit -m "Initial Pelican site"
git push origin pelican
```

**Pelican Themes and Plugins**

A Pelican theme should be configured for site generation.
[Elegant](https://elegant.oncrashreboot.com/) theme is recommended.

```bash
git clone https://github.com/Pelican-Elegant/elegant.git themes/elegant
```

Set the theme in `pelicanconf.py`:

```python
THEME = 'themes/elegant'
```

Install your desired Pelican plugins. For example:

```bash
pip install pelican-render-math
```

**Write Contents and Preview**

Contents can be written in either Markdown or rStructureText format. In `windows` system, a batch
file can be used to generate and preview webpages in a local server.

```batch
pelican content && ^
start "" "http://localhost:8000/" && ^
pelican --listen && ^
REM Ctrl-C to quit
```

## Deploy Generated Webpages

Pelican will generate output into output/. You’ll use `ghp-import` to publish that to `main`
branch. Batch files in `windows` system can be used for this purpose.

**`pelican` Branch (`publish_private.bat`)**

```batch
git checkout pelican
git add .
git commit -a -m %1
git push -u origin pelican
```

**`main` Branch (`publish_public.bat`)**

```batch
pelican content -o output -ds publishconf.py && ^
ghp-import output -r origin -b main && ^
git push origin main
git checkout pelican
```

**Batch File to Call Both (`publish.bat`)**

```batch
REM .\publish "some comment" # when called inside PS
call publish_private.bat %1
call publish_public.bat
ECHO Done
```

# Editor

[VS Code](https://code.visualstudio.com/download) is suggested for creating the contents.

# Tips

## Nested List

For nested list, Python-Markdown uses four-space indents. For example:

```md
- **Visual Narration**: Description here
- **Story Arcs and Pacing**:
   * Sub-item 1, two space indent
   * Sub-item 2, two space indent
```

works for some Markdown parser, but not for Python-Markdown. Python-Markdown (also Pelican) will
produce:

- **Visual Narration**: Description here
- **Story Arcs and Pacing**:
   - Sub-item 1, two space indent
   - Sub-item 2, two space indent

It must be written as:

```md
- **Visual Narration**: Description here
- **Story Arcs and Pacing**:
    - Sub-item 1, four space indent
    - Sub-item 2, four space indent
```

for Python-Markdown (as well as Pelican) to parse correctly. It will result in:

- **Visual Narration**: Description here
- **Story Arcs and Pacing**:
    - Sub-item 1, four space indent
    - Sub-item 2, four space indent

Also,

```md
1. **Visual Narration**: Description here
    - Sub-item 1, four space indent
    - Sub-item 2, four space indent
2. **Story Arcs and Pacing**:
    - Sub-item 1, four space indent
    - Sub-item 2, four space indent
```

will produce:

1. **Visual Narration**: Description here
    - Sub-item 1, four space indent
    - Sub-item 2, four space indent
2. **Story Arcs and Pacing**:
    - Sub-item 1, four space indent
    - Sub-item 2, four space indent
