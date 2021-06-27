def add_left_zeros(ipv6: str) -> str:
    hextets, two_double_points_index = segment_hextets(ipv6)
    hextets = [f'{hextets[i]:0>4}' for i in range(len(hextets))]

    return ':'.join(hextets[:two_double_points_index]) + '::' + ':'.join(hextets[two_double_points_index:])


def add_missing_hextets(ipv6: str) -> str:
    hextets, two_double_points_index = segment_hextets(ipv6)
    zero_hextets = ['0000'] * (8 - len(hextets))

    hextets.insert(two_double_points_index, ':'.join(zero_hextets))
    return ':'.join(hextets)


def segment_hextets(ipv6: str) -> tuple:
    hextets = ipv6.replace('::', ':*:').split(':')
    hextets = list(filter(None, hextets))  # eliminação de espaços vazios ''
    two_double_points_index = hextets.index('*')
    hextets.remove('*')

    return hextets, two_double_points_index


if __name__ == '__main__':
    abbreviated_ipv6 = input('Abbreviated IPv6: ')
    abbreviated_ipv6 = add_left_zeros(abbreviated_ipv6)
    abbreviated_ipv6 = add_missing_hextets(abbreviated_ipv6)

    print(f'Complete -> {abbreviated_ipv6}')
