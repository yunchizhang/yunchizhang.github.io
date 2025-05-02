Title: Markdown codeblock format for Pelican
Date: 2025-5-1 14:00
Category: Content Creation
Tags: pelican, markdown, webpage
Slug: codeblock_markdown_pelican
Authors: Yunchi Zhang
Summary: Describe how to write codeblock inside a list item in markdown.
Keywords: Pelican, Markdown, Codeblock, CodeHilite

[TOC]

## Code Snippet in Markdown

### Inline Code

The single **backticks \`** in Markdown can be used to indicate inline code. For example,
\`inline code\` is displayed as `inline code`. This is also recognized by Pelican that uses
[Pygments](https://pygments.org/) for code highlighting.

### Codeblock

There are a few ways to indicate codeblock in Markdown. Two primary methods are usually employed:
Indented Code and "Fenced" Code Block.

!!! note
    Fenced Code Block is recommended to use for syntax highlighting purpose.

#### Indented Code

Preceding all codes by an indent (4 spaces or tab).

For example, the following indented block:

```md
    # python code
    print(f"This is a test")
    print(f"This is another test")
    print(f"This is another test")
    print(f"This is another test")
```

produces:

    # python code
    print(f"This is a test")
    print(f"This is another test")
    print(f"This is another test")
    print(f"This is another test")

There is no syntax highlighting while using indented code since the language can not be specified.

#### [Fenced Code Blocks](https://python-markdown.github.io/extensions/fenced_code_blocks/)

Use triple backticks (**\`\`\`**) or triple tildes (**~~~**) and the name of the language. Fenced
code block usually support syntax highlighting since the language can be specified.

For example,

````md
```python
# python code
print(f"This is a test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
```
````

produces:

```python
# python code
print(f"This is a test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
```

To include a set of backticks (or tildes) within a code block, use a different number of backticks
for the delimiters.

`````md
````
```
````
`````

!!! important

    When using Fenced code block, **\`\`\`** or **~~~** should not be indented, otherwise it will be treated as
    indented code block.

!!! warning
    Fenced Code Blocks are only supported at the document root level. Therefore, they cannot be
    nested inside lists or blockquote's. If you need to nest fenced code blocks, you may want to try
    the third party extension [SuperFences] instead.

## Codeblock Syntax Highlighting for Pelican

[Python-Markdown](https://github.com/Python-Markdown/markdown/) uses
[CodeHilite](https://python-markdown.github.io/extensions/code_hilite/) extension for syntax
highlighting. This extension is included in the standard Markdown library.

### Fenced Code Block

Various attributes may be defined on a per-code-block basis by defining them immediately following
the opening deliminator. The attributes should be wrapped in curly braces {} and be on the same
line as the deliminator. It is generally best to separate the attribute list from the deliminator
with a space. Attributes within the list must be separated by a space. So long as the language is
the only option specified, the curly brackets and/or the dot may be excluded.

````md
``` { attributes go here }
a code block with attributes
```
````

The codehilite extension uses the [Pygments](https://pygments.org/) engine to do syntax
highlighting. Any valid Pygments options can be defined as key/value pairs in the attribute list
and will be passed on to Pygments.

````md
``` { .lang linenos=true linenostart=42 hl_lines="43-44 50" title="An Example Code Block" }`
A truncated code block...
```
````

For example,

````md
``` {.python linenos=true linenostart=42 hl_lines="2 4" title="A Python Codeblock"}
# python code
print(f"This is a test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
```
````

will produce:

``` {.python linenos=true linenostart=42 hl_lines="2 4" title="A Python Codeblock"}
# python code
print(f"This is a test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
print(f"This is another test")
```

!!! note
    `hl_lines` should be specified by the actual line count number in the codeblock. Do not count the
    line from `linenostart`.

To disable syntax highlighting on an individual code block, include `use_pygments=false` in the
attribute list. For example:

````md
``` {.python use_pygments=false style="color: #030303; background: #f8f8f8;"}
# python code
print(f"This is a test")
print(f"This is another test")
```
````

will produce:

``` {.python use_pygments=false style="color: #030303; background: #f8f8f8;"}
# python code
print(f"This is a test")
print(f"This is another test")
```

### Indented Code Block

Either **Sheband** or **Colons** can be used to tell CodeHilite what language the codeblock contains.

#### Shebang

Line numbers will be displayed by default.

```md
    #!python
    # Code goes here ...
```

will result in:

    #!python
    #Code goes here ...

To highlight lines:

```md
    #!python hl_lines="1 3"
    # This line is emphasized
    # This line isn't
    # This line is emphasized
```

will result in:

    #!python hl_lines="1 3"
    # This line is emphasized
    # This line isn't
    # This line is emphasized

#### Colons

If the first line begins with three or more colons, the text following the colons identifies the
language. The first line is removed from the code block before processing and line numbers are not
used.

```md
    :::python
    # Code goes here ...
```

will result in:

    :::python
    # Code goes here ...

To highlight lines:

```md
    :::python hl_lines="1 3"
    # This line is emphasized
    # This line isn't
    # This line is emphasized
```

will result in:

    :::python hl_lines="1 3"
    # This line is emphasized
    # This line isn't
    # This line is emphasized

## Markdown CodeHilite Extension for Pelican

In `pelicanconf.py`, CodeHilite should be configured to use `.highlight` CSS class.

```python
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"}
    },
}
```
