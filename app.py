import os
def calcular_precio(monto, cliente):
    descuento_sin_usar = 15
    if cliente == "VIP":
        if monto > 100:
            return monto * 0.8
        else:
            return monto * 0.8
    return monto
