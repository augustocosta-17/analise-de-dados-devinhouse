with open("Manip_Arquivos/vendas.csv", "r", encoding="utf-8") as arq:
    vendas = {}
    for linha in arq.readlines()[1:]:
        data, produto, quantidade, valor = linha.strip().split(",")
        qtd = int(quantidade)
        val = float(valor)
        if produto not in vendas:
            vendas[produto] = {"total_vendido": 0, "valor_total": 0.0}
        vendas[produto]["total_vendido"] += qtd
        vendas[produto]["valor_total"] += qtd * val

with open("Manip_Arquivos/relatorio.csv", "w", encoding="utf-8") as arq:
    arq.write("Produto,Total Vendido,Valor Total\n")
    for produto, dados in vendas.items():
        arq.write(f"{produto},{dados['total_vendido']},{dados['valor_total']:.2f}\n")