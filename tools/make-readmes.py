#!/usr/bin/env python3
# Generates README.md (English) and README.<lang>.md at the repo root
# from the translations below. Each file shows the 8 *other* languages as a flag row.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import LANGS as _L, TITLE, DEFAULT
LANGS = [(c, f, n) for c, f, n, *_ in _L]
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT, exist_ok=True)

def fname(code):
    return "README.md" if code == DEFAULT else f"README.{code}.md"

def nav(current):
    cells = "".join(
        f'<td align="center"><a href="{fname(c)}"><img src="assets/flags/{c}.png" width="40" alt="{n}"></a><br>'
        f'<a href="{fname(c)}"><sub>{n}</sub></a></td>'
        for c, _, n in LANGS if c != current)
    return f"<table>\n  <tr>{cells}</tr>\n</table>"

TRIGGER = 'tell application id "com.runningwithcrayons.Alfred" to run trigger "copy-path" in workflow "dev.gotan.alfred.copyfinderpath"'
JSON = '`{"alfredworkflow":{"arg":"<paths>","variables":{"title":"<localized title>"}}}`'

TEMPLATE = """<a href="dist/Copy-Finder-Path.alfredworkflow?raw=true"><img src="assets/download/{code}.png" width="240" align="right" alt="{btn_alt}"></a>

{nav}

###### ALFRED WORKFLOW
# {title}

**{pitch}**

{tagline}

<img src="screenshots/usage.png" width="640" alt="{alt_usage}">

## ✨ {h_what}

- **{single_t}** → {single_d} `/Users/you/Projects/report.pdf`
- **{multi_t}** → {multi_d}
- **{none_t}** → {none_d}
- **{clean_t}** → {clean_d}
- **{notif_t}** → {notif_d}

## 🚀 {h_install}

1. {inst1}
2. {inst2}
3. {inst3}

{requires}

## 🔧 {h_how}

<img src="screenshots/settings.png" width="640" alt="{alt_settings}">

{how_p}

{trigger_p}

```applescript
{trigger}
```

## 🛠 {h_dev}

{dev_p}

```bash
tools/build.py            # {c1}
tools/build.py --install  # {c2}
tools/make-icon.py        # {c3}
tools/make-readmes.py     # {c4}
```

{uids}

{hood}

**{h_ideas}**

- {idea1}
- {idea2}
- {idea3}

## 📚 {h_refs}

- [Alfred](https://www.alfredapp.com) · [Powerpack](https://www.alfredapp.com/powerpack/) · [Alfred Gallery](https://alfred.app)
- [{ref_docs}](https://www.alfredapp.com/help/workflows/) — [Hotkey](https://www.alfredapp.com/help/workflows/triggers/hotkey/), [Run Script](https://www.alfredapp.com/help/workflows/actions/run-script/), [Copy to Clipboard](https://www.alfredapp.com/help/workflows/outputs/copy-to-clipboard/), [Post Notification](https://www.alfredapp.com/help/workflows/outputs/post-notification/)
- [{ref_vars}](https://www.alfredapp.com/help/workflows/advanced/variables/) — `{{var:title}}`
- [{ref_forum}](https://www.alfredforum.com)

## 📄 {h_license}

MIT.

---

{footer}
"""

