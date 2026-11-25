import os

def calcular_precio(monto, cliente):
    if cliente == "VIP":
        return monto * 0.8
    return monto