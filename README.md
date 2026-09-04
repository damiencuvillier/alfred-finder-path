# Copy Finder Path — Alfred Workflow

**One hotkey. The full POSIX path of whatever you have selected in Finder, straight to your clipboard.**

No more right-click → hold ⌥ → hunt for "Copy as Pathname". Select, press, paste.

## ✨ What it does

- **Single item** → copies its absolute path
  `/Users/you/Projects/report.pdf`
- **Multiple items** → one path per line, ready to paste into a script or a terminal
- **Nothing selected** → copies the folder of the frontmost Finder window
  (perfect for a quick `cd` in your terminal)
- **Clean output** → no trailing `/` on folders, no stray characters
- **Instant feedback** → a notification shows exactly what was copied

## 🚀 Install

1. Download `Copy-Finder-Path.alfredworkflow` and double-click it
2. The default hotkey is **⇧⌘C**. To change it, open the workflow in Alfred and double-click the **Hotkey** block
3. On first run, allow Alfred to control Finder when macOS asks
   (System Settings → Privacy & Security → Automation)

That's it.

## 🔧 How it works

```
Hotkey ──▶ Run Script (bash + osascript) ──▶ Copy to Clipboard
                                        └──▶ Notification
```

The script asks Finder for its current selection via AppleScript, converts each item to a POSIX path, and hands the result to Alfred. No dependencies, no external tools — it runs on a stock macOS install.

## 🛠 Build from source

The whole workflow is defined in a single `build.py` file. Edit it, then:

```bash
./build.py            # regenerates info.plist and the .alfredworkflow bundle
./build.py --install  # …and opens it in Alfred
```

UIDs are stable, so re-importing updates the existing workflow in place and keeps your hotkey.

## 💡 Variants

Want a shell-escaped path (`My\ Folder/file.txt`)? Replace the final `sed` in the script with:

```bash
sed -E 's/([ ()&])/\\\1/g'
```

Other easy tweaks: emit `file://` URLs, or paths relative to `$HOME` (`~/…`).

## 📋 Requirements

- Alfred 5 with the Powerpack
- macOS 12 or later

## 📄 License

MIT — do whatever you want with it.

---

Made by [Damien](https://gotan.dev) · Issues and PRs welcome