T = {}
T["en"] = dict(
 btn_alt="Download the workflow",
 pitch="One hotkey. The full path of whatever you have selected in Finder, straight to your clipboard.",
 tagline='No more right-click → hold ⌥ → hunt for "Copy as Pathname". Select, press **⇧⌘C**, paste.',
 alt_usage="Finder selection copied to clipboard", alt_settings="Workflow canvas in Alfred",
 h_what="What it does",
 single_t="Single item", single_d="copies its absolute path, e.g.",
 multi_t="Multiple items", multi_d="one path per line, ready for a script or a terminal",
 none_t="Nothing selected", none_d="copies the folder of the frontmost Finder window (handy for a quick `cd`)",
 clean_t="Clean output", clean_d="no trailing `/` on folders",
 notif_t="Instant feedback", notif_d="a notification shows what was copied, in your macOS language (English, French, German, Spanish, Italian, Portuguese, Japanese, Chinese, Greek)",
 h_install="Install",
 inst1="Download `Copy-Finder-Path.alfredworkflow` and double-click it",
 inst2="Default hotkey is **⇧⌘C** — double-click the Hotkey block in Alfred to change it",
 inst3="On first use, allow Alfred to control Finder when macOS asks (System Settings → Privacy & Security → Automation)",
 requires="Requires [Alfred 5](https://www.alfredapp.com) with the [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 or later.",
 h_how="How it works",
 how_p="An AppleScript asks Finder for its selection, a few lines of bash tidy the paths up, and Alfred puts the result on the clipboard. No dependencies — runs on a stock macOS install.",
 trigger_p="The workflow also exposes an [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) named `copy-path`, so you can fire it from anywhere:",
 h_dev="Development",
 dev_p="The whole workflow lives in `tools/build.py` — `workflow/info.plist` and `dist/Copy-Finder-Path.alfredworkflow` are generated from it.",
 c1="regenerate workflow/info.plist + dist/*.alfredworkflow", c2="…and open it in Alfred", c3="regenerate workflow/icon.png", c4="regenerate all README files",
 uids="UIDs are stable, so re-importing updates the existing workflow in place.",
 hood=f"**Under the hood**, the Run Script block emits [Alfred's JSON format](https://www.alfredapp.com/help/workflows/utilities/json/): {JSON}. `arg` feeds the clipboard, `title` (picked from `AppleLanguages`) feeds the notification via `{{var:title}}`. The workflow description and readme are static metadata and stay in English.",
 h_ideas="Ideas / easy tweaks",
 idea1="Shell-escaped paths (`My\\ Folder`): swap the final `sed` for `sed -E 's/([ ()&])/\\\\\\1/g'`",
 idea2="`file://` URLs, or paths relative to `$HOME` (`~/…`)",
 idea3="Traditional Chinese for `zh-TW` / `zh-HK` by matching the full locale",
 h_refs="References", ref_docs="Workflows documentation", ref_vars="Workflow variables", ref_forum="Alfred Community Forum",
 h_license="License",
 footer="Made by <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues and PRs welcome",
)

T["fr"] = dict(
 btn_alt="Télécharger le workflow",
 pitch="Un raccourci. Le chemin complet de ce que vous avez sélectionné dans le Finder, directement dans le presse-papiers.",
 tagline="Fini le clic droit → maintenir ⌥ → chercher « Copier en tant que chemin ». Sélectionnez, pressez **⇧⌘C**, collez.",
 alt_usage="Sélection Finder copiée dans le presse-papiers", alt_settings="Canvas du workflow dans Alfred",
 h_what="Ce que ça fait",
 single_t="Un élément", single_d="copie son chemin absolu, ex.",
 multi_t="Plusieurs éléments", multi_d="un chemin par ligne, prêt pour un script ou un terminal",
 none_t="Aucune sélection", none_d="copie le dossier de la fenêtre Finder active (pratique pour un `cd` rapide)",
 clean_t="Sortie propre", clean_d="pas de `/` final sur les dossiers",
 notif_t="Retour immédiat", notif_d="une notification affiche ce qui a été copié, dans la langue de votre macOS (anglais, français, allemand, espagnol, italien, portugais, japonais, chinois, grec)",
 h_install="Installation",
 inst1="Téléchargez `Copy-Finder-Path.alfredworkflow` et double-cliquez dessus",
 inst2="Le raccourci par défaut est **⇧⌘C** — double-cliquez sur le bloc Hotkey dans Alfred pour le changer",
 inst3="À la première utilisation, autorisez Alfred à contrôler le Finder quand macOS le demande (Réglages Système → Confidentialité et sécurité → Automatisation)",
 requires="Nécessite [Alfred 5](https://www.alfredapp.com) avec le [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 ou plus récent.",
 h_how="Comment ça marche",
 how_p="Un AppleScript demande au Finder sa sélection, quelques lignes de bash nettoient les chemins, et Alfred place le résultat dans le presse-papiers. Aucune dépendance — fonctionne sur un macOS standard.",
 trigger_p="Le workflow expose aussi un [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) nommé `copy-path`, pour le déclencher depuis n'importe où :",
 h_dev="Développement",
 dev_p="Tout le workflow tient dans `tools/build.py` — `workflow/info.plist` et le bundle `dist/Copy-Finder-Path.alfredworkflow` en sont générés.",
 c1="régénère workflow/info.plist + dist/*.alfredworkflow", c2="…et l'ouvre dans Alfred", c3="régénère workflow/icon.png", c4="régénère tous les README",
 uids="Les UIDs sont stables : réimporter met à jour le workflow existant sur place.",
 hood=f"**Sous le capot**, le bloc Run Script émet du [JSON Alfred](https://www.alfredapp.com/help/workflows/utilities/json/) : {JSON}. `arg` alimente le presse-papiers, `title` (choisi d'après `AppleLanguages`) alimente la notification via `{{var:title}}`. La description et le readme du workflow sont des métadonnées statiques et restent en anglais.",
 h_ideas="Idées / variantes faciles",
 idea1="Chemins échappés pour le shell (`Mon\\ Dossier`) : remplacer le `sed` final par `sed -E 's/([ ()&])/\\\\\\1/g'`",
 idea2="URLs `file://`, ou chemins relatifs à `$HOME` (`~/…`)",
 idea3="Chinois traditionnel pour `zh-TW` / `zh-HK` en testant la locale complète",
 h_refs="Références", ref_docs="Documentation des workflows", ref_vars="Variables de workflow", ref_forum="Forum de la communauté Alfred",
 h_license="Licence",
 footer="Réalisé par <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues et PRs bienvenues",
)

