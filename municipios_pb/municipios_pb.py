def buscarMunicipios():
    csv_municipios = open('./municipios.csv', 'r', encoding='utf-8')
    dict_municipios = {}

    for mun in csv_municipios.read().splitlines():
        linha = mun.split(',')

        dict_municipios[linha[1]] = {
            'nome': linha[0],
            'gentilico': linha[2],
            'area': int(linha[3]),
            'populacao': int(linha[4]),
            'densidade': float(linha[5])
        }
    csv_municipios.close()
    return dict_municipios


municipios = buscarMunicipios()
while (cod := input('Código do município: ')) != 'fim':
    print(f'\n\n{f" CÓDIGO IBGE {cod} ":=^100}\n')
    print(f'Quem nasce em {municipios[cod]["nome"]} é {municipios[cod]["gentilico"]}')
    print(f'Área territorial: {municipios[cod]["area"]} km\u00b2 [2020]')
    print(f'População estimada: {municipios[cod]["populacao"]} pessoas [2020]')
    print(f'Densidade demográfica: {municipios[cod]["densidade"]} habitantes/km\u00b2 [2010]')
    print(f'\n{"":=^100}\n\n')
