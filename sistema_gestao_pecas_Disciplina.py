"""
Sistema de Gestão de Peças - Controle de Qualidade e Armazenamento
11Projeto de Algoritmos e Lógica de Programação
Curso: Tecnólogo em IA e Automação - UniFECAF
"""

# ============================================================================
# ESTRUTURA DE DADOS
# ============================================================================
# Cada peça é representada por uma lista com 6 elementos:
# [0] id (int)
# [1] peso (float)
# [2] cor (str)
# [3] comprimento (float)
# [4] aprovada (bool)
# [5] motivos_reprovacao (lista de strings)

# Cada caixa é representada por uma lista com 3 elementos:
# [0] numero (int)
# [1] pecas (lista de peças)
# [2] fechada (bool)

# ============================================================================
# VARIÁVEIS
# ============================================================================

# Lista de todas as peças cadastradas
pecas_cadastradas = []

# Lista de caixas
caixas = []

# Contador para gerar IDs únicos
contador_id = [1]  # Usando lista para permitir modificação dentro de funções

# Capacidade máxima de peças por caixa
CAPACIDADE_MAXIMA_CAIXA = 10


# ============================================================================
# FUNÇÕES DE CRIAÇÃO E VALIDAÇÃO
# ============================================================================

def criar_peca(peso, cor, comprimento):
    """
    Cria uma lista representando uma peça.
    
    Args:
        peso (float): Peso da peça em gramas
        cor (str): Cor da peça
        comprimento (float): Comprimento da peça em centímetros
    
    Returns:
        list: Lista com os dados da peça [id, peso, cor, comprimento, aprovada, motivos]
    """
    id_peca = contador_id[0]
    contador_id[0] += 1
    
    # Criar peça: [id, peso, cor, comprimento, aprovada, motivos_reprovacao]
    peca = [id_peca, peso, cor.lower(), comprimento, True, []]
    
    # Validar a peça
    validar_qualidade_peca(peca)
    
    return peca


def validar_qualidade_peca(peca):
    """
    Valida se a peça atende aos critérios de qualidade.
    Modifica a lista da peça diretamente.
    
    Args:
        peca (list): Lista representando a peça
    """
    # Índices: [0]id, [1]peso, [2]cor, [3]comprimento, [4]aprovada, [5]motivos
    
    # Validar peso (95g a 105g)
    if peca[1] < 95 or peca[1] > 105:
        peca[4] = False
        peca[5].append(f"Peso fora do padrão ({peca[1]}g - esperado: 95g-105g)")
    
    # Validar cor (azul ou verde)
    if peca[2] not in ['azul', 'verde']:
        peca[4] = False
        peca[5].append(f"Cor inválida ({peca[2]} - esperado: azul ou verde)")
    
    # Validar comprimento (10cm a 20cm)
    if peca[3] < 10 or peca[3] > 20:
        peca[4] = False
        peca[5].append(f"Comprimento fora do padrão ({peca[3]}cm - esperado: 10cm-20cm)")


def criar_caixa(numero):
    """
    Cria uma lista representando uma caixa.
    
    Args:
        numero (int): Número identificador da caixa
    
    Returns:
        list: Lista com os dados da caixa [numero, pecas, fechada]
    """
    return [numero, [], False]


# ============================================================================
# FUNÇÕES DE GERENCIAMENTO DE PEÇAS
# ============================================================================

def cadastrar_peca(peso, cor, comprimento):
    """
    Cadastra uma nova peça no sistema.
    
    Args:
        peso (float): Peso da peça em gramas
        cor (str): Cor da peça
        comprimento (float): Comprimento da peça em centímetros
    
    Returns:
        list: Lista representando a peça cadastrada
    """
    peca = criar_peca(peso, cor, comprimento)
    pecas_cadastradas.append(peca)
    
    # Se aprovada (índice [4]), armazena em caixa
    if peca[4]:
        armazenar_peca(peca)
    
    return peca


def armazenar_peca(peca):
    """
    Armazena uma peça aprovada em uma caixa disponível.
    
    Args:
        peca (list): Lista representando a peça a ser armazenada
    """
    # Se não há caixas, cria a primeira
    if len(caixas) == 0:
        caixas.append(criar_caixa(1))
    
    # Pega a última caixa
    caixa_atual = caixas[len(caixas) - 1]
    
    # Se a caixa atual está fechada (índice [2]), cria uma nova
    if caixa_atual[2]:
        nova_caixa = criar_caixa(len(caixas) + 1)
        caixas.append(nova_caixa)
        caixa_atual = nova_caixa
    
    # Adiciona a peça na caixa (índice [1] é a lista de peças)
    caixa_atual[1].append(peca)
    
    # Verifica se a caixa atingiu a capacidade máxima
    if len(caixa_atual[1]) >= CAPACIDADE_MAXIMA_CAIXA:
        caixa_atual[2] = True  # Fecha a caixa