T["de"] = dict(
 btn_alt="Workflow herunterladen",
 pitch="Ein Hotkey. Der vollständige Pfad deiner Finder-Auswahl, direkt in der Zwischenablage.",
 tagline="Kein Rechtsklick → ⌥ halten → „Als Pfadname kopieren“ suchen mehr. Auswählen, **⇧⌘C** drücken, einfügen.",
 alt_usage="Finder-Auswahl in die Zwischenablage kopiert", alt_settings="Workflow-Canvas in Alfred",
 h_what="Was es tut",
 single_t="Ein Element", single_d="kopiert den absoluten Pfad, z. B.",
 multi_t="Mehrere Elemente", multi_d="ein Pfad pro Zeile, bereit für ein Skript oder das Terminal",
 none_t="Nichts ausgewählt", none_d="kopiert den Ordner des vordersten Finder-Fensters (praktisch für ein schnelles `cd`)",
 clean_t="Saubere Ausgabe", clean_d="kein abschließendes `/` bei Ordnern",
 notif_t="Sofortiges Feedback", notif_d="eine Mitteilung zeigt, was kopiert wurde – in deiner macOS-Sprache (Englisch, Französisch, Deutsch, Spanisch, Italienisch, Portugiesisch, Japanisch, Chinesisch, Griechisch)",
 h_install="Installation",
 inst1="`Copy-Finder-Path.alfredworkflow` herunterladen und doppelklicken",
 inst2="Standard-Hotkey ist **⇧⌘C** – zum Ändern den Hotkey-Block in Alfred doppelklicken",
 inst3="Beim ersten Einsatz Alfred erlauben, den Finder zu steuern, wenn macOS fragt (Systemeinstellungen → Datenschutz & Sicherheit → Automation)",
 requires="Benötigt [Alfred 5](https://www.alfredapp.com) mit [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 oder neuer.",
 h_how="So funktioniert es",
 how_p="Ein AppleScript fragt den Finder nach der Auswahl, ein paar Zeilen Bash bereinigen die Pfade, und Alfred legt das Ergebnis in die Zwischenablage. Keine Abhängigkeiten – läuft auf jedem Standard-macOS.",
 trigger_p="Der Workflow stellt außerdem einen [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) namens `copy-path` bereit, um ihn von überall auszulösen:",
 h_dev="Entwicklung",
 dev_p="Der gesamte Workflow steckt in `tools/build.py` – `workflow/info.plist` und das `dist/Copy-Finder-Path.alfredworkflow`-Bundle werden daraus erzeugt.",
 c1="workflow/info.plist + dist/*.alfredworkflow neu erzeugen", c2="…und in Alfred öffnen", c3="workflow/icon.png neu erzeugen", c4="alle README-Dateien neu erzeugen",
 uids="Die UIDs sind stabil, ein erneuter Import aktualisiert den bestehenden Workflow an Ort und Stelle.",
 hood=f"**Unter der Haube** gibt der Run-Script-Block [Alfred-JSON](https://www.alfredapp.com/help/workflows/utilities/json/) aus: {JSON}. `arg` füllt die Zwischenablage, `title` (aus `AppleLanguages` gewählt) die Mitteilung über `{{var:title}}`. Beschreibung und Readme des Workflows sind statische Metadaten und bleiben auf Englisch.",
 h_ideas="Ideen / einfache Anpassungen",
 idea1="Shell-escapte Pfade (`Mein\\ Ordner`): das letzte `sed` durch `sed -E 's/([ ()&])/\\\\\\1/g'` ersetzen",
 idea2="`file://`-URLs oder Pfade relativ zu `$HOME` (`~/…`)",
 idea3="Traditionelles Chinesisch für `zh-TW` / `zh-HK` über die vollständige Locale",
 h_refs="Referenzen", ref_docs="Workflow-Dokumentation", ref_vars="Workflow-Variablen", ref_forum="Alfred Community Forum",
 h_license="Lizenz",
 footer="Erstellt von <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues und PRs willkommen",
)

