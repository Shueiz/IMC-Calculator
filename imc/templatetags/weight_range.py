from django import template

register = template.Library()
@register.filter(name="Tabela")
def weight_range(imc_value):
    if imc_value < 18.5:
        return 'Abaixo do Peso'
    elif 18.5 <= imc_value < 24.9:
        return 'Peso Normal'
    elif 25 <= imc_value < 29.9:
        return 'Sobrepeso'
    elif 30 <= imc_value < 34.9:
        return 'Obesidade Grau I'
    elif 35 <= imc_value < 39.9:
        return 'Obesidade Grau II'
    else:
        return 'Obesidade Grau III'
    