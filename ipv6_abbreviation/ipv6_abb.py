# IPv6 abbreviation rule 1
def remove_left_zeros(ipv6: str) -> str:
    abb_hextets = []
    for hextet in ipv6.split(':'):
        for char in hextet[:len(hextet) - 1]:
            if char != '0':
                break
            hextet = hextet[1:]
        abb_hextets.append(hextet)
    return ':'.join(abb_hextets)


# IPv6 abbreviation rule 2
def find_zero_sequence_hextets(ipv6: list[str]) -> list[dict[str: int]]:
    ipv6 = ipv6 + ['!']  # ! indica o fim da string, para quando o último char for igual a 0
    sequences = []

    # enquanto houver valores 0 na sublista de hextets, encontre o início e o fim da primeira sequência presente
    end = 0
    while '0' in ipv6[end:]:
        start = ipv6.index('0', end)

        for i in range(start, len(ipv6)):
            end = i
            if ipv6[i] != '0':
                sequences.append({'start': start, 'end': end - 1})
                break
    return sequences


# IPv6 abbreviation rule 2 (continuation)
def replace_zero_sequence_hextet(ipv6: str) -> str:
    # encontrar o maior intervalo de valores 0 seguidos e substituir por ::, se não houver maior, o primeiro é escolhido
    hextets = ipv6.split(':')
    sequences = find_zero_sequence_hextets(hextets)
    if len(sequences) != 0:
        sequences = sorted(sequences, key=lambda interval: interval['end'] - interval['start'], reverse=True)
        hextets = ':'.join(hextets[:sequences[0]['start']]) + '::' + ':'.join(hextets[sequences[0]['end'] + 1:])
        return hextets

    return ipv6


# Main function
def ipv6abb(ipv6: str) -> str:
    abb_ipv6 = remove_left_zeros(ipv6)
    abb_ipv6 = replace_zero_sequence_hextet(abb_ipv6)

    return abb_ipv6


# Test
if __name__ == '__main__':
    complete_ipv6 = input('Complete IPv6: ')
    print(f'Abbreviation -> {ipv6abb(complete_ipv6)}')
