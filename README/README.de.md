<img src="../icon.png" width="128" align="right" alt="Copy Finder Path icon">

# Copy Finder Path — [Alfred](https://www.alfredapp.com) Workflow

← [Zurück zur Übersicht](../README.md)

**Ein Hotkey. Der vollständige Pfad deiner Finder-Auswahl, direkt in der Zwischenablage.**

Kein Rechtsklick → ⌥ halten → „Als Pfadname kopieren“ suchen mehr. Auswählen, **⇧⌘C** drücken, einfügen.

<img src="../screenshots/usage.png" width="640" alt="Finder-Auswahl in die Zwischenablage kopiert">

## ✨ Was es tut

- **Ein Element** → kopiert den absoluten Pfad, z. B. `/Users/you/Projects/report.pdf`
- **Mehrere Elemente** → ein Pfad pro Zeile, bereit für ein Skript oder das Terminal
- **Nichts ausgewählt** → kopiert den Ordner des vordersten Finder-Fensters (praktisch für ein schnelles `cd`)
- **Saubere Ausgabe** → kein abschließendes `/` bei Ordnern
- **Sofortiges Feedback** → eine Mitteilung zeigt, was kopiert wurde – in deiner macOS-Sprache (Englisch, Französisch, Deutsch, Spanisch, Italienisch, Portugiesisch, Japanisch, Chinesisch, Griechisch)

## 🚀 Installation

1. `Copy-Finder-Path.alfredworkflow` herunterladen und doppelklicken
2. Standard-Hotkey ist **⇧⌘C** – zum Ändern den Hotkey-Block in Alfred doppelklicken
3. Beim ersten Einsatz Alfred erlauben, den Finder zu steuern, wenn macOS fragt (Systemeinstellungen → Datenschutz & Sicherheit → Automation)

Benötigt [Alfred 5](https://www.alfredapp.com) mit [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 oder neuer.

## 🔧 So funktioniert es

<img src="../screenshots/settings.png" width="640" alt="Workflow-Canvas in Alfred">

Ein AppleScript fragt den Finder nach der Auswahl, ein paar Zeilen Bash bereinigen die Pfade, und Alfred legt das Ergebnis in die Zwischenablage. Keine Abhängigkeiten – läuft auf jedem Standard-macOS.

Der Workflow stellt außerdem einen [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) namens `copy-path` bereit, um ihn von überall auszulösen:

```applescript
tell application id "com.runningwithcrayons.Alfred" to run trigger "copy-path" in workflow "dev.gotan.alfred.copyfinderpath"
```

## 🛠 Entwicklung

Der gesamte Workflow steckt in `build.py` – `info.plist` und das `.alfredworkflow`-Bundle werden daraus erzeugt.

```bash
./build.py            # info.plist + Copy-Finder-Path.alfredworkflow neu erzeugen
./build.py --install  # …und in Alfred öffnen
./make_icon.py        # icon.png neu erzeugen
```

Die UIDs sind stabil, ein erneuter Import aktualisiert den bestehenden Workflow an Ort und Stelle.

**Unter der Haube** gibt der Run-Script-Block [Alfred-JSON](https://www.alfredapp.com/help/workflows/utilities/json/) aus: `{"alfredworkflow":{"arg":"<paths>","variables":{"title":"<localized title>"}}}`. `arg` füllt die Zwischenablage, `title` (aus `AppleLanguages` gewählt) die Mitteilung über `{var:title}`. Beschreibung und Readme des Workflows sind statische Metadaten und bleiben auf Englisch.

**Ideen / einfache Anpassungen**

- Shell-escapte Pfade (`Mein\ Ordner`): das letzte `sed` durch `sed -E 's/([ ()&])/\\\1/g'` ersetzen
- `file://`-URLs oder Pfade relativ zu `$HOME` (`~/…`)
- Traditionelles Chinesisch für `zh-TW` / `zh-HK` über die vollständige Locale

## 📚 Referenzen

- [Alfred](https://www.alfredapp.com) · [Powerpack](https://www.alfredapp.com/powerpack/) · [Alfred Gallery](https://alfred.app)
- [Workflow-Dokumentation](https://www.alfredapp.com/help/workflows/) — [Hotkey](https://www.alfredapp.com/help/workflows/triggers/hotkey/), [Run Script](https://www.alfredapp.com/help/workflows/actions/run-script/), [Copy to Clipboard](https://www.alfredapp.com/help/workflows/outputs/copy-to-clipboard/), [Post Notification](https://www.alfredapp.com/help/workflows/outputs/post-notification/)
- [Workflow-Variablen](https://www.alfredapp.com/help/workflows/advanced/variables/) — `{var:title}`
- [Alfred Community Forum](https://www.alfredforum.com)

## 📄 Lizenz

MIT.

---

Erstellt von <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues und PRs willkommen
