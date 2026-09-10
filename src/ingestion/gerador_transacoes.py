import random
from datetime import datetime

def gerar_transacao():
    """Gera um dicionário representando uma única transação financeira."""
    tipos = ["PIX", "CARTAO_CREDITO", "BOLETO", "TED"]
    
    transacao = {
        "transacao_id": random.randint(100000, 999999),
        "cliente_id": random.randint(1000, 1050),
        "valor": round(random.uniform(5.00, 5000.00), 2),
        "tipo": random.choice(tipos),
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return transacao

if __name__ == "__main__":
    print(gerar_transacao())