from django import template

register = template.Library()

@register.filter
def custom_float_format(value):
    if value is None:
        return "No disponible"
    # Formatear el número
    value_str = f"{value:,.2f}"  # Formato estándar con comas
    formatted_value = value_str.replace(",", ".").replace(".", ",", 1)  # Cambia la primera coma por punto y el resto por coma
    return f"${formatted_value}"  # Agrega el símbolo de pesos