T["es"] = dict(
 btn_alt="Descargar el workflow",
 pitch="Un atajo. La ruta completa de lo que tengas seleccionado en el Finder, directa al portapapeles.",
 tagline="Se acabó el clic derecho → mantener ⌥ → buscar «Copiar como nombre de ruta». Selecciona, pulsa **⇧⌘C**, pega.",
 alt_usage="Selección del Finder copiada al portapapeles", alt_settings="Lienzo del workflow en Alfred",
 h_what="Qué hace",
 single_t="Un elemento", single_d="copia su ruta absoluta, p. ej.",
 multi_t="Varios elementos", multi_d="una ruta por línea, lista para un script o el terminal",
 none_t="Sin selección", none_d="copia la carpeta de la ventana del Finder en primer plano (útil para un `cd` rápido)",
 clean_t="Salida limpia", clean_d="sin `/` final en las carpetas",
 notif_t="Respuesta inmediata", notif_d="una notificación muestra lo copiado, en el idioma de tu macOS (inglés, francés, alemán, español, italiano, portugués, japonés, chino, griego)",
 h_install="Instalación",
 inst1="Descarga `Copy-Finder-Path.alfredworkflow` y haz doble clic",
 inst2="El atajo por defecto es **⇧⌘C**; haz doble clic en el bloque Hotkey de Alfred para cambiarlo",
 inst3="La primera vez, permite que Alfred controle el Finder cuando macOS lo pida (Ajustes del Sistema → Privacidad y seguridad → Automatización)",
 requires="Requiere [Alfred 5](https://www.alfredapp.com) con el [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 o posterior.",
 h_how="Cómo funciona",
 how_p="Un AppleScript pide al Finder su selección, unas líneas de bash limpian las rutas y Alfred deja el resultado en el portapapeles. Sin dependencias: funciona en un macOS estándar.",
 trigger_p="El workflow también expone un [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) llamado `copy-path`, para lanzarlo desde cualquier sitio:",
 h_dev="Desarrollo",
 dev_p="Todo el workflow vive en `tools/build.py`: `workflow/info.plist` y el paquete `dist/Copy-Finder-Path.alfredworkflow` se generan a partir de él.",
 c1="regenera workflow/info.plist + dist/*.alfredworkflow", c2="…y lo abre en Alfred", c3="regenera workflow/icon.png", c4="regenera todos los README",
 uids="Los UIDs son estables, así que reimportar actualiza el workflow existente en su sitio.",
 hood=f"**Por dentro**, el bloque Run Script emite [JSON de Alfred](https://www.alfredapp.com/help/workflows/utilities/json/): {JSON}. `arg` alimenta el portapapeles y `title` (elegido según `AppleLanguages`) la notificación mediante `{{var:title}}`. La descripción y el readme del workflow son metadatos estáticos y se quedan en inglés.",
 h_ideas="Ideas / ajustes fáciles",
 idea1="Rutas escapadas para shell (`Mi\\ Carpeta`): sustituye el `sed` final por `sed -E 's/([ ()&])/\\\\\\1/g'`",
 idea2="URLs `file://`, o rutas relativas a `$HOME` (`~/…`)",
 idea3="Chino tradicional para `zh-TW` / `zh-HK` comprobando la locale completa",
 h_refs="Referencias", ref_docs="Documentación de workflows", ref_vars="Variables de workflow", ref_forum="Foro de la comunidad Alfred",
 h_license="Licencia",
 footer="Hecho por <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues y PRs bienvenidos",
)

