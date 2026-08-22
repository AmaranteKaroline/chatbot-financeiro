import pandas as pd

# Carrega seus gastos - usa o mesmo csv do Projeto 1
# Cria um gastos.csv com colunas: Data, Descricao, Categoria, Valor
try:
    df = pd.read_csv('gastos.csv')
    print("💜 Base de gastos carregada!")
except:
    # Se não tiver csv, cria dados falsos pra testar
    dados = {
        'Descricao': ['iFood Burger', 'Uber ida', 'Mercado Extra', 'iFood Pizza', 'Uber volta'],
        'Categoria': ['Alimentação', 'Transporte', 'Mercado', 'Alimentação', 'Transporte'],
        'Valor': [35.90, 22.50, 150.00, 42.00, 18.00]
    }
    df = pd.DataFrame(dados)
    print("Usando dados de exemplo")

def responder(pergunta):
    pergunta = pergunta.lower()
    
    # Pergunta 1: quanto gastei em X?
    if "gastei em" in pergunta or "gastos com" in pergunta:
        for categoria in df['Categoria'].unique():
            if categoria.lower() in pergunta:
                total = df[df['Categoria'].str.lower() == categoria.lower()]['Valor'].sum()
                return f"Você gastou R$ {total:.2f} em {categoria} 💸"
        return "Não encontrei essa categoria. Tente: Alimentação, Transporte, Mercado"

    # Pergunta 2: maior gasto
    if "maior gasto" in pergunta:
        maior = df.loc[df['Valor'].idxmax()]
        return f"Seu maior gasto foi R$ {maior['Valor']:.2f} com {maior['Descricao']} ({maior['Categoria']})"

    # Pergunta 3: total
    if "total" in pergunta:
        total = df['Valor'].sum()
        return f"Você gastou R$ {total:.2f} no total esse mês"

    return "Posso responder: 'quanto gastei em alimentação?', 'qual meu maior gasto?', 'total gasto'"

# Loop do ChatBot
print("\n🤖 Olá! Sou seu assistente financeiro. Digite 'sair' para terminar.\n")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() == 'sair':
        print("Assistente: Até logo! 💜")
        break
    resposta = responder(pergunta)
    print(f"Assistente: {resposta}\n")
