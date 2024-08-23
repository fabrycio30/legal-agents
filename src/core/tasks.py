import yaml
from crewai import Task
from src.core.agents import advogado_redator, analista_peticions, especialista_legislacao, classificador_fatos
'''
# Tarefa de mascarar dados sigilosos contidos na petição inicial passada como entrada
mascarar_dados_task = Task(
    description='Mascarar dados sensíveis na petição inicial recebida, substituindo nomes, RG, CPF e outros dados por máscaras.',
    expected_output='Uma versão da petição inicial com dados sensíveis mascarados.',
    agent=advogado_redator
)

# Tarefa de análisar a petição e fazer a divisão entre as principais partes: Fato, Tese jurídica e Pedido. O foco que possa se utlizar
#essa seguimentação para explorar novas alternativas de Aprendizado de Máquina

analisar_peticao_task = Task(
    description='Revisar a petição e mapear fato, tese jurídica e pedido.',
    expected_output='Um resumo detalhado dos principais elementos da petição.',
    agent=analista_peticions
)

# Tarefa de verificação de legislação é um ideia ousada que seria interessante para acelerar vários processos no trinubal de justiça
verificar_legislacao_task = Task(
    description='Buscar leis e jurisprudências que apoiem a tese jurídica apresentada.',
    expected_output='Uma lista de leis e precedentes que suportam a tese jurídica.',
    agent=especialista_legislacao
)

# Tarefa de classificação de fatos utiliza a task de analisa da petição para tentar postioremente analisar os fatos e utizar ténicas menos 
#robustas e mais leves para juntar docs com o mesmo fatos e tal.
classificar_fatos_task = Task(
    description='Classificar a petição por assunto com base na seção de fatos.',
    expected_output='Uma classificação clara e precisa da petição por assunto.',
    agent=classificador_fatos
)
'''


# Carregando as configurações/descrições das tarefas d uma arquivo externo YAML
with open('src/config/tasks.yaml', 'r') as file:
    tasks_config = yaml.safe_load(file)

# Mapeamento de agentes pelo nome para associá-los às tarefas
agents_map = {
    'advogado_redator': advogado_redator,
    'analista_peticions': analista_peticions,
    'especialista_legislacao': especialista_legislacao,
    'classificador_fatos': classificador_fatos,
}

# Criar tarefas com base nas configurações YAML
mascarar_dados_task = Task(
    agent=agents_map[tasks_config['mascarar_dados_task']['agent']],
    description=tasks_config['mascarar_dados_task']['description'],
    expected_output=tasks_config['mascarar_dados_task']['expected_output']
)

analisar_peticao_task = Task(
    agent=agents_map[tasks_config['analisar_peticao_task']['agent']],
    description=tasks_config['analisar_peticao_task']['description'],
    expected_output=tasks_config['analisar_peticao_task']['expected_output']
)

verificar_legislacao_task = Task(
    agent=agents_map[tasks_config['verificar_legislacao_task']['agent']],
    description=tasks_config['verificar_legislacao_task']['description'],
    expected_output=tasks_config['verificar_legislacao_task']['expected_output']
)

classificar_fatos_task = Task(
    agent=agents_map[tasks_config['classificar_fatos_task']['agent']],
    description=tasks_config['classificar_fatos_task']['description'],
    expected_output=tasks_config['classificar_fatos_task']['expected_output']
)
