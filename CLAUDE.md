# alfred-path — Copy Finder Path (workflow Alfred)

Hotkey → copie le chemin POSIX complet de la sélection Finder dans le presse-papiers.
Multi-sélection = un chemin par ligne. Sans sélection = dossier de la fenêtre Finder active.
Le `/` final des dossiers est retiré.

## Fichiers
- `build.py` — source unique : génère `info.plist` et zippe `Copy-Finder-Path.alfredworkflow`
  - `./build.py --install` ouvre le workflow dans Alfred (réimport idempotent, UIDs stables)
- `info.plist` / `*.alfredworkflow` — générés, ignorés par git

## Structure du workflow
Hotkey (sans argument) → Run Script bash (osascript sur le Finder) → Copy to Clipboard + Notification

## Après import
- Assigner le hotkey (double-clic sur le bloc Hotkey). Éviter ⌥⌘C, déjà natif Finder.
- Autoriser Alfred à contrôler le Finder (Réglages → Confidentialité → Automatisation).

## Idées
- Variante chemin échappé shell : `sed -E 's/([ ()&])/\\\1/g'` à la place du sed final
- Variante `file://` URL ou chemin relatif à `$HOME`
