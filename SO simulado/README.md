# SO Simulado

Projeto de sistema operacional simulado em Python que executa comandos básicos de terminal e apps internos.

## Estrutura do projeto

- `SO/`
  - `main.py` — shell principal que interpreta comandos e executa apps.
  - `system.py` — comandos do sistema: `ls`, `cd`, `pwd`, `create`, `rm`, `clear`, `help`, etc.
  - `disco/` — disco virtual do SO; todos os arquivos e pastas do sistema ficam aqui.
  - `apps/` — apps Python executáveis pelo terminal do SO.
    - `calculadora.py` — app de calculadora simples.
    - `jokenpo.py` — app de pedra/papel/tesoura.

## Como executar

1. Abra o terminal no diretório do projeto:
   ```bash
   cd "/home/nicolas/Documentos/SO simulado/SO"
   ```
2. Execute o shell do SO simulado:
   ```bash
   python main.py
   ```

## Comandos disponíveis

- `help` — mostra a lista de comandos.
- `ls` — lista o conteúdo do diretório atual.
- `cd <diretório>` — altera o diretório atual. Use `..` para subir e `/` para ir à raiz do disco.
- `pwd` — mostra o diretório atual dentro do SO.
- `create <nome>` — cria arquivo ou pasta (pasta se começar com `/`).
- `rm <nome>` — remove arquivo ou pasta.
- `clear` — limpa a tela do terminal.
- `exit` — sai do sistema.
- `<app>` — executa scripts Python em `SO/apps/<app>.py`.

## Apps disponíveis

- `calculadora` — abre uma calculadora no terminal.

### Exemplo de uso de app

No prompt do SO simulado, digite:
```bash
calculadora
```


## Como adicionar novos apps

### Instruções dentro de `SO/apps`.

## Observações

- O SO simulado usa a pasta `SO/disco/` como raiz do sistema de arquivos.
- Os comandos são processados pelo shell em `SO/main.py`, então o app precisa existir dentro da pasta `SO/apps`.
