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
EX = "A1C0F1E0-0005-4A00-8000-C0F1DE20A7E5"

SCRIPT = r"""# 1. Selected paths from Finder (fallback: front window folder)
paths=$(osascript -e 'tell application "Finder"
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
end tell' | sed -E 's:(.)/$:\1:' | tr -d '\r')

# 2. Notification title in the OS language
lang=$(defaults read -g AppleLanguages 2>/dev/null | sed -n 's/^ *"\([a-z][a-z]\).*/\1/p' | head -1)
case "$lang" in
  fr) title="Chemin copié" ;;
  it) title="Percorso copiato" ;;
  de) title="Pfad kopiert" ;;
  pt) title="Caminho copiado" ;;
  es) title="Ruta copiada" ;;
  ja) title="パスをコピーしました" ;;
  zh) title="路径已复制" ;;
  el) title="Η διαδρομή αντιγράφηκε" ;;
  *)  title="Path copied" ;;
esac

# 3. JSON for Alfred: arg = paths, variable title = localized
esc() { printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' | awk '{printf "%s%s", (NR>1?"\\n":""), $0}'; }
printf '{"alfredworkflow":{"arg":"%s","variables":{"title":"%s"}}}' "$(esc "$paths")" "$(esc "$title")"
"""

def conn(dst):
    return {"destinationuid": dst, "modifiers": 0, "modifiersubtext": "", "vitoclose": False}

WORKFLOW = {
    "bundleid": "dev.gotan.alfred.copyfinderpath",
    "category": "Productivity",
    "createdby": "Damien",
    "description": "Copy the full POSIX path of the Finder selection to the clipboard",
    "name": "Copy Finder Path",
    "readme": ("Select one or more items in Finder, then press the hotkey.\n"
               "No selection: the folder of the frontmost Finder window is copied.\n"
               "Multiple items: one path per line.\n\n"
               "Default hotkey: ⇧⌘C (double-click the Hotkey trigger to change it).\n"
               "The notification title follows your macOS language."),
    "version": "1.0",
    "webaddress": "https://gotan.dev",
    "objects": [
        {"type": "alfred.workflow.trigger.hotkey", "uid": HK, "version": 2,
         "config": {"action": 0, "argument": 0, "focusedappvariable": False, "focusedappvariablename": "",
                    # ⇧⌘C : keycode 8 = C, hotmod = Cmd (0x100000) | Shift (0x20000)
                    "hotkey": 8, "hotmod": 1179648, "hotstring": "C", "leftcursor": False,
                    "modsmode": 0, "relatedAppsMode": 0}},
        {"type": "alfred.workflow.trigger.external", "uid": EX, "version": 1,
         "config": {"triggerid": "copy-path"}},
        {"type": "alfred.workflow.action.script", "uid": SC, "version": 2,
         "config": {"concurrently": False, "escaping": 0, "script": SCRIPT,
                    "scriptargtype": 1, "scriptfile": "", "type": 0}},
        {"type": "alfred.workflow.output.clipboard", "uid": CB, "version": 3,
         "config": {"autopaste": False, "clipboardtext": "{query}",
                    "ignoredynamicplaceholders": False, "transient": False}},
        {"type": "alfred.workflow.output.notification", "uid": NT, "version": 1,
         "config": {"lastpathcomponent": False, "onlyshowifquerypopulated": True,
                    "removeextension": False, "text": "{query}", "title": "{var:title}"}},
    ],
    "connections": {HK: [conn(SC)], EX: [conn(SC)], SC: [conn(CB), conn(NT)]},
    "uidata": {HK: {"xpos": 50, "ypos": 40}, EX: {"xpos": 50, "ypos": 170}, SC: {"xpos": 250, "ypos": 100},
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
        icon = os.path.join(HERE, "icon.png")
        if os.path.exists(icon):
            z.write(icon, "icon.png")
    print(f"→ {os.path.basename(OUT)}")
    if "--install" in sys.argv:
        subprocess.run(["open", OUT], check=True)
