from ingestion.gerador_transacoes import gerar_transacao
from database.conexao import salvar_transacao

def main():
    print("=== Plataforma de Análise Financeira e Risco ===")
    print("Status: Sistema inicializado com sucesso.\n")
    
    print("--- Ingerindo e Gravando Transações no MySQL ---")
    for i in range(1, 6):
        transacao = gerar_transacao()
        salvar_transacao(transacao)
        print(f"Transação {i} salva no banco de dados com sucesso!")

if __name__ == "__main__":
    main()