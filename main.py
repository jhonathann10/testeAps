import re

def validate_cpf(data_cpf):
    """Validate CPF function.

    Args: CPF to validate.

            # Entradas Incorretas:
             - 'abcdefghijk'
             - '123'
             - ''
             - None
             - '12345678900'

            # Entradas Corretas:
             - '95524361503'
             - '955.243.615-03'
             - 955 243 615 03'

    Returns:
        bool: Retorna True quando CPF é válido senão retorna False.
    """
    cpf = ''.join(re.findall('\d', str(data_cpf)))

    if (not cpf) or (len(cpf) < 11):
        return False

    # Gera últimos dois dígitos baseado nos primeiros nove.
    integers = list(map(int, cpf))
    new_value = integers[:9]

    while len(new_value) < 11:
        r = sum([(len(new_value) + 1 - i) * v for i, v in enumerate(new_value)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        new_value.append(f)

    # Se o número gerado é igual aos inteiros retorna True.
    if new_value == integers:
        return True
    return False

print(validate_cpf('123451231231'))