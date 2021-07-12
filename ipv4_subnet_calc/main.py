import subnet_calcs as snc

ip_addr, net_length = input('Seu IPv4 + prefixo CIDR de rede (formato -> x.x.x.x/x): ').split('/')
net_length = int(net_length)
subnet_length = input('Sua máscara de subrede em CIDR: ').replace('/', '')
subnet_length = int(subnet_length)

net_address = snc.find_net_address(ip_addr, subnet_length)
qtd_hosts_per_subnet = snc.find_qtd_hosts_per_subnet(subnet_length)
qtd_subnets = snc.find_qtd_subnets(net_length, subnet_length)
brd_address = snc.find_brd_address(net_address, qtd_hosts_per_subnet)
host_interval = snc.find_host_interval(net_address, brd_address)

print(f'\n* Endereço de rede: {net_address}/{subnet_length}')
print(f'* Endereço de broadcast: {brd_address}/{subnet_length}')
print(f'* Intervalo de hosts: {host_interval[0]}-{host_interval[1]}')
print(f'* Hosts por sub-rede: {qtd_hosts_per_subnet} hosts')
print(f'* Número de sub-redes: {qtd_subnets} sub-redes')