T["it"] = dict(
 btn_alt="Scarica il workflow",
 pitch="Una scorciatoia. Il percorso completo di ciò che hai selezionato nel Finder, direttamente negli appunti.",
 tagline="Basta clic destro → tenere ⌥ → cercare «Copia come percorso». Seleziona, premi **⇧⌘C**, incolla.",
 alt_usage="Selezione del Finder copiata negli appunti", alt_settings="Canvas del workflow in Alfred",
 h_what="Cosa fa",
 single_t="Un elemento", single_d="copia il suo percorso assoluto, es.",
 multi_t="Più elementi", multi_d="un percorso per riga, pronto per uno script o il terminale",
 none_t="Nessuna selezione", none_d="copia la cartella della finestra Finder in primo piano (comodo per un `cd` al volo)",
 clean_t="Output pulito", clean_d="nessun `/` finale sulle cartelle",
 notif_t="Feedback immediato", notif_d="una notifica mostra cosa è stato copiato, nella lingua del tuo macOS (inglese, francese, tedesco, spagnolo, italiano, portoghese, giapponese, cinese, greco)",
 h_install="Installazione",
 inst1="Scarica `Copy-Finder-Path.alfredworkflow` e fai doppio clic",
 inst2="La scorciatoia predefinita è **⇧⌘C**: fai doppio clic sul blocco Hotkey in Alfred per cambiarla",
 inst3="Al primo utilizzo, consenti ad Alfred di controllare il Finder quando macOS lo chiede (Impostazioni di Sistema → Privacy e sicurezza → Automazione)",
 requires="Richiede [Alfred 5](https://www.alfredapp.com) con il [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 o successivo.",
 h_how="Come funziona",
 how_p="Un AppleScript chiede al Finder la selezione, poche righe di bash ripuliscono i percorsi e Alfred mette il risultato negli appunti. Nessuna dipendenza: funziona su un macOS standard.",
 trigger_p="Il workflow espone anche un [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) chiamato `copy-path`, per lanciarlo da qualsiasi punto:",
 h_dev="Sviluppo",
 dev_p="Tutto il workflow è in `tools/build.py`: `workflow/info.plist` e il bundle `dist/Copy-Finder-Path.alfredworkflow` vengono generati da lì.",
 c1="rigenera workflow/info.plist + dist/*.alfredworkflow", c2="…e lo apre in Alfred", c3="rigenera workflow/icon.png", c4="rigenera tutti i README",
 uids="Gli UID sono stabili, quindi reimportare aggiorna il workflow esistente sul posto.",
 hood=f"**Sotto il cofano**, il blocco Run Script emette [JSON Alfred](https://www.alfredapp.com/help/workflows/utilities/json/): {JSON}. `arg` alimenta gli appunti, `title` (scelto da `AppleLanguages`) alimenta la notifica tramite `{{var:title}}`. Descrizione e readme del workflow sono metadati statici e restano in inglese.",
 h_ideas="Idee / modifiche facili",
 idea1="Percorsi con escape per la shell (`Mia\\ Cartella`): sostituisci il `sed` finale con `sed -E 's/([ ()&])/\\\\\\1/g'`",
 idea2="URL `file://`, oppure percorsi relativi a `$HOME` (`~/…`)",
 idea3="Cinese tradizionale per `zh-TW` / `zh-HK` controllando la locale completa",
 h_refs="Riferimenti", ref_docs="Documentazione dei workflow", ref_vars="Variabili di workflow", ref_forum="Forum della community Alfred",
 h_license="Licenza",
 footer="Realizzato da <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issue e PR benvenute",
)

T["pt"] = dict(
 btn_alt="Descarregar o workflow",
 pitch="Um atalho. O caminho completo do que tiveres selecionado no Finder, direto para a área de transferência.",
 tagline="Acabou o clique direito → manter ⌥ → procurar «Copiar como nome de caminho». Seleciona, prime **⇧⌘C**, cola.",
 alt_usage="Seleção do Finder copiada para a área de transferência", alt_settings="Canvas do workflow no Alfred",
 h_what="O que faz",
 single_t="Um item", single_d="copia o seu caminho absoluto, p. ex.",
 multi_t="Vários itens", multi_d="um caminho por linha, pronto para um script ou o terminal",
 none_t="Sem seleção", none_d="copia a pasta da janela do Finder em primeiro plano (útil para um `cd` rápido)",
 clean_t="Saída limpa", clean_d="sem `/` final nas pastas",
 notif_t="Feedback imediato", notif_d="uma notificação mostra o que foi copiado, no idioma do teu macOS (inglês, francês, alemão, espanhol, italiano, português, japonês, chinês, grego)",
 h_install="Instalação",
 inst1="Descarrega `Copy-Finder-Path.alfredworkflow` e faz duplo clique",
 inst2="O atalho predefinido é **⇧⌘C** — faz duplo clique no bloco Hotkey no Alfred para o alterar",
 inst3="Na primeira utilização, permite que o Alfred controle o Finder quando o macOS pedir (Definições do Sistema → Privacidade e Segurança → Automatização)",
 requires="Requer [Alfred 5](https://www.alfredapp.com) com o [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 ou posterior.",
 h_how="Como funciona",
 how_p="Um AppleScript pede ao Finder a seleção, algumas linhas de bash limpam os caminhos e o Alfred coloca o resultado na área de transferência. Sem dependências — funciona num macOS de origem.",
 trigger_p="O workflow expõe também um [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) chamado `copy-path`, para o disparar de qualquer lado:",
 h_dev="Desenvolvimento",
 dev_p="Todo o workflow vive em `tools/build.py` — o `workflow/info.plist` e o pacote `dist/Copy-Finder-Path.alfredworkflow` são gerados a partir dele.",
 c1="regenera workflow/info.plist + dist/*.alfredworkflow", c2="…e abre-o no Alfred", c3="regenera workflow/icon.png", c4="regenera todos os README",
 uids="Os UIDs são estáveis, por isso reimportar atualiza o workflow existente no lugar.",
 hood=f"**Por baixo do capô**, o bloco Run Script emite [JSON do Alfred](https://www.alfredapp.com/help/workflows/utilities/json/): {JSON}. `arg` alimenta a área de transferência, `title` (escolhido a partir de `AppleLanguages`) alimenta a notificação via `{{var:title}}`. A descrição e o readme do workflow são metadados estáticos e ficam em inglês.",
 h_ideas="Ideias / ajustes fáceis",
 idea1="Caminhos com escape para a shell (`Minha\\ Pasta`): troca o `sed` final por `sed -E 's/([ ()&])/\\\\\\1/g'`",
 idea2="URLs `file://`, ou caminhos relativos a `$HOME` (`~/…`)",
 idea3="Chinês tradicional para `zh-TW` / `zh-HK` verificando a locale completa",
 h_refs="Referências", ref_docs="Documentação de workflows", ref_vars="Variáveis de workflow", ref_forum="Fórum da comunidade Alfred",
 h_license="Licença",
 footer="Feito por <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues e PRs bem-vindos",
)

