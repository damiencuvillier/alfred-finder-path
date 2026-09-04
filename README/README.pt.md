<img src="../icon.png" width="128" align="right" alt="Copy Finder Path icon">

# Copy Finder Path — [Alfred](https://www.alfredapp.com) Workflow

← [Voltar ao início](../README.md)

**Um atalho. O caminho completo do que tiveres selecionado no Finder, direto para a área de transferência.**

Acabou o clique direito → manter ⌥ → procurar «Copiar como nome de caminho». Seleciona, prime **⇧⌘C**, cola.

<img src="../screenshots/usage.png" width="640" alt="Seleção do Finder copiada para a área de transferência">

## ✨ O que faz

- **Um item** → copia o seu caminho absoluto, p. ex. `/Users/you/Projects/report.pdf`
- **Vários itens** → um caminho por linha, pronto para um script ou o terminal
- **Sem seleção** → copia a pasta da janela do Finder em primeiro plano (útil para um `cd` rápido)
- **Saída limpa** → sem `/` final nas pastas
- **Feedback imediato** → uma notificação mostra o que foi copiado, no idioma do teu macOS (inglês, francês, alemão, espanhol, italiano, português, japonês, chinês, grego)

## 🚀 Instalação

1. Descarrega `Copy-Finder-Path.alfredworkflow` e faz duplo clique
2. O atalho predefinido é **⇧⌘C** — faz duplo clique no bloco Hotkey no Alfred para o alterar
3. Na primeira utilização, permite que o Alfred controle o Finder quando o macOS pedir (Definições do Sistema → Privacidade e Segurança → Automatização)

Requer [Alfred 5](https://www.alfredapp.com) com o [Powerpack](https://www.alfredapp.com/powerpack/), macOS 12 ou posterior.

## 🔧 Como funciona

<img src="../screenshots/settings.png" width="640" alt="Canvas do workflow no Alfred">

Um AppleScript pede ao Finder a seleção, algumas linhas de bash limpam os caminhos e o Alfred coloca o resultado na área de transferência. Sem dependências — funciona num macOS de origem.

O workflow expõe também um [**External Trigger**](https://www.alfredapp.com/help/workflows/triggers/external/) chamado `copy-path`, para o disparar de qualquer lado:

```applescript
tell application id "com.runningwithcrayons.Alfred" to run trigger "copy-path" in workflow "dev.gotan.alfred.copyfinderpath"
```

## 🛠 Desenvolvimento

Todo o workflow vive em `build.py` — o `info.plist` e o pacote `.alfredworkflow` são gerados a partir dele.

```bash
./build.py            # regenera info.plist + Copy-Finder-Path.alfredworkflow
./build.py --install  # …e abre-o no Alfred
./make_icon.py        # regenera icon.png
```

Os UIDs são estáveis, por isso reimportar atualiza o workflow existente no lugar.

**Por baixo do capô**, o bloco Run Script emite [JSON do Alfred](https://www.alfredapp.com/help/workflows/utilities/json/): `{"alfredworkflow":{"arg":"<paths>","variables":{"title":"<localized title>"}}}`. `arg` alimenta a área de transferência, `title` (escolhido a partir de `AppleLanguages`) alimenta a notificação via `{var:title}`. A descrição e o readme do workflow são metadados estáticos e ficam em inglês.

**Ideias / ajustes fáceis**

- Caminhos com escape para a shell (`Minha\ Pasta`): troca o `sed` final por `sed -E 's/([ ()&])/\\\1/g'`
- URLs `file://`, ou caminhos relativos a `$HOME` (`~/…`)
- Chinês tradicional para `zh-TW` / `zh-HK` verificando a locale completa

## 📚 Referências

- [Alfred](https://www.alfredapp.com) · [Powerpack](https://www.alfredapp.com/powerpack/) · [Alfred Gallery](https://alfred.app)
- [Documentação de workflows](https://www.alfredapp.com/help/workflows/) — [Hotkey](https://www.alfredapp.com/help/workflows/triggers/hotkey/), [Run Script](https://www.alfredapp.com/help/workflows/actions/run-script/), [Copy to Clipboard](https://www.alfredapp.com/help/workflows/outputs/copy-to-clipboard/), [Post Notification](https://www.alfredapp.com/help/workflows/outputs/post-notification/)
- [Variáveis de workflow](https://www.alfredapp.com/help/workflows/advanced/variables/) — `{var:title}`
- [Fórum da comunidade Alfred](https://www.alfredforum.com)

## 📄 Licença

MIT.

---

Feito por <a href='https://damiencuvillier.com' target='_blank' rel='noopener'>Damien</a> · Issues e PRs bem-vindos
