from crewai import Crew, Process
from src.core.tasks import mascarar_dados_task, analisar_peticao_task, verificar_legislacao_task, classificar_fatos_task

# Criação da equipe de agentes com o framework crew.ai
crew = Crew(
    agents=[mascarar_dados_task.agent, analisar_peticao_task.agent, verificar_legislacao_task.agent, classificar_fatos_task.agent],
    tasks=[mascarar_dados_task, analisar_peticao_task, verificar_legislacao_task, classificar_fatos_task],
    process=Process.sequential
)
