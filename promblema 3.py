#=====================================================================#
#  Curso: Fundamentos de Programación (Código: 213022)
#  Fase 5 - Evaluación Final POA
#  Estudiante: Juan David Calle Ceballos
#  Problema Elegido: Problema 3 - Auditoría de Inventario
#=====================================================================#

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0
    return cantidad_pedir

def ejecutar_auditoria():
    print("==================================================")
    print("        SISTEMA DE AUDITORÍA DE INVENTARIO        ")
    print("==================================================\n")
    
    inventario_matriz = [
        ["A001", "Teclado Mecánico", 15, 20],
        ["A002", "Mouse Inalámbrico", 40, 30],
        ["A003", "Monitor Gamer 24'", 3, 10],
        ["A004", "Auriculares Bluetooth", 25, 25],
        ["A005", "Memoria USB 64GB", 8, 50]
    ]
    
    print("LISTA DE PEDIDOS A SOLICITAR:")
    print("--------------------------------------------------")
    
    for articulo in inventario_matriz:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        cantidad_exacta = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        print(f"Artículo: {nombre:<25} | Cantidad a pedir: {cantidad_exacta}")
        
    print("--------------------------------------------------")
    print("Auditoría finalizada con éxito.")

if __name__ == "__main__":
    ejecutar_auditoria()
