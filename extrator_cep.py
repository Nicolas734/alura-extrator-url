import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

# 5 digitos + hifen (opcional) + 3 digitos

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
padrao = re.compile("[0-9]{5}[-]{0,1}?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)


#padrao para o cep exemplo xxx.xxx.xxx-xx

#  [0-9]{3}[.]{1}?[0-9]{3}[.]{1}?[0-9]{3}[-]{1}?[0-9]{2}

