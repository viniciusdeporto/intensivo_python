glossario = {
    'dicionario': 'basicamente é um lugar que contem chave e valor.',
    'lista': 'listas em python são sequencia de coisas que contem indexação.',
    'tupla': 'tuplas sao iguais listas mas elas sao inalteraveis.',
    'string': 'strings são caracteres, ou palavras, ou frases, tudo que esta entre aspas simples ou dupla',
    'boleano': 'valors falsos ou verdadeiros',
}

for chave in glossario:
    print(f'{chave.title()}:\n {glossario[chave].title()}')