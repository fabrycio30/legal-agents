from crewai import Agent
import yaml

'''
#Agentes
advogado_redator = Agent(
    role='Advogado Redator',
    goal='Mascarar dados sensíveis na petição inicial recebida.',
    backstory='Você é um advogado experiente que assegura a privacidade e proteção de dados em documentos jurídicos.',
    memory=True,
    verbose=True
)
analista_peticions = Agent(
    role='Analista de Petições',
    goal='Revisar a petição e identificar o fato, a tese jurídica e o pedido.',
    backstory='Você é um analista detalhista, especializado em revisar petições jurídicas.',
    memory=True,
    verbose=True
)
especialista_legislacao = Agent(
    role='Especialista em Legislação Civil Brasileira',
    goal='Procurar leis, jurisprudências e precedentes que apoiem a tese jurídica da petição.',
    backstory='Você é um jurista com profundo conhecimento em direito civil brasileiro.',
    memory=True,
    verbose=True
)
classificador_fatos = Agent(
    role='Classificador de Fatos',
    goal='Classificar a petição por assunto com base na seção de fatos.',
    backstory='Você é um analista com expertise em classificação e organização de documentos jurídicos.',
    memory=True,
    verbose=True
)
'''


# Carregando as configurações/descrições dos agentes d uma arquivo externo YAML
with open('src/config/agents.yaml', 'r') as file:
    agents_config = yaml.safe_load(file)

# Criar agentes com base nas configurações YAML
advogado_redator = Agent(**agents_config['advogado_redator'])
analista_peticions = Agent(**agents_config['analista_peticions'])
especialista_legislacao = Agent(**agents_config['especialista_legislacao'])
classificador_fatos = Agent(**agents_config['classificador_fatos'])
