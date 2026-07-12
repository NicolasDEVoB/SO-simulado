import os
import runpy
import sys
import system


def inicializar_sistema():
    """Simula o boot/inicialização do Sistema Operacional."""
    system.comando_limpar()
    print("Montando unidade de disco (/disco)... OK")
    print("Digite 'help' para ver a lista de comandos.")
    print("----------------------------------------")


def shell():
    """Loop principal que orquestra as entradas do usuário."""
    inicializar_sistema()
    
    while True:
        # Exibe o prompt estilizado, ex: [SO Simulado][ /docs ]$ 
        prompt = f"\033[32mdefault@default-desktop\033[0m:\033[34m~{system.diretorio_atual_simulado}$\033[0m "
        
        try:
            entrada = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            # Captura Ctrl+C ou Ctrl+D de forma elegante
            print("\nDesligando via interrupção de hardware...")
            break

        if not entrada:
            continue

        # Divide a entrada em comando e argumentos
        partes = entrada.split(" ", 1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else None

        # Orquestração dos comandos
        
        match comando:
            case "exit":
                print("Desligando o sistema... Até logo!")
                break
                
            case "help":
                system.comando_ajuda()
                
            case "ls":
                system.comando_ls()
                
            case "pwd":
                system.comando_pwd()
                
            case "clear":
                system.comando_limpar()
                
            case "cd":
                if argumento:
                    system.comando_cd(argumento)
                else:
                    print("Uso correto: cd <nome_do_diretorio>")
                    
            case "create":
                if argumento:
                    system.comando_criar(argumento)
                else:
                    print("Uso correto: create <nome_do_arquivo.txt>")
                    
            case "rm":
                if argumento:
                    system.comando_rm(argumento)
                else:
                    print("Uso correto: rm <nome_do_item>")
                    
            case _:
                if executar_app(comando, argumento):
                    continue
                print(f"Comando '{comando}' não reconhecido. Digite 'help'.")


def executar_app(comando, argumento):
    """Tenta executar um app Python dentro da pasta apps."""
    app_caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apps", f"{comando}.py")
    if not os.path.isfile(app_caminho):
        return False

    argumentos = [comando] + (argumento.split() if argumento else [])
    original_argv = sys.argv.copy()
    try:
        sys.argv = argumentos
        runpy.run_path(app_caminho, run_name="__main__")
    except Exception as e:
        print(f"Erro ao executar app '{comando}': {e}")
    finally:
        sys.argv = original_argv
    return True

if __name__ == "__main__":
    shell()