T["ja"] = dict(
 btn_alt="ワークフローをダウンロード",
 pitch="ホットキーひとつ。Finder で選択した項目のフルパスを、そのままクリップボードへ。",
 tagline="右クリック → ⌥ を押しながら → 「パス名をコピー」を探す、はもう不要。選択して **⇧⌘C**、貼り付けるだけ。",
 alt_usage="Finder の選択項目がクリップボードにコピーされた様子", alt_settings="Alfred のワークフローキャンバス",
 h_what="できること",
 single_t="1 項目", single_d="絶対パスをコピーします。例：",
 multi_t="複数項目", multi_d="1 行に 1 パス。スクリプトやターミナルにそのまま貼れます",
 none_t="選択なし", none_d="最前面の Finder ウインドウのフォルダをコピー（サッと `cd` するのに便利）",
 clean_t="きれいな出力", clean_d="フォルダ末尾の `/` は付きません",
 notif_t="すぐにフィードバック", notif_d="コピーした内容を通知で表示。macOS の言語に合わせます（英語・フランス語・ドイツ語・スペイン語・イタリア語・ポルトガル語・日本語・中国語・ギリシャ語）",
 h_install="インストール",
 inst1="`Copy-Finder-Path.alfredworkflow` をダウンロードしてダブルクリック",
 inst2="デフォルトのホットキーは **⇧⌘C**。変更は Alfred の Hotkey ブロックをダブルクリック",
 inst3="初回使用時、macOS の確認で Alfred による Finder の制御を許可（システム設定 → プライバシーとセキュリティ → オートメーション）",
 requires="[Alfred 5](https://www.alfredapp.com) と [Powerpack](https://www.alfredapp.com/powerpack/)、macOS 12 以降が必要です。",
 h_how="仕組み",
 how_p="AppleScript が Finder に選択項目を問い合わせ、数行の bash がパスを整え、Alfred が結果をクリップボードに入れます。依存なし。素の macOS で動きます。",
 trigger_p="`copy-path` という名前の [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) も用意しているので、どこからでも呼び出せます：",
 h_dev="開発",
 dev_p="ワークフロー全体は `tools/build.py` にあります。`workflow/info.plist` と `dist/Copy-Finder-Path.alfredworkflow` バンドルはそこから生成されます。",
 c1="workflow/info.plist + dist/*.alfredworkflow を再生成", c2="…さらに Alfred で開く", c3="workflow/icon.png を再生成", c4="README をすべて再生成",
 uids="UID は固定なので、再インポートすると既存のワークフローがその場で更新されます。",
 hood=f"**内部では**、Run Script ブロックが [Alfred の JSON 形式](https://www.alfredapp.com/help/workflows/utilities/json/)を出力します：{JSON}。`arg` はクリップボードへ、`title`（`AppleLanguages` から選択）は `{{var:title}}` 経由で通知へ渡されます。ワークフローの説明と readme は静的なメタデータのため英語のままです。",
 h_ideas="アイデア / 簡単なカスタマイズ",
 idea1="シェル用にエスケープしたパス（`My\\ Folder`）：最後の `sed` を `sed -E 's/([ ()&])/\\\\\\1/g'` に置き換え",
 idea2="`file://` URL、または `$HOME` からの相対パス（`~/…`）",
 idea3="`zh-TW` / `zh-HK` はロケール全体を判定して繁体字中国語に",
 h_refs="参考リンク", ref_docs="ワークフローのドキュメント", ref_vars="ワークフロー変数", ref_forum="Alfred コミュニティフォーラム",
 h_license="ライセンス",
 footer="作者：<a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issue や PR を歓迎します",
)

