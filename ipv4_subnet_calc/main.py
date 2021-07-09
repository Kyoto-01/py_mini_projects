def find_net_addr(ip, subnet_len):
    net_octs = subnet_len // 8
    qtd_net_octs = net_octs
    net_addr = [ip[i] for i in range(net_octs)]
    net_octs = subnet_len % 8

    if net_octs > 0:
        last_oct = 255 - (2**(8 - net_octs)) + 1
        last_oct = str(last_oct)
        net_addr.append(last_oct)
        qtd_net_octs += 1

    for i in range(qtd_net_octs, len(ip)):
        net_addr.append('0')

    print('.'.join(net_addr))


ip_addr, net_length = input('Seu IPv4 e prefixo CIDR de rede: ').split('/')
ip_addr = ip_addr.split('.')
net_length = int(net_length)
subnet_length = input('Sua máscara de subrede em CIDR: ').replace('/', '')
subnet_length = int(subnet_length)


print(ip_addr, net_length, subnet_length)

find_net_addr(ip_addr, subnet_length)
