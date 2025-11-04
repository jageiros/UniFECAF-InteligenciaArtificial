
Sistema de Gestão de Peças - (Funções e Listas)
1. Descrição do Projeto
Este sistema é uma implementação minimalista para o desafio de automação digital proposto pela disciplina de Algoritmos e Lógica de Programação. O objetivo desta versão é resolver o problema utilizando apenas os fundamentos da programação estruturada: funções e listas.
O programa simula o controle de qualidade e o armazenamento de peças em uma linha de produção, demonstrando como a lógica de programação pura, sem o uso de estruturas de dados complexas como classes ou dicionários, pode ser aplicada para criar uma solução funcional.
2. Estrutura de Dados: O Poder e o Perigo das Listas
Nesta implementação, todas as entidades do sistema (peças e caixas) são representadas por listas simples. A estrutura de dados depende de uma convenção de índices, onde cada posição na lista tem um significado fixo.
Estrutura da Peça
Cada peça é uma lista de 6 elementos:
---------------------------------------------
| |Índice | |Chave | |Tipo de Dado | |Descrição |
---------------------------------------------
| |0 | |id | |int | |Identificador único da peça. |
---------------------------------------------
| |1 | |peso | |float | |Peso da peça em gramas. |
---------------------------------------------
| |2 | |cor | |str | |Cor da peça. |
---------------------------------------------
| |3 | |comprimento | |float | |Comprimento da peça em centímetros. |
---------------------------------------------
| |4 | |aprovada | |bool | |True se a peça atende aos critérios, False caso contrário. |
---------------------------------------------
| |5 | |motivos | |list | |Lista de strings com os motivos da reprovação. |

Exemplo de uma peça: [1, 100.5, 'azul', 15.0, True, []]
Estrutura da Caixa
Cada caixa é uma lista de 3 elementos:
---------------------------------------------
| |Índice | |Chave | |Tipo de Dado | |Descrição |
---------------------------------------------
| |0 | |numero | |int | |Número identificador da caixa. |
---------------------------------------------
| |1 | |pecas | |list | |Lista contendo as peças (que também são listas) armazenadas. |
---------------------------------------------
| |2 | |fechada | |bool | |True se a caixa atingiu a capacidade máxima, False caso contrário. |

Exemplo de uma caixa: [1, [[...], [...]], False]
Atenção: Esta abordagem é poderosa para o aprendizado, mas frágil na prática. O código depende inteiramente da memorização e do uso correto dos índices. Uma pequena confusão (por exemplo, usar peca[2] esperando o peso em vez da cor) pode causar erros difíceis de rastrear.
3. Funcionalidades Principais
O sistema oferece as seguintes funcionalidades através de um menu interativo:
1. Cadastrar nova peça: Registra uma nova peça, valida sua qualidade e a armazena se for aprovada.
2. Listar peças aprovadas/reprovadas: Exibe listas de peças com base em seu status de aprovação.
3. Remover peça cadastrada: Exclui uma peça do sistema pelo seu ID.
4. Listar caixas fechadas: Mostra as caixas que já atingiram a capacidade máxima.
5. Gerar relatório final: Apresenta um resumo completo da produção.
4. Como Rodar o Programa
Pré-requisitos
* Python 3.6 ou superior.
Instruções de Execução
1. Salve o arquivo sistema_gestao_pecas_Disciplina.py em um diretório de sua escolha.
2. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo foi salvo.
3. Execute o seguinte comando:
python3 sistema_gestao_pecas_Disciplina.py

4. O menu interativo será exibido. Digite o número da opção desejada e pressione Enter para interagir com o sistema.
5. Análise da Abordagem
---------------------------------------------
| |Vantagens | |Desvantagens |
---------------------------------------------
| |✅ Simplicidade Fundamental: Utiliza apenas os conceitos mais básicos de Python, excelente para iniciantes. | |❌ Baixa Legibilidade: O código é poluído por "números mágicos" (índices), tornando-o difícil de entender. |
---------------------------------------------
| |✅ Foco na Lógica: Força o desenvolvedor a se concentrar no algoritmo e no fluxo de controle. | |❌ Alta Fragilidade: Uma mudança na estrutura da lista (ex: adicionar um novo campo) exige a revisão de todo o código. |
---------------------------------------------
| |✅ Leveza: Consome o mínimo de recursos, pois usa as estruturas de dados mais simples. | |❌ Manutenção Difícil: Depurar e estender o sistema é uma tarefa complexa e propensa a erros. |

6. Autor
Estudante do Curso de Tecnólogo em IA e Automação

UniFECAF - Disciplina de Algoritmos e Lógica de Programação