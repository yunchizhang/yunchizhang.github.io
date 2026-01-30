Title: Directory Tree in Windows
Date: 2026-1-30 15:00
Category: Coding
Tags: PowerShell, Windows, Directory
Slug: directory_tree_windows
Authors: Yunchi Zhang
Summary: Generate directory tree in Windows operating system.
Keywords: Directory, Tree

[TOC]

In Windows, if you want to see the directory structure up to a specific depth level. **PowerShell**
script can be used. Windows has a built-in `tree` command. While it doesn't have a "depth" flag,
you can simulate it in **PowerShell** by filtering the output, though it's a bit "hacky."

For a cleaner approach, I recommend sticking to **PowerShell** objects.

## The "Custom Tree" Script

```PowerShell
function Show-Tree {
<#
.SYNOPSIS
Displays a directory tree with configurable depth.

.DESCRIPTION
Show-Tree outputs a tree-like view of folders (and optionally files),
starting from a given path. Supports depth control, Unicode characters,
and optional inclusion of hidden files.Indent is internal; use -IncludeFiles,
-Unicode, and -ShowHidden as needed.

.PARAMETER Path
Root directory. Defaults to current directory.

.PARAMETER Depth
Maximum recursion depth.

.PARAMETER IncludeFiles
Include files in output.

.PARAMETER Unicode
Use Unicode tree characters (runtime-safe).

.PARAMETER ShowHidden
Include hidden items.

.EXAMPLE
Show-Tree
- Displays the current directory tree up to the default depth (2), showing only folders.

.EXAMPLE
Show-Tree -Depth 3
- Displays the current directory tree up to 3 levels deep, showing only folders.

.EXAMPLE
Show-Tree -IncludeFiles
- Displays folders and files under the current directory up to the default depth (2).

.EXAMPLE
Show-Tree -Path C:\Projects -IncludeFiles -Depth 4 -Unicode
- Displays a Unicode tree of folders and files under C:\Projects up to 4 levels deep.

.EXAMPLE
Show-Tree -Path D:\Work -IncludeFiles -Depth 2 -ShowHidden
- Displays folders and files under D:\Work up to 2 levels, including hidden items.

.NOTES
Author: ChatGPT
Compatible with Windows PowerShell 5.1 and PowerShell 7+
#>

    param(
        [string]$Path = ".",
        [int]$Depth = 2,
        [string]$Indent = "",
        [switch]$IncludeFiles,
        [switch]$Unicode,
        [switch]$ShowHidden
    )

    if ($Depth -lt 0) { return }

    # Runtime-safe Unicode characters
    if ($Unicode) {
        $CHAR_TEE  = [char]0x251C  # ├
        $CHAR_ELB  = [char]0x2514  # └
        $CHAR_VERT = [char]0x2502  # │
        $CHAR_HORZ = [char]0x2500  # ─
    }

    $gciParams = @{ Path = $Path }
    if ($ShowHidden) { $gciParams.Force = $true }

    # Sort folders first, then files
    $items = Get-ChildItem @gciParams |
        Sort-Object @{ Expression = 'PSIsContainer'; Descending = $true }, Name

    for ($i = 0; $i -lt $items.Count; $i++) {
        $item = $items[$i]

        if (-not $IncludeFiles -and -not $item.PSIsContainer) { continue }

        $isLast = ($i -eq $items.Count - 1)

        # Decide branch and indent safely
        if ($Unicode) {
            if ($isLast) {
                $branch = "$CHAR_ELB$CHAR_HORZ$CHAR_HORZ "
                $nextIndent = $Indent + "    "
            } else {
                $branch = "$CHAR_TEE$CHAR_HORZ$CHAR_HORZ "
                $nextIndent = $Indent + "$CHAR_VERT   "
            }
        }
        else {
            if ($isLast) {
                $branch = "|-- "
            } else {
                $branch = "|-- "
            }
            $nextIndent = $Indent + "    "
        }

        Write-Output "$Indent$branch$($item.Name)"

        if ($item.PSIsContainer) {
            Show-Tree `
                -Path $item.FullName `
                -Depth ($Depth - 1) `
                -Indent $nextIndent `
                -IncludeFiles:$IncludeFiles `
                -Unicode:$Unicode `
                -ShowHidden:$ShowHidden
        }
    }
}

```

## Add to PowerShell Profile

### Step 1: Open your Profile

Run this command to open your profile script in Notepad:

```PowerShell
notepad $PROFILE
```

!!!note
    If it says "the system cannot find the path specified," run `New-Item -Path $PROFILE -Type File -Force` first, then try the notepad command again.

### Step 2: Paste the Function

Copy and paste this code into the Notepad window and save it.

### Step 3: Refresh and Use

Close Notepad and refresh your session by running:

```PowerShell
. $PROFILE
```

Now you can use it anywhere just like a built-in command!

## Examples

### Folders only, Depth 1

```PowerShell
PS C:\Temp> Show-Tree -Depth 1 -Unicode
├── DCU
│   └── Logs
├── Dummy1
│   ├── Dummy1_1
│   ├── Dummy1_2
├── Dummy2
│   ├── Dummy2_1
│   ├── Dummy2_2

```

### Folders only, Depth 2

```PowerShell
PS C:\Temp> Show-Tree -Depth 2 -Unicode
├── DCU
│   └── Logs
├── Dummy1
│   ├── Dummy1_1
│   │   ├── Dummy1_1_1
│   ├── Dummy1_2
├── Dummy2
│   ├── Dummy2_1
│   │   ├── Dummy2_1_1
│   ├── Dummy2_2

```

### With Files, Depth 2

```PowerShell
PS C:\Temp> Show-Tree -Depth 2 -Unicode -IncludeFiles
├── DCU
│   └── Logs
│       ├── DCUApply.log
│       └── DCUScan.log
├── Dummy1
│   ├── Dummy1_1
│   │   ├── Dummy1_1_1
│   │   └── Dummy1_1_1.txt
│   ├── Dummy1_2
│   └── dummy1_1.txt
├── Dummy2
│   ├── Dummy2_1
│   │   ├── Dummy2_1_1
│   │   └── Dummy2_1_1.txt
│   ├── Dummy2_2
│   └── dummy2_1.txt
├── Dummy1.txt
└── Dummy2.txt

```

### Output to file

```PowerShell
PS C:\Temp> Show-Tree -Depth 2 -Unicode -IncludeFiles | Out-File tree.txt
```