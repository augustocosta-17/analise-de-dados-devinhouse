João = ['Arroz', 'Feijão', 'Macarrão', 'Peixe']
Maria = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Ovos']

conjunto_joao = set(João)
conjunto_maria = set(Maria)

listacombinada = conjunto_joao | conjunto_maria
emcomum = conjunto_joao & conjunto_maria

print("Itens em comum em cada uma das listas:", emcomum)
print("Itens que só a Maria comprou:", conjunto_maria - conjunto_joao)
print("Itens que só o João comprou:", conjunto_joao - conjunto_maria)
print("Itens das duas listas juntos:", listacombinada)