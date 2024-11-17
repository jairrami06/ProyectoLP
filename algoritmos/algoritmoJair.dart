import 'dart:io';

void main() {
  print('¡Bienvenido al Buscador de Números Primos!');
  print('Ingrese el rango donde buscar primos.');

  // Leer rango del usuario
  stdout.write('Inicio del rango: ');
  int? rangoInicio = int.tryParse(stdin.readLineSync() ?? '');
  stdout.write('Fin del rango: ');
  int? rangoFin = int.tryParse(stdin.readLineSync() ?? '');

  // Validar entrada
  if (rangoInicio == null || rangoFin == null || rangoInicio > rangoFin || rangoInicio < 2) {
    print('Por favor, ingrese un rango válido (mayor o igual a 2).');
    return;
  }

  // Encontrar números primos
  List<int> primos = encontrarPrimos(rangoInicio, rangoFin);

  if (primos.isEmpty) {
    print('No se encontraron números primos en el rango proporcionado.');
    return;
  }

  // Mostrar los resultados
  print('Números primos encontrados: $primos');
  mostrarEstadisticas(primos);

  // Guardar resultados en un archivo
  guardarEnArchivo(primos, 'primos.txt');
  print('Los resultados se han guardado en el archivo "primos.txt".');
}

List<int> encontrarPrimos(int inicio, int fin) {
  List<bool> esPrimo = List.filled(fin + 1, true);
  esPrimo[0] = esPrimo[1] = false;

  for (int i = 2; i * i <= fin; i++) {
    if (esPrimo[i]) {
      for (int j = i * i; j <= fin; j += i) {
        esPrimo[j] = false;
      }
    }
  }

  List<int> primos = [];
  for (int k = inicio; k <= fin; k++) {
    if (esPrimo[k]) {
      primos.add(k);
    }
  }
  return primos;
}

void mostrarEstadisticas(List<int> primos) {
  int suma = primos.reduce((a, b) => a + b);
  double promedio = suma / primos.length;
  int maximo = primos.last;
  int minimo = primos.first;

  print('Estadísticas de los números primos encontrados:');
  print('Cantidad de números primos: ${primos.length}');
  print('Suma de los números primos: $suma');
  print('Promedio de los números primos: ${promedio.toStringAsFixed(2)}');
  print('Primo más pequeño: $minimo');
  print('Primo más grande: $maximo');
}

void guardarEnArchivo(List<int> primos, String nombreArchivo) {
  File archivo = File(nombreArchivo);
  archivo.writeAsStringSync('Números primos: ${primos.join(', ')}', mode: FileMode.write);
}
