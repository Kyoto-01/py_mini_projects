def convert_decimal_ip_to_binary(ip: str) -> str:
	converted_ip = ip.split('.')
	converted_ip = [f'{int(octect):0>8b}' for octect in converted_ip]
	converted_ip = ''.join(converted_ip)

	return converted_ip


def convert_binary_ip_to_decimal(ip: str) -> str:
	converted_ip = [str(int(ip[i:i + 8], 2)) for i in range(0, len(ip), 8)]
	converted_ip = '.'.join(converted_ip)
	return converted_ip


def convert_cidr_to_binary_mask(cidr: int) -> str:
	bin_mask = '1' * cidr
	bin_mask = f'{bin_mask:0<32}'

	return bin_mask


def and_operation(bin1: str, bin2: str) -> str:
	result = ''
	for bit_b1, bit_b2 in zip(bin1, bin2):
		and_op = int(bit_b1) * int(bit_b2)
		result += str(and_op)

	return result
