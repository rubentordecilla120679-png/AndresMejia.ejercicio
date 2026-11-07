
def menu():
  while True:
    print("MENU DE ESTUDIANTES")
    print("1. Ingresar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Estadística del salón")
    print("4. Ordenar estudiantes por nota")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
      ingresar_estudiante()
    elif opcion == "2":
      mostrar_estudiante()
    elif opcion == "3":
      estadistica_salon()
    elif opcion == "4":
      ordenar_estudiantes()
    elif opcion == "5":
      print("Fin del programa.")
      break
    else:
      print("Opcion no valida.")


estudiantes = []


def ingresar_estudiante():
  nombre = input("Nombre del estudiante: ")

  nota = float(input("Nota del estudiante (1 a 5): "))
  while nota < 1 or nota > 5:
    print("La nota debe estar entre 1 y 5.")
    nota = float(input("Ingresa la nota nuevamente: "))

  if nota >= 3.0:
    estado = "Ganó"
  else:
    estado = "Perdió"

  estudiante = {"nombre": nombre, "nota": nota, "estado": estado}

  estudiantes.append(estudiante)
  print("Estudiante guardado con éxito.")


def mostrar_estudiante():
  if len(estudiantes) == 0:
    print("No hay estudiantes registrados.")
  else:
    print("LISTA DE ESTUDIANTES")
    for est in estudiantes:
      print(
          "Nombre:",
          est["nombre"],
          "- Nota:",
          est["nota"],
          "- Estado:",
          est["estado"],
      )


def estadistica_salon():
  if len(estudiantes) == 0:
    print("No hay datos para mostrar.")
  else:
    total = len(estudiantes)
    suma = 0
    ganaron = 0
    perdieron = 0

    mayor = estudiantes[0]["nota"]
    menor = estudiantes[0]["nota"]
    estudiante_mejor = estudiantes[0]["nombre"]
    estudiante_peor = estudiantes[0]["nombre"]

    for est in estudiantes:
      nota_actual = est["nota"]
      suma += nota_actual

      
      if nota_actual > mayor:
        mayor = nota_actual
        estudiante_mejor = est["nombre"]

      
      if nota_actual < menor:
        menor = nota_actual
        estudiante_peor = est["nombre"]

      
      if est["estado"] == "Ganó":
        ganaron += 1
      else:
        perdieron += 1

    promedio_salon = suma / total

    print("ESTADÍSTICA GENERAL DEL SALON")
    print(f"Total de estudiantes: {total}")
    print(f"Promedio general del salón: {promedio_salon:.2f}")
    print(f"Estudiantes que ganaron: {ganaron}")
    print(f"Estudiantes que perdieron: {perdieron}")
    print(f"Mejor nota: {mayor} (Estudiante: {estudiante_mejor})")
    print(f"Peor nota: {menor} (Estudiante: {estudiante_peor})")

def obtener_nota(estudiante):
  return estudiante["nota"]


def ordenar_estudiantes():
  if len(estudiantes) == 0:
    print("No hay datos para mostrar.")
  else:
    
    estudiantes_ordenados = sorted(
        estudiantes, key=obtener_nota, reverse=True
    )

    print("ESTUDIANTES ORDENADOS POR NOTA")
    for i, est in enumerate(estudiantes_ordenados, 1):
      print(
          f"{i}. Nombre: {est['nombre']} - Nota: {est['nota']} - Estado:"
          f" {est['estado']}"
      )

   
    destacado = estudiantes_ordenados[0]
    print(
        f"\ Estudiante destacado: {destacado['nombre']} con una nota de"
        f" {destacado['nota']}"
    )
    
if __name__ == "__main__":
  menu()
  #gtrtv6ujb6k6bk