def remover_peca(id_peca):
    """
    Remove uma peça cadastrada pelo ID.
    
    Args:
        id_peca (int): ID da peça a ser removida
    
    Returns:
        bool: True se a peça foi removida, False caso contrário
    """
    # Procurar a peça na lista de peças cadastradas
    for i in range(len(pecas_cadastradas)):
        # Índice [0] é o ID da peça
        if pecas_cadastradas[i][0] == id_peca:
            peca_removida = pecas_cadastradas[i]
            pecas_cadastradas.pop(i)
            
            # Se estava aprovada (índice [4]), remove das caixas também
            if peca_removida[4]:
                for caixa in caixas:
                    # Índice [1] é a lista de peças da caixa
                    for j in range(len(caixa[1])):
                        if caixa[1][j][0] == id_peca:
                            caixa[1].pop(j)
                            caixa[2] = False  # Reabre a caixa
                            return True
            
            return True
    
    return False


def listar_pecas_aprovadas():
    """
    Retorna lista de peças aprovadas.
    
    Returns:
        list: Lista de peças aprovadas
    """
    aprovadas = []
    for peca in pecas_cadastradas:
        # Índice [4] indica se está aprovada
        if peca[4]:
            aprovadas.append(peca)
    return aprovadas


def listar_pecas_reprovadas():
    """
    Retorna lista de peças reprovadas.
    
    Returns:
        list: Lista de peças reprovadas
    """
    reprovadas = []
    for peca in pecas_cadastradas:
        # Índice [4] indica se está aprovada
        if not peca[4]:
            reprovadas.append(peca)
    return reprovadas


def listar_caixas_fechadas():
    """
    Retorna lista de caixas fechadas.
    
    Returns:
        list: Lista de caixas fechadas
    """
    fechadas = []
    for caixa in caixas:
        # Índice [2] indica se está fechada
        if caixa[2]:
            fechadas.append(caixa)
    return fechadas


# ============================================================================
# FUNÇÕES DE FORMATAÇÃO E EXIBIÇÃO
# ============================================================================

def formatar_peca(peca):
    """
    Formata os dados de uma peça para exibição.
    
    Args:
        peca (list): Lista representando a peça
    
    Returns:
        str: String formatada com os dados da peça
    """
    # Índices: [0]id, [1]peso, [2]cor, [3]comprimento, [4]aprovada
    status = "APROVADA" if peca[4] else "REPROVADA"
    return f"ID: {peca[0]} | Peso: {peca[1]}g | Cor: {peca[2]} | Comprimento: {peca[3]}cm | Status: {status}"


def formatar_caixa(caixa):
    """
    Formata os dados de uma caixa para exibição.
    
    Args:
        caixa (list): Lista representando a caixa
    
    Returns:
        str: String formatada com os dados da caixa
    """
    # Índices: [0]numero, [1]pecas, [2]fechada
    status = "FECHADA" if caixa[2] else "ABERTA"
    return f"Caixa #{caixa[0]} - {len(caixa[1])}/{CAPACIDADE_MAXIMA_CAIXA} peças - Status: {status}"


def gerar_relatorio():
    """
    Gera relatório consolidado do sistema.
    
    Returns:
        str: String contendo o relatório completo
    """
    aprovadas = listar_pecas_aprovadas()
    reprovadas = listar_pecas_reprovadas()
    caixas_fechadas = listar_caixas_fechadas()
    
    relatorio = "\n" + "="*70 + "\n"
    relatorio += "RELATÓRIO FINAL - SISTEMA DE GESTÃO DE PEÇAS\n"
    relatorio += "="*70 + "\n\n"
    
    # Total de peças aprovadas
    relatorio += f"📊 TOTAL DE PEÇAS APROVADAS: {len(aprovadas)}\n"
    relatorio += "-"*70 + "\n"
    if len(aprovadas) > 0:
        for peca in aprovadas:
            relatorio += f"  • {formatar_peca(peca)}\n"
    else:
        relatorio += "  Nenhuma peça aprovada.\n"
    
    # Total de peças reprovadas
    relatorio += f"\n❌ TOTAL DE PEÇAS REPROVADAS: {len(reprovadas)}\n"
    relatorio += "-"*70 + "\n"
    if len(reprovadas) > 0:
        for peca in reprovadas:
            relatorio += f"  • {formatar_peca(peca)}\n"
            # Índice [5] contém os motivos de reprovação
            for motivo in peca[5]:
                relatorio += f"    → {motivo}\n"
    else:
        relatorio += "  Nenhuma peça reprovada.\n"
    
    # Quantidade de caixas utilizadas
    relatorio += f"\n📦 QUANTIDADE DE CAIXAS UTILIZADAS: {len(caixas)}\n"
    relatorio += "-"*70 + "\n"
    for caixa in caixas:
        relatorio += f"  • {formatar_caixa(caixa)}\n"
    
    # Caixas fechadas
    relatorio += f"\n🔒 CAIXAS FECHADAS: {len(caixas_fechadas)}\n"
    relatorio += "-"*70 + "\n"
    if len(caixas_fechadas) > 0:
        for caixa in caixas_fechadas:
            relatorio += f"  • {formatar_caixa(caixa)}\n"
    else:
        relatorio += "  Nenhuma caixa fechada ainda.\n"
    
    relatorio += "\n" + "="*70 + "\n"
    
    return relatorio


