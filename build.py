#!/usr/bin/env python3
"""Génère info.plist et empaquette Copy-Finder-Path.alfredworkflow.
Usage: ./build.py [--install]
"""
import os, plistlib, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Copy-Finder-Path.alfredworkflow")

# UIDs stables → réimport sans doublon, hotkey conservé
HK = "A1C0F1E0-0001-4A00-8000-C0F1DE20A7E5"
SC = "A1C0F1E0-0002-4A00-8000-C0F1DE20A7E5"
CB = "A1C0F1E0-0003-4A00-8000-C0F1DE20A7E5"
NT = "A1C0F1E0-0004-4A00-8000-C0F1DE20A7E5"

SCRIPT = r'''osascript -e 'tell application "Finder"
  set sel to selection as alias list
  if sel is {} then
    try
      set sel to {target of front Finder window as alias}
    on error
      return ""
    end try
  end if
  set out to ""
  repeat with f in sel
    set out to out & POSIX path of f & linefeed
  end repeat
  return text 1 thru -2 of out
end tell' | sed -E 's:(.)/$:\1:' | tr -d '\r'
'''

def conn(dst):
    return {"destinationuid": dst, "modifiers": 0, "modifiersubtext": "", "vitoclose": False}

WORKFLOW = {
    "bundleid": "dev.gotan.alfred.copyfinderpath",
    "category": "Productivity",
    "createdby": "Damien",
    "description": "Copie le chemin POSIX complet de la sélection Finder dans le presse-papiers",
    "name": "Copy Finder Path",
    "readme": ("Sélectionne un ou plusieurs éléments dans le Finder puis presse le hotkey.\n"
               "Sans sélection : le dossier de la fenêtre Finder active est copié.\n"
               "Plusieurs éléments = un chemin par ligne.\n\n"
               "Hotkey par défaut : ⇧⌘C (modifiable en double-cliquant sur le déclencheur)."),
    "version": "1.0",
    "webaddress": "https://gotan.dev",
    "objects": [
        {"type": "alfred.workflow.trigger.hotkey", "uid": HK, "version": 2,
         "config": {"action": 0, "argument": 1, "focusedappvariable": False, "focusedappvariablename": "",
                    # ⇧⌘C : keycode 8 = C, hotmod = Cmd (0x100000) | Shift (0x20000)
                    "hotkey": 8, "hotmod": 1179648, "hotstring": "C", "leftcursor": False,
                    "modsmode": 0, "relatedAppsMode": 0}},
        {"type": "alfred.workflow.action.script", "uid": SC, "version": 2,
         "config": {"concurrently": False, "escaping": 0, "script": SCRIPT,
                    "scriptargtype": 1, "scriptfile": "", "type": 0}},
        {"type": "alfred.workflow.output.clipboard", "uid": CB, "version": 3,
         "config": {"autopaste": False, "clipboardtext": "{query}",
                    "ignoredynamicplaceholders": False, "transient": False}},
        {"type": "alfred.workflow.output.notification", "uid": NT, "version": 1,
         "config": {"lastpathcomponent": False, "onlyshowifquerypopulated": True,
                    "removeextension": False, "text": "{query}", "title": "Chemin copié"}},
    ],
    "connections": {HK: [conn(SC)], SC: [conn(CB), conn(NT)]},
    "uidata": {HK: {"xpos": 50, "ypos": 100}, SC: {"xpos": 250, "ypos": 100},
               CB: {"xpos": 450, "ypos": 40}, NT: {"xpos": 450, "ypos": 170}},
}

if __name__ == "__main__":
    plist = os.path.join(HERE, "info.plist")
    with open(plist, "wb") as f:
        plistlib.dump(WORKFLOW, f)
    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(plist, "info.plist")
    print(f"→ {os.path.basename(OUT)}")
    if "--install" in sys.argv:
        subprocess.run(["open", OUT], check=True)
