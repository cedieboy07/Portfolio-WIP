# Charles' Spellbook

A menu-driven Python terminal application exploring skills, writings, programs, and featured works.

## Run the packaged application (Windows)

1. Open the project's `dist` folder.
2. Double-click `CharlesSpellbook.exe`, or run it from PowerShell:

   ```powershell
   .\dist\CharlesSpellbook.exe
   ```

The executable is built as a PyInstaller one-file application. The Python runtime, `pyfiglet`, and the JSON data files are bundled, so the recipient does not need Python or the source project installed. To distribute it, copy `dist\CharlesSpellbook.exe` to another compatible Windows computer. This executable is Windows-specific.

## Run from source (Windows)

Requirements: Python 3.14 (the version used to build the included executable) and an internet connection to install `pyfiglet`.

From the project root in PowerShell:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pyfiglet
python .\cover_page.py
```

Keep the project files and folders together, and run from the project root. The program uses modules under `assets` and `db_folder`, and reads its JSON data from `db_folder`.

## Build the Windows executable

Install PyInstaller in the activated virtual environment, then build using the repository's spec file:

```powershell
python -m pip install pyinstaller
pyinstaller --clean --noconfirm .\CharlesSpellbook.spec
```

The resulting executable is `dist\CharlesSpellbook.exe`. Rebuild after changing source code, the JSON data, or the spec file.

## Project layout

- `cover_page.py` — application entry point.
- `chap_1.py`, `chap_2.py`, `chap_3.py`, `final_chap.py`, `auth_info.py`, `ackno.py` — menu sections.
- `assets/` — terminal presentation helpers and ASCII banners.
- `db_folder/` — JSON content and its loading/display modules.
- `CharlesSpellbook.spec` — PyInstaller packaging configuration.
