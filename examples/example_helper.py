from seal import scheme_type

def int_to_hex_string(value: int) -> str:
    return hex(value)[2:]

def print_parameters(context) -> None:
    context_data = context.key_context_data
    if context_data.parms.scheme == scheme_type.bfv:
        scheme_name = 'bfv'
    elif context_data.parms.scheme == scheme_type.ckks:
        scheme_name = 'ckks'
    else:
        scheme_name = 'none'
    print('/')
    print('| Encryption parameters')
    print('| scheme: ' + scheme_name)
    print(f'| poly_modulus_degree: {context_data.parms.poly_modulus_degree}')
    coeff_modulus = context_data.parms.coeff_modulus
    coeff_modulus_sum = 0
    for j in coeff_modulus:
        coeff_modulus_sum += j.bit_count
    print(f'| coeff_modulus size: {coeff_modulus_sum}(', end='')
    for i in range(len(coeff_modulus) - 1):
        print(f'{coeff_modulus[i].bit_count} + ', end='')
    print(f'{coeff_modulus[-1].bit_count}) bits')
    if context_data.parms.scheme == scheme_type.bfv:
        print(f'| plain_modulus: {context_data.parms.plain_modulus.value}')
    print('\\')

def print_vector(vec, print_size=4, prec=3) -> None:
    slot_count = len(vec)
    print()
    if slot_count <= 2*print_size:
        print('    [', end='')
        for i in range(slot_count):
            print(f' {vec[i]:.{prec}f}' + (',' if (i != slot_count - 1) else ' ]\n'), end='')
    else:
        print('    [', end='')
        for i in range(print_size):
            print(f' {vec[i]:.{prec}f},', end='')
        if slot_count > 2*print_size:
            print(' ...,', end='')
        for i in range(slot_count - print_size, slot_count):
            print(f' {vec[i]:.{prec}f}' + (',' if (i != slot_count - 1) else ' ]\n'), end='')
    print()

def print_matrix(matrix, row_size, print_size=5, prec=3):
    print()
    print("    [", end="")
    for i in range(print_size):
        print(f" {matrix[i]:.{prec}f},", end="")
    print(" ...,", end="")
    for i in range(row_size - print_size, row_size):
        print(f" {matrix[i]:.{prec}f}" + (',' if (i != row_size - 1) else ' ]\n'), end='')
    print("    [", end="")
    for i in range(row_size, row_size + print_size):
        print(f" {matrix[i]:.{prec}f},", end="")
    print(" ...,", end="")
    for i in range(2*row_size - print_size, 2*row_size):
        print(f" {matrix[i]:.{prec}f}" + (',' if (i != 2*row_size - 1) else ' ]\n'), end='')
    print()
