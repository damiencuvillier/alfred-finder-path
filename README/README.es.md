<img src="../icon.png" width="128" align="right" alt="Copy Finder Path icon">

# Copy Finder Path — [Alfred](https://www.alfredapp.com) Workflow

← [Volver al inicio](../README.md)

**Un atajo. La ruta completa de lo que tengas seleccionado en el Finder, directa al portapapeles.**

Se acabó el clic derecho → mantener ⌥ → buscar «Copiar como nombre de ruta». Selecciona, pulsa **⇧⌘C**, pega.

<img src="../screenshots/usage.png" width="640" alt="Selección del Finder copiada al portapapeles">

## ✨ Qué hace

- **Un elemento** → copia su ruta absoluta, p. ej. `/Users/you/Projects/report.pdf`
- **Varios elementos** → una ruta por línea, lista para un script o el terminal
- **Sin selección** → copia la carpeta de la ventana del Finder en primer plano (útil para un `cd` rápido)
- **Salida limpia** → sin `/` final en las carpetas
- **Respuesta inmediata** → una notificación muestra lo copiado, en el idioma de tu macOS (inglés, francés, alemán, español, italiano, portugués, japonés, chino, griego)

## 🚀 Instalación

1. Descarga `Copy-Finder-Path.alfredworkflow` y haz doble clic
2. El atajo por defecto es **⇧⌘C**; haz doble clic en el bloque Hotkey de Alfred para cambiarlo
3. La primera vez, permite que Alfred controle el Finder cuando macOS lo pida (Ajustes del Sistema → Privacidad y seguridad → Automatización)

Requiere [Alfred 5](https://www.alfredapp.com) con el [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 o posterior.

## 🔧 Cómo funciona

<img src="../screenshots/settings.png" width="640" alt="Lienzo del workflow en Alfred">

Un AppleScript pide al Finder su selección, unas líneas de bash limpian las rutas y Alfred deja el resultado en el portapapeles. Sin dependencias: funciona en un macOS estándar.

El workflow también expone un [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) llamado `copy-path`, para lanzarlo desde cualquier sitio:

```applescript
tell application id "com.runningwithcrayons.Alfred" to run trigger "copy-path" in workflow "dev.gotan.alfred.copyfinderpath"
```

## 🛠 Desarrollo

Todo el workflow vive en `build.py`: `info.plist` y el paquete `.alfredworkflow` se generan a partir de él.

```bash
./build.py            # regenera info.plist + Copy-Finder-Path.alfredworkflow
./build.py --install  # …y lo abre en Alfred
./make_icon.py        # regenera icon.png
```

Los UIDs son estables, así que reimportar actualiza el workflow existente en su sitio.

**Por dentro**, el bloque Run Script emite [JSON de Alfred](https://www.alfredapp.com/help/workflows/utilities/json/): `{"alfredworkflow":{"arg":"<paths>","variables":{"title":"<localized title>"}}}`. `arg` alimenta el portapapeles y `title` (elegido según `AppleLanguages`) la notificación mediante `{var:title}`. La descripción y el readme del workflow son metadatos estáticos y se quedan en inglés.

**Ideas / ajustes fáciles**

- Rutas escapadas para shell (`Mi\ Carpeta`): sustituye el `sed` final por `sed -E 's/([ ()&])/\\\1/g'`
- URLs `file://`, o rutas relativas a `$HOME` (`~/…`)
- Chino tradicional para `zh-TW` / `zh-HK` comprobando la locale completa

## 📚 Referencias

- [Alfred](https://www.alfredapp.com) · [Powerpack](https://www.alfredapp.com/powerpack/) · [Alfred Gallery](https://alfred.app)
- [Documentación de workflows](https://www.alfredapp.com/help/workflows/) — [Hotkey](https://www.alfredapp.com/help/workflows/triggers/hotkey/), [Run Script](https://www.alfredapp.com/help/workflows/actions/run-script/), [Copy to Clipboard](https://www.alfredapp.com/help/workflows/outputs/copy-to-clipboard/), [Post Notification](https://www.alfredapp.com/help/workflows/outputs/post-notification/)
- [Variables de workflow](https://www.alfredapp.com/help/workflows/advanced/variables/) — `{var:title}`
- [Foro de la comunidad Alfred](https://www.alfredforum.com)

## 📄 Licencia

MIT.

---

Hecho por [Damien](https://damiencuvillier.com) · Issues y PRs bienvenidos
