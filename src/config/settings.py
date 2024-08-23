
import os
from dotenv import load_dotenv

# basicamente para usar a chave da openai que terá de ser configurada no arquivo .env
load_dotenv()

# Exemplo de chave de API da OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")