T["zh"] = dict(
 btn_alt="下载工作流",
 pitch="一个快捷键，把 Finder 中所选项目的完整路径直接送进剪贴板。",
 tagline="不用再右键 → 按住 ⌥ → 找“拷贝为路径名称”。选中，按 **⇧⌘C**，粘贴。",
 alt_usage="Finder 选中项已复制到剪贴板", alt_settings="Alfred 中的工作流画布",
 h_what="功能",
 single_t="单个项目", single_d="复制其绝对路径，例如",
 multi_t="多个项目", multi_d="每行一个路径，可直接用于脚本或终端",
 none_t="未选中任何项目", none_d="复制最前面 Finder 窗口所在的文件夹（快速 `cd` 很方便）",
 clean_t="干净的输出", clean_d="文件夹末尾不带 `/`",
 notif_t="即时反馈", notif_d="通知会显示复制的内容，并跟随 macOS 系统语言（英语、法语、德语、西班牙语、意大利语、葡萄牙语、日语、中文、希腊语）",
 h_install="安装",
 inst1="下载 `Copy-Finder-Path.alfredworkflow` 并双击",
 inst2="默认快捷键为 **⇧⌘C**，在 Alfred 中双击 Hotkey 模块即可修改",
 inst3="首次使用时，按 macOS 提示允许 Alfred 控制 Finder（系统设置 → 隐私与安全性 → 自动化）",
 requires="需要 [Alfred 5](https://www.alfredapp.com) 及 [Powerpack](https://www.alfredapp.com/powerpack/)，macOS 12 或更高版本。",
 h_how="工作原理",
 how_p="一段 AppleScript 向 Finder 获取选中项，几行 bash 整理路径，Alfred 把结果放入剪贴板。零依赖，原生 macOS 即可运行。",
 trigger_p="工作流还提供名为 `copy-path` 的 [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/)，可从任何地方触发：",
 h_dev="开发",
 dev_p="整个工作流都在 `tools/build.py` 中，`workflow/info.plist` 与 `dist/Copy-Finder-Path.alfredworkflow` 包由它生成。",
 c1="重新生成 workflow/info.plist + dist/*.alfredworkflow", c2="…并在 Alfred 中打开", c3="重新生成 workflow/icon.png", c4="重新生成所有 README",
 uids="UID 固定不变，重新导入会原地更新已有工作流。",
 hood=f"**内部实现**：Run Script 模块输出 [Alfred JSON 格式](https://www.alfredapp.com/help/workflows/utilities/json/)：{JSON}。`arg` 送入剪贴板，`title`（根据 `AppleLanguages` 选择）通过 `{{var:title}}` 送入通知。工作流的描述和 readme 是静态元数据，保持英文。",
 h_ideas="想法 / 简单改动",
 idea1="Shell 转义路径（`My\\ Folder`）：把最后的 `sed` 换成 `sed -E 's/([ ()&])/\\\\\\1/g'`",
 idea2="`file://` URL，或相对于 `$HOME` 的路径（`~/…`）",
 idea3="判断完整 locale，为 `zh-TW` / `zh-HK` 提供繁体中文",
 h_refs="参考", ref_docs="工作流文档", ref_vars="工作流变量", ref_forum="Alfred 社区论坛",
 h_license="许可证",
 footer="作者：<a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · 欢迎提交 Issue 和 PR",
)

