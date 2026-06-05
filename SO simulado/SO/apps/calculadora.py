import sys


def main():
    print("Calculadora do SO Simulado")
    print("Digite 'sair' para voltar ao terminal.")

    while True:
        try:
            entrada = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nVoltando ao terminal...")
            break

        if not entrada:
            continue

        if entrada.lower() in ("sair", "exit", "voltar"):
            print("Voltando ao terminal...")
            break

        try:
            resultado = eval(entrada, {"__builtins__": None}, {})
            print(resultado)
        except Exception:
            print("Expressão inválida. Use apenas números e operadores básicos.")


if __name__ == "__main__":
    main()
