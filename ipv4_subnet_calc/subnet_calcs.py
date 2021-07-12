import conversions_and_operations as conop


# Função p/ encontrar o endereço de rede
def find_net_address(ip: str, subnet_cidr: int) -> str:
	ip_bin = conop.convert_decimal_ip_to_binary(ip)
	cidr_bin = conop.convert_cidr_to_binary_mask(subnet_cidr)
	net_addr = conop.and_operation(ip_bin, cidr_bin)
	net_addr = conop.convert_binary_ip_to_decimal(net_addr)

	return net_addr


def find_brd_address(net_address: str, qtd_hosts_in_subnet: int) -> str:
	bin_net_address = conop.convert_decimal_ip_to_binary(net_address)
	brd_address = f'{(int(bin_net_address, 2) + qtd_hosts_in_subnet + 1):0>32b}'
	brd_address = conop.convert_binary_ip_to_decimal(brd_address)

	return brd_address


def find_host_interval(net_address: str, brd_address: str) -> tuple:
	bin_net_address = conop.convert_decimal_ip_to_binary(net_address)
	bin_brd_address = conop.convert_decimal_ip_to_binary(brd_address)

	first_host = f'{(int(bin_net_address, 2) + 1):0>32b}'
	first_host = conop.convert_binary_ip_to_decimal(first_host)
	last_host = f'{(int(bin_brd_address, 2) - 1):0>32b}'
	last_host = conop.convert_binary_ip_to_decimal(last_host)

	return first_host, last_host


def find_qtd_hosts_per_subnet(subnet_cidr: int) -> int:
	return (2 ** (32 - subnet_cidr)) - 2


def find_qtd_subnets(net_cidr: int, subnet_cidr: int) -> int:
	return 2 ** (subnet_cidr - net_cidr)