# ============================================================================
# FUNÇÕES DO MENU INTERATIVO
# ============================================================================

def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n" + "="*70)
    print("SISTEMA DE GESTÃO DE PEÇAS - CONTROLE DE QUALIDADE")
    print("="*70)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("="*70)


def menu_cadastrar_peca():
    """Menu para cadastrar nova peça."""
    print("\n--- CADASTRAR NOVA PEÇA ---")
    
    try:
        peso = float(input("Digite o peso da peça (em gramas): "))
        cor = input("Digite a cor da peça (azul ou verde): ").strip()
        comprimento = float(input("Digite o comprimento da peça (em cm): "))
        
        peca = cadastrar_peca(peso, cor, comprimento)
        
        print("\n✓ Peça cadastrada com sucesso!")
        print(formatar_peca(peca))
        
        # Índice [4] indica se está aprovada
        if peca[4]:
            print("✓ Peça APROVADA e armazenada em caixa!")
        else:
            print("✗ Peça REPROVADA!")
            print("Motivos:")
            # Índice [5] contém os motivos
            for motivo in peca[5]:
                print(f"  → {motivo}")
    
    except ValueError:
        print("\n✗ Erro: Valores inválidos! Digite números válidos para peso e comprimento.")
    except Exception as e:
        print(f"\n✗ Erro ao cadastrar peça: {e}")


def menu_listar_pecas():
    """Menu para listar peças."""
    print("\n--- LISTAR PEÇAS ---")
    print("1. Listar peças aprovadas")
    print("2. Listar peças reprovadas")
    print("3. Listar todas as peças")
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == "1":
        pecas = listar_pecas_aprovadas()
        print(f"\n📊 PEÇAS APROVADAS ({len(pecas)}):")
        print("-"*70)
    elif opcao == "2":
        pecas = listar_pecas_reprovadas()
        print(f"\n❌ PEÇAS REPROVADAS ({len(pecas)}):")
        print("-"*70)
    elif opcao == "3":
        pecas = pecas_cadastradas
        print(f"\n📋 TODAS AS PEÇAS ({len(pecas)}):")
        print("-"*70)
    else:
        print("✗ Opção inválida!")
        return
    
    if len(pecas) > 0:
        for peca in pecas:
            print(f"  • {formatar_peca(peca)}")
            # Índice [4] indica se está aprovada, [5] contém motivos
            if not peca[4]:
                for motivo in peca[5]:
                    print(f"    → {motivo}")
    else:
        print("  Nenhuma peça encontrada.")


def menu_remover_peca():
    """Menu para remover peça."""
    print("\n--- REMOVER PEÇA ---")
    
    try:
        id_peca = int(input("Digite o ID da peça a ser removida: "))
        
        if remover_peca(id_peca):
            print(f"\n✓ Peça ID {id_peca} removida com sucesso!")
        else:
            print(f"\n✗ Peça ID {id_peca} não encontrada!")
    
    except ValueError:
        print("\n✗ Erro: Digite um ID válido (número inteiro).")
    except Exception as e:
        print(f"\n✗ Erro ao remover peça: {e}")


def menu_listar_caixas():
    """Menu para listar caixas fechadas."""
    print("\n--- CAIXAS FECHADAS ---")
    caixas_fechadas = listar_caixas_fechadas()
    
    print(f"\n🔒 Total de caixas fechadas: {len(caixas_fechadas)}")
    print("-"*70)
    
    if len(caixas_fechadas) > 0:
        for caixa in caixas_fechadas:
            print(f"  • {formatar_caixa(caixa)}")
            print(f"    Peças armazenadas:")
            # Índice [1] contém a lista de peças
            for peca in caixa[1]:
                # Índices: [0]id, [1]peso, [2]cor, [3]comprimento
                print(f"      - ID: {peca[0]} | Peso: {peca[1]}g | Cor: {peca[2]} | Comprimento: {peca[3]}cm")
    else:
        print("  Nenhuma caixa fechada ainda.")


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """Função principal do programa."""
    print("\n🏭 BEM-VINDO AO SISTEMA DE GESTÃO DE PEÇAS")
    print("Controle de Qualidade e Armazenamento Automatizado")
    print("Versão: Programação Estruturada (apenas funções e listas)")
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            menu_cadastrar_peca()
        elif opcao == "2":
            menu_listar_pecas()
        elif opcao == "3":
            menu_remover_peca()
        elif opcao == "4":
            menu_listar_caixas()
        elif opcao == "5":
            print(gerar_relatorio())
        elif opcao == "0":
            print("\n👋 Encerrando o sistema...")
            print("Obrigado por utilizar o Sistema de Gestão de Peças!")
            break
        else:
            print("\n✗ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()