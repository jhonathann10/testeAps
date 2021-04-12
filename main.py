import re
import pandas as pd

def validate_cpf(data_cpf):

    cpf = ''.join(re.findall('\d', str(data_cpf)))

    if (not cpf) or (len(cpf) < 11):
        return False

    integers = list(map(int, cpf))
    new_value = integers[:9]

    while len(new_value) < 11:
        r = sum([(len(new_value) + 1 - i) * v for i, v in enumerate(new_value)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        new_value.append(f)

    if new_value == integers:
        return True
    return False

df = pd.read_csv("base_teste.txt")
tam_lista = len(df)
for i in df:
    df['cpf_valido'] = df['cpf'].apply(validate_cpf)

print(f"DataFrame: {df}")