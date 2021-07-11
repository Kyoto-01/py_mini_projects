import conversions_and_operations as conop


# Função p/ encontrar o endereço de rede
def find_net_address(ip: str, subnet_cidr: int) -> str:
    ip_bin = conop.convert_decimal_ip_to_binary(ip)
    cidr_bin = conop.convert_cidr_to_binary_mask(subnet_cidr)
    net_addr = conop.and_operation(ip_bin, cidr_bin)
    net_addr = conop.convert_binary_ip_to_decimal(net_addr)

    return net_addr


ip_addr, net_length = input('Seu IPv4 e prefixo CIDR de rede: ').split('/')
net_length = int(net_length)
subnet_length = input('Sua máscara de subrede em CIDR: ').replace('/', '')
subnet_length = int(subnet_length)

print(find_net_address(ip_addr, subnet_length))