T["el"] = dict(
 btn_alt="Λήψη του workflow",
 pitch="Μία συντόμευση. Η πλήρης διαδρομή ό,τι έχεις επιλέξει στο Finder, κατευθείαν στο πρόχειρο.",
 tagline="Τέλος το δεξί κλικ → κράτημα ⌥ → ψάξιμο για «Αντιγραφή ως όνομα διαδρομής». Επίλεξε, πάτα **⇧⌘C**, επικόλλησε.",
 alt_usage="Η επιλογή του Finder αντιγράφηκε στο πρόχειρο", alt_settings="Ο καμβάς του workflow στο Alfred",
 h_what="Τι κάνει",
 single_t="Ένα στοιχείο", single_d="αντιγράφει την απόλυτη διαδρομή του, π.χ.",
 multi_t="Πολλά στοιχεία", multi_d="μία διαδρομή ανά γραμμή, έτοιμη για script ή τερματικό",
 none_t="Χωρίς επιλογή", none_d="αντιγράφει τον φάκελο του μπροστινού παραθύρου Finder (βολικό για ένα γρήγορο `cd`)",
 clean_t="Καθαρή έξοδος", clean_d="χωρίς `/` στο τέλος των φακέλων",
 notif_t="Άμεση ανατροφοδότηση", notif_d="μια ειδοποίηση δείχνει τι αντιγράφηκε, στη γλώσσα του macOS σου (Αγγλικά, Γαλλικά, Γερμανικά, Ισπανικά, Ιταλικά, Πορτογαλικά, Ιαπωνικά, Κινεζικά, Ελληνικά)",
 h_install="Εγκατάσταση",
 inst1="Κατέβασε το `Copy-Finder-Path.alfredworkflow` και κάνε διπλό κλικ",
 inst2="Η προεπιλεγμένη συντόμευση είναι **⇧⌘C** — διπλό κλικ στο μπλοκ Hotkey στο Alfred για να την αλλάξεις",
 inst3="Στην πρώτη χρήση, επίτρεψε στο Alfred να ελέγχει το Finder όταν το ζητήσει το macOS (Ρυθμίσεις συστήματος → Απόρρητο και ασφάλεια → Αυτοματισμός)",
 requires="Απαιτεί [Alfred 5](https://www.alfredapp.com) με [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 ή νεότερο.",
 h_how="Πώς λειτουργεί",
 how_p="Ένα AppleScript ζητά από το Finder την επιλογή, λίγες γραμμές bash καθαρίζουν τις διαδρομές και το Alfred βάζει το αποτέλεσμα στο πρόχειρο. Χωρίς εξαρτήσεις — τρέχει σε ένα καθαρό macOS.",
 trigger_p="Το workflow εκθέτει επίσης ένα [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) με όνομα `copy-path`, ώστε να το ενεργοποιείς από οπουδήποτε:",
 h_dev="Ανάπτυξη",
 dev_p="Ολόκληρο το workflow βρίσκεται στο `tools/build.py` — το `workflow/info.plist` και το πακέτο `dist/Copy-Finder-Path.alfredworkflow` παράγονται από αυτό.",
 c1="αναδημιουργεί workflow/info.plist + dist/*.alfredworkflow", c2="…και το ανοίγει στο Alfred", c3="αναδημιουργεί το workflow/icon.png", c4="αναδημιουργεί όλα τα README",
 uids="Τα UID είναι σταθερά, οπότε η επανεισαγωγή ενημερώνει το υπάρχον workflow επιτόπου.",
 hood=f"**Στο παρασκήνιο**, το μπλοκ Run Script παράγει [JSON του Alfred](https://www.alfredapp.com/help/workflows/utilities/json/): {JSON}. Το `arg` τροφοδοτεί το πρόχειρο, το `title` (επιλεγμένο από το `AppleLanguages`) την ειδοποίηση μέσω `{{var:title}}`. Η περιγραφή και το readme του workflow είναι στατικά μεταδεδομένα και παραμένουν στα Αγγλικά.",
 h_ideas="Ιδέες / εύκολες παραλλαγές",
 idea1="Διαδρομές με escape για shell (`My\\ Folder`): αντικατάστησε το τελευταίο `sed` με `sed -E 's/([ ()&])/\\\\\\1/g'`",
 idea2="`file://` URL, ή διαδρομές σχετικές με το `$HOME` (`~/…`)",
 idea3="Παραδοσιακά Κινεζικά για `zh-TW` / `zh-HK` ελέγχοντας ολόκληρο το locale",
 h_refs="Αναφορές", ref_docs="Τεκμηρίωση workflows", ref_vars="Μεταβλητές workflow", ref_forum="Φόρουμ κοινότητας Alfred",
 h_license="Άδεια",
 footer="Από τον <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues και PRs ευπρόσδεκτα",
)

for code, _, _ in LANGS:
    body = TEMPLATE.format(nav=nav(code), trigger=TRIGGER, code=code, title=TITLE[code], **T[code])
    with open(os.path.join(OUT, fname(code)), "w") as f:
        f.write(body)
    print("→ " + fname(code))
