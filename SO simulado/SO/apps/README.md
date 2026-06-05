# Como criar um app para o SO Simulado

Este README explica como criar um novo app Python que pode ser executado diretamente pelo terminal do SO simulado.

## Onde colocar o app

Crie seu arquivo Python dentro da pasta:

```bash
SO/apps/
```

O nome do arquivo deve ser o nome do app. Por exemplo:

- `SO/apps/calculadora.py`
- `SO/apps/jokenpo.py`
- `SO/apps/agenda.py`

## Como o app é executado

No shell do SO simulado, basta digitar o nome do app (sem `.py`):

```bash
calculadora
```

O sistema procura por `SO/apps/calculadora.py` e executa esse script.

## Regras básicas do app

1. Use `if __name__ == '__main__':` para iniciar o app.
2. O app pode ser interativo usando `input()` e `print()`.
3. Quando o usuário quiser sair do app, retorne ao terminal normalmente.

### Exemplo mínimo

```python
# SO/apps/exemplo.py

def main():
    print("Olá do app Exemplo!")
    resposta = input("Digite algo: ")
    print(f"Você digitou: {resposta}")


if __name__ == '__main__':
    main()
```

Após criar o arquivo, rode no terminal do SO:

```bash
exemplo
```

## Boas práticas

- não modifique `sys.argv` sem necessidade;
- mantenha a lógica de interface no `main()` ou em funções chamadas pelo `main()`;
- trate `EOFError` e `KeyboardInterrupt` para sair do app com mais elegância;
- evite código muito pesado para não travar o shell.

## Arquivos de exemplo

O projeto já tem exemplos de apps, como `calculadora.py`.

Você pode usar esses exemplos como base para criar seu próprio app.
