# OLD STYLE
# email_tmpl = '''
# Olá, %(nome)s.
# Tem interesse em comprar %(produto)s?

# Este produto é ótimo para resolver %(texto)s

# Clique agora em %(link)s

# Apenas %(quantidade)d disponíveis!

# Preço promocional %(preco).2f
# '''

# clientes = ['Bruno', 'Carlos', 'Danilo', 'Joubert']

# for cliente in clientes:
#     print(email_tmpl % {
#             'nome': cliente,
#             'produto': 'caneta',
#             'texto': 'escreve muito bem!',
#             'link': 'https://www.canetasleais.com.br',
#             'quantidade': 10,
#             'preco': 5})

# NEW STYLE
email_tmpl = '''
Olá, {nome}.
Tem interesse em comprar {produto}?

Este produto é ótimo para resolver {problema}

Clique agora em {link}

Apenas {qtd} disponíveis!

Preço promocional {preco}
'''  # caso quira colocar a qtd correta {:%2.f}

clientes = ['Bruno', 'Carlos', 'Danilo', 'Joubert']

for cliente in clientes:
    print(email_tmpl.format(
        nome = cliente,
        produto = 'caneta',
        problema = 'texto',
        link = 'link',
        qtd = 10,
        preco = 5.0)
    )
