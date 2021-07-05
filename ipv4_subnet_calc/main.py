ip, net_length = input('Seu IPv4 e prefixo CIDR de rede: ').split('/')
net_length = int(net_length)
subnet_length = input('Sua máscara de subrede em CIDR: ').replace('/', '')
subnet_length = int(subnet_length)

print(ip, net_length, subnet_length)

