import os
import shutil

# Define a raiz do nosso disco simulado (caminho absoluto para evitar fugas)
# Usa __file__ para referenciar corretamente o diretório onde system.py está localizado
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(SCRIPT_DIR, "disco")

# Garante que a pasta do disco exista ao iniciar
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

# Variável global para rastrear o diretório atual do usuário dentro do SO simulado
# Começa sempre na raiz ('/')
diretorio_atual_simulado = "/"


def obter_caminho_real():
    """Converte o caminho simulado do SO para o caminho real no computador."""
    # Remove a barra inicial para o os.path.join funcionar corretamente
    relativo = diretorio_atual_simulado.lstrip("/")
    caminho_real = os.path.abspath(os.path.join(BASE_DIR, relativo))
    return caminho_real


def comando_ajuda():
    """Exibe os comandos disponíveis no sistema."""
    ajuda_texto = """
SO Simulado v0.1B - Comandos Disponíveis:
--------------------------------------------------
help         : Mostra esta tela de auxílio.
ls           : Lista os arquivos e pastas do diretório atual.
cd <dir>      : Altera o diretório atual (use '..' para voltar).
pwd          : Mostra o caminho do diretório atual.
create <arq>  : Cria um arquivo de texto vazio.
rm <arq>      : Remove um arquivo ou pasta.
clear        : Limpa a tela do terminal.
exit         : Desliga o sistema operacional.
<app>        : Executa um app Python em SO/apps/<app>.py.
--------------------------------------------------
"""
    print(ajuda_texto)


def comando_ls():
    """Lista o conteúdo do diretório atual."""
    caminho_real = obter_caminho_real()
    try:
        conteudo = os.listdir(caminho_real)
        if not conteudo:
            print("(Diretório vazio)")
        for item in conteudo:
            # Diferencia visualmente pastas de arquivos
            if os.path.isdir(os.path.join(caminho_real, item)):
                print(f"📁 {item}/")
            else:
                print(f"📄 {item}")

    except Exception as e:
        print(f"Erro ao listar diretório: {e}")


def comando_pwd():
    """Mostra o diretório simulado atual."""
    print(diretorio_atual_simulado)


def comando_cd(destino):
    """Altera o diretório atual, impedindo o usuário de sair da pasta 'disco'."""
    global diretorio_atual_simulado
    
    # Se o destino é um caminho absoluto (começa com '/'), trata como caminho simulado
    if destino.startswith('/'):
        # Remove barras iniciais para usar como relativo a BASE_DIR
        caminho_relativo = destino.lstrip('/')
        nova_rota_real = os.path.abspath(os.path.join(BASE_DIR, caminho_relativo))
    else:
        # Caso contrário, trata como relativo ao diretório atual
        caminho_real_atual = obter_caminho_real()
        nova_rota_real = os.path.abspath(os.path.join(caminho_real_atual, destino))
    
    # Segurança: Impede que o usuário use '../../' para acessar pastas fora do 'disco'
    if not nova_rota_real.startswith(BASE_DIR):
        print("Acesso negado: Você não pode sair do diretório raiz do SO.")
        return

    if os.path.isdir(nova_rota_real):
        # Atualiza a rota simulada tirando a parte do BASE_DIR real
        sub_caminho = nova_rota_real.replace(BASE_DIR, "").replace("\\", "/")
        diretorio_atual_simulado = sub_caminho if sub_caminho != "" else "/"
    else:
        print(f"Erro: O diretório '{destino}' não existe.")


def comando_criar(nome_arquivo):
    """Cria um arquivo de texto vazio ou uma pasta no diretório atual.

    Comportamento:
    - Se `nome_arquivo` começar com '/' ou '\\', cria um diretório (e pais).
    - Se for um caminho para arquivo (p.ex. 'pasta/sub/arquivo.txt'), cria os
      diretórios pais necessários e o arquivo vazio.
    Segurança: impede criar fora de `BASE_DIR` usando caminhos com '..'.
    """
    # Detecta se é uma pasta (começa com '/' ou '\')
    eh_diretorio = nome_arquivo.startswith('/') or nome_arquivo.startswith('\\')
    
    # Remove a barra inicial para processar o caminho
    nome_processado = nome_arquivo.lstrip('/\\')
    
    # Caminho absoluto destino dentro do disco simulado
    caminho_real = os.path.abspath(os.path.join(obter_caminho_real(), nome_processado))

    # Segurança: não permitir sair do BASE_DIR
    if not caminho_real.startswith(BASE_DIR):
        print("Acesso negado: caminho fora do disco simulado.")
        return

    try:
        if eh_diretorio:
            os.makedirs(caminho_real, exist_ok=True)
            print(f"Diretório '{nome_processado}' criado com sucesso.")

        else:
            # Garante que os diretórios pais existam antes de criar o arquivo
            diretorio_pai = os.path.dirname(caminho_real)
            if diretorio_pai and not os.path.exists(diretorio_pai):
                os.makedirs(diretorio_pai, exist_ok=True)

            with open(caminho_real, 'w', encoding='utf-8') as f:
                f.write("")
            print(f"Arquivo '{nome_arquivo}' criado com sucesso.")


    except Exception as e:
        print(f"Erro ao criar: {e}")


def comando_rm(nome_item):
    """Remove um arquivo ou pasta do diretório atual."""
    caminho_real = os.path.join(obter_caminho_real(), nome_item)
    if not os.path.exists(caminho_real):
        print(f"Erro: '{nome_item}' não encontrado.")
        return
        
    try:
        if os.path.isdir(caminho_real):
            shutil.rmtree(caminho_real)
            print(f"Diretório '{nome_item}' removido.")

        else:
            os.remove(caminho_real)
            print(f"Arquivo '{nome_item}' removido.")
    

    except Exception as e:
        print(f"Erro ao remover: {e}")


def comando_limpar():
    """Limpa a tela do terminal do sistema hospedeiro."""
    os.system('cls' if os.name == 'nt' else 'clear')
