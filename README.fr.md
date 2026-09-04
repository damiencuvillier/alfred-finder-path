<a href="dist/Copy-Finder-Path.alfredworkflow?raw=true"><img src="assets/download/fr.png" width="240" align="right" alt="Télécharger le workflow"></a>

<table>
  <tr><td align="center"><a href="README.md"><img src="assets/flags/en.png" width="40" alt="English"></a><br><a href="README.md"><sub>English</sub></a></td><td align="center"><a href="README.de.md"><img src="assets/flags/de.png" width="40" alt="Deutsch"></a><br><a href="README.de.md"><sub>Deutsch</sub></a></td><td align="center"><a href="README.es.md"><img src="assets/flags/es.png" width="40" alt="Español"></a><br><a href="README.es.md"><sub>Español</sub></a></td><td align="center"><a href="README.it.md"><img src="assets/flags/it.png" width="40" alt="Italiano"></a><br><a href="README.it.md"><sub>Italiano</sub></a></td><td align="center"><a href="README.pt.md"><img src="assets/flags/pt.png" width="40" alt="Português"></a><br><a href="README.pt.md"><sub>Português</sub></a></td><td align="center"><a href="README.ja.md"><img src="assets/flags/ja.png" width="40" alt="日本語"></a><br><a href="README.ja.md"><sub>日本語</sub></a></td><td align="center"><a href="README.zh.md"><img src="assets/flags/zh.png" width="40" alt="中文"></a><br><a href="README.zh.md"><sub>中文</sub></a></td><td align="center"><a href="README.el.md"><img src="assets/flags/el.png" width="40" alt="Ελληνικά"></a><br><a href="README.el.md"><sub>Ελληνικά</sub></a></td></tr>
</table>

###### ALFRED WORKFLOW
# Copier le chemin complet depuis le Finder

**Un raccourci. Le chemin complet de ce que vous avez sélectionné dans le Finder, directement dans le presse-papiers.**

Fini le clic droit → maintenir ⌥ → chercher « Copier en tant que chemin ». Sélectionnez, pressez **⇧⌘C**, collez.

<img src="screenshots/usage.png" width="640" alt="Sélection Finder copiée dans le presse-papiers">

## ✨ Ce que ça fait

- **Un élément** → copie son chemin absolu, ex. `/Users/you/Projects/report.pdf`
- **Plusieurs éléments** → un chemin par ligne, prêt pour un script ou un terminal
- **Aucune sélection** → copie le dossier de la fenêtre Finder active (pratique pour un `cd` rapide)
- **Sortie propre** → pas de `/` final sur les dossiers
- **Retour immédiat** → une notification affiche ce qui a été copié, dans la langue de votre macOS (anglais, français, allemand, espagnol, italien, portugais, japonais, chinois, grec)

## 🚀 Installation

1. Téléchargez `Copy-Finder-Path.alfredworkflow` et double-cliquez dessus
2. Le raccourci par défaut est **⇧⌘C** — double-cliquez sur le bloc Hotkey dans Alfred pour le changer
3. À la première utilisation, autorisez Alfred à contrôler le Finder quand macOS le demande (Réglages Système → Confidentialité et sécurité → Automatisation)

Nécessite [Alfred 5](https://www.alfredapp.com) avec le [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 ou plus récent.

## 🔧 Comment ça marche

<img src="screenshots/settings.png" width="640" alt="Canvas du workflow dans Alfred">

Un AppleScript demande au Finder sa sélection, quelques lignes de bash nettoient les chemins, et Alfred place le résultat dans le presse-papiers. Aucune dépendance — fonctionne sur un macOS standard.

Le workflow expose aussi un [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) nommé `copy-path`, pour le déclencher depuis n'importe où :

```applescript
tell application id "com.runningwithcrayons.Alfred" to run trigger "copy-path" in workflow "dev.gotan.alfred.copyfinderpath"
```

## 🛠 Développement

Tout le workflow tient dans `tools/build.py` — `workflow/info.plist` et le bundle `dist/Copy-Finder-Path.alfredworkflow` en sont générés.

```bash
tools/build.py            # régénère workflow/info.plist + dist/*.alfredworkflow
tools/build.py --install  # …et l'ouvre dans Alfred
tools/make-icon.py        # régénère workflow/icon.png
tools/make-readmes.py     # régénère tous les README
```

Les UIDs sont stables : réimporter met à jour le workflow existant sur place.

**Sous le capot**, le bloc Run Script émet du [JSON Alfred](https://www.alfredapp.com/help/workflows/utilities/json/) : `{"alfredworkflow":{"arg":"<paths>","variables":{"title":"<localized title>"}}}`. `arg` alimente le presse-papiers, `title` (choisi d'après `AppleLanguages`) alimente la notification via `{var:title}`. La description et le readme du workflow sont des métadonnées statiques et restent en anglais.

**Idées / variantes faciles**

- Chemins échappés pour le shell (`Mon\ Dossier`) : remplacer le `sed` final par `sed -E 's/([ ()&])/\\\1/g'`
- URLs `file://`, ou chemins relatifs à `$HOME` (`~/…`)
- Chinois traditionnel pour `zh-TW` / `zh-HK` en testant la locale complète

## 📚 Références

- [Alfred](https://www.alfredapp.com) · [Powerpack](https://www.alfredapp.com/powerpack/) · [Alfred Gallery](https://alfred.app)
- [Documentation des workflows](https://www.alfredapp.com/help/workflows/) — [Hotkey](https://www.alfredapp.com/help/workflows/triggers/hotkey/), [Run Script](https://www.alfredapp.com/help/workflows/actions/run-script/), [Copy to Clipboard](https://www.alfredapp.com/help/workflows/outputs/copy-to-clipboard/), [Post Notification](https://www.alfredapp.com/help/workflows/outputs/post-notification/)
- [Variables de workflow](https://www.alfredapp.com/help/workflows/advanced/variables/) — `{var:title}`
- [Forum de la communauté Alfred](https://www.alfredforum.com)

## 📄 Licence

MIT.

---

Réalisé par <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues et PRs bienvenues
