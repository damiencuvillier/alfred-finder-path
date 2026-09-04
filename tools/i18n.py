"""Single source of truth for supported languages.

Every tool (build.py, make-flags.py, make-buttons.py, make-readmes.py) reads
this list, so adding a language here adds it everywhere: notification title
in the workflow, flag, download button and README.
"""

# code, flag emoji, native name, notification title, download label, README title
LANGS = [
    ("en", "🇬🇧", "English",   "Path copied",              "Download",      "Copy fullpath from Finder"),
    ("fr", "🇫🇷", "Français",  "Chemin copié",             "Télécharger",   "Copier le chemin complet depuis le Finder"),
    ("de", "🇩🇪", "Deutsch",   "Pfad kopiert",             "Herunterladen", "Vollständigen Pfad aus dem Finder kopieren"),
    ("es", "🇪🇸", "Español",   "Ruta copiada",             "Descargar",     "Copiar la ruta completa desde el Finder"),
    ("it", "🇮🇹", "Italiano",  "Percorso copiato",         "Scarica",       "Copia il percorso completo dal Finder"),
    ("pt", "🇵🇹", "Português", "Caminho copiado",          "Descarregar",   "Copiar o caminho completo do Finder"),
    ("ja", "🇯🇵", "日本語",     "パスをコピーしました",        "ダウンロード",    "Finder からフルパスをコピー"),
    ("zh", "🇨🇳", "中文",       "路径已复制",                "下载",           "从 Finder 复制完整路径"),
    ("el", "🇬🇷", "Ελληνικά",  "Η διαδρομή αντιγράφηκε",   "Λήψη",          "Αντιγραφή πλήρους διαδρομής από το Finder"),
]

DEFAULT = "en"
CODES = [l[0] for l in LANGS]
FLAG = {l[0]: l[1] for l in LANGS}
NAME = {l[0]: l[2] for l in LANGS}
NOTIF = {l[0]: l[3] for l in LANGS}
DOWNLOAD = {l[0]: l[4] for l in LANGS}
TITLE = {l[0]: l[5] for l in LANGS}

# Fonts that can render each language's download label (make-buttons.py)
CJK = {"ja", "zh"}
