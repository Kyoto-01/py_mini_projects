# Função p/ encontrar o endereço de rede
def find_net_address(ip_octects: list[str], subnet_len: int) -> str:
    qtd_full_net_octects = subnet_len // 8
    qtd_borrowed_bits = subnet_len % 8
    net_address = [ip_octects[i] for i in range(qtd_full_net_octects)]

    if qtd_full_net_octects > 0:
        last_oct = 255 - (2**(8 - qtd_full_net_octects)) + 1
        last_oct = str(last_oct)
        net_address.append(last_oct)
        qtd_full_net_octects += 1

    for i in range(qtd_full_net_octects, len(ip_octects)):
        net_address.append('0')

    return '.'.join(net_address)


ip_addr, net_length = input('Seu IPv4 e prefixo CIDR de rede: ').split('/')
ip_addr = ip_addr.split('.')
net_length = int(net_length)
subnet_length = input('Sua máscara de subrede em CIDR: ').replace('/', '')
subnet_length = int(subnet_length)

print(find_net_address(ip_addr, subnet_length))
