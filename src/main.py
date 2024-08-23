# src/main.py
from src.core.crew import crew

def main():
    # Verificar uma forma de passar o texto de uma petiçao inicial já estraidad do PDF.
    #Pegar uma da internet depsoi

    peticao_inicial = "João Silva, portador do RG 12345678 e CPF 123.456.789-00, solicita que..."
    
    # Mandar a petição inicial como input e seja o que Deus quiser kkkk
    result = crew.kickoff(inputs={'peticao_inicial': peticao_inicial})
    print(result)

if __name__ == "__main__":
    main()
