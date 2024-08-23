## Projeto: Análise de Petições Iniciais
***

Este projeto tem como objetivo criar uma equipe automatizada para analisar petições iniciais produzidas por advogados independentes. A equipe é composta por agentes especializados que realizam tarefas como mascaramento de dados sensíveis, análise jurídica, pesquisa de legislação e classificação das petições por assunto.

### Funcionalidades

O projeto possui quatro agentes principais, cada um responsável por uma tarefa específica:

Advogado Redator: Recebe uma petição inicial e mascara dados sensíveis como nomes de pessoas, RG e CPF, substituindo-os por máscaras como [nome], [RG], [CPF].
Analista de Petições: Revisa a petição inicial, identificando o fato, a tese jurídica e o pedido.
Especialista em Legislação Civil Brasileira: Analisa a tese jurídica e pesquisa leis, jurisprudências e precedentes que apoiem a tese apresentada.
Classificador de Fatos: Examina a seção dos fatos da petição e classifica a petição por assunto.

### Requisitos

Para rodar este projeto, você precisará de:

Python 3.8+
Dependências listadas em requirements.txt
Modelo de linguagem spaCy para português: pt_core_news_sm
Conta e chave de API da OpenAI (se optar por usar serviços da OpenAI)


### Instalação

1 - Clone o repositório:

```

git clone https://github.com/fabrycio30/legal-agents.git
cd legal-agents

```

2 - Montar um ambiente python para o projeto

```

python -m venv venv
source venv/bin/activate  
#Para SO Windows, use: venv\Scripts\activate

```


3 - Instalar dpendencias do projeto

``
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
``

4 - Configure as variáveis de ambiente no arquivo .env:

```

OPENAI_API_KEY=your_openai_api_key_here

```

### Executando o Projeto. 

Para rodar o projeto, execute o arquivo `main.py`:

```

python src/main.py

```
### Contribuição

Contribuições são bem-vindas! Caso queira contribuir, siga estas etapas:

i) Faça um fork do repositório.

ii) Crie uma branch para sua feature (git checkout -b minha-feature).

iii) Faça commit das suas alterações (git commit -m 'Adicionei uma nova feature').

iv) Envie para o branch (git push origin minha-feature).

v) Abra um Pull Request.


### Licença

Por enquanto são apenas experimentos iniciais, mas este projeto está sob a licença MIT. Em breve adicionarei o arquivo LICENSE para mais detalhes.

