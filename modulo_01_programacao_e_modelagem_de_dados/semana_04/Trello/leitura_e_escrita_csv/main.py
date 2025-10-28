def processar_vendas():
    with open('vendas.csv', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    with open('vendas_com_total.csv', 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write('produto,quantidade,preco,Total\n')
        
        for i in range(1, len(linhas)):
            linha = linhas[i].strip()
            valores = linha.split(',')
            produto = valores[0].strip()
            quantidade = float(valores[1].strip())
            preco = float(valores[2].strip())
            total = quantidade * preco
            arquivo_saida.write(f'{produto},{quantidade},{preco},{total}\n')
    
    print("Arquivo 'vendas_com_total.csv' criado com sucesso!")
    
    with open('vendas_com_total.csv', 'r', encoding='utf-8') as arquivo:
        print("\nConteúdo do arquivo gerado:")
        print(arquivo.read())

if __name__ == "__main__":
    processar_vendas()
