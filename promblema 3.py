#=====================================================================#
#  Curso: Fundamentos de Programación (Código: 213022)
#  Fase 5 - Evaluación Final POA
#  Estudiante: Juan David Calle Ceballos
#  Problema Elegido: Problema 3 - Auditoría de Inventario
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (función) que determina la cantidad exacta a pedir para un 
    artículo basado en la lógica de negocio.
    """
    if stock_actual < stock_minimo:
        # Si el Stock Actual es menor al Stock Mínimo, se pide la diferencia
        cantidad_pedir = stock_minimo - stock_actual
    else:
        # Si el Stock Actual es suficiente (mayor o igual), no se pide nada
        cantidad_pedir = 0
    return cantidad_pedir

def ejecutar_auditoria():
    print("==================================================")
    print("        SISTEMA DE AUDITORÍA DE INVENTARIO        ")
    print("==================================================\n")
    
    # Matriz con 5 artículos: [Código Artículo, Nombre, Stock Actual, Stock Mínimo]
    inventario_matriz = [
        ["A001", "Teclado Mecánico", 15, 20],
        ["A002", "Mouse Inalámbrico", 40, 30],
        ["A003", "Monitor Gamer 24'", 3, 10],
        ["A004", "Auriculares Bluetooth", 25, 25],
        ["A005", "Memoria USB 64GB", 8, 50]
    ]
    
    print("LISTA DE PEDIDOS A SOLICITAR:")
    print("--------------------------------------------------")
    
    # Recorrido de la matriz para procesar la información de cada artículo
    for articulo in inventario_matriz:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamado al módulo/función obligatorio
        cantidad_exacta = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Salida requerida: Imprimir nombre y cantidad exacta solicitada
        print(f"Artículo: {nombre:<25} | Cantidad a pedir: {cantidad_exacta}")
        
    print("--------------------------------------------------")
    print("Auditoría finalizada con éxito.")

# Bloque principal que inicia la ejecución del programa
if __name__ == "__main__":
    ejecutar_auditoria()
