// Función principal
void @main() {
  // Definir listas de títulos, taquillas y años
  List<String> titulos = ['Inception', 'Parasite', 'Interstellar', 'Whiplash'];
  List<double> taquillas = [829.89, 258.8, 677.5, 49.0];
  List<int> anios = [2010, 2019, 2014, 2014];

  // Función flecha para imprimir la descripción de una película
  var imprimirDescripcion = (int i) => print('${titulos[i]} (${anios[i]}) - Taquilla: \$${taquillas[i]} millones');

  // Imprimir descripciones de todas las películas
  for (int i = 0; i < titulos.length; i++) {
    imprimirDescripcion(i);
  }

  // Buscar una película específica por título
  String claveBuscada = 'Inception';
  int i = 0;
  while (i < titulos.length) {
    if (titulos[i] == claveBuscada) {
      print('Película encontrada: ${titulos[i]} (${anios[i]}) - Taquilla: \$${taquillas[i]} millones');
      break;
    }
    i++;
  }

  // Regla sencilla de sintaxis: función flecha para agregar una nueva película
  var agregarPelicula = (String titulo, double taquilla, int anio) {
    if (!titulos.contains(titulo)) {
      titulos.add(titulo);
      taquillas.add(taquilla);
      anios.add(anio);
      print('Película agregada: $titulo ($anio) - Taquilla: \$${taquilla} millones');
    } else {
      print('La película "$titulo" ya existe.');
    }
  };

  // Ejemplo de agregar una nueva película
  agregarPelicula('The Dark Knight', 1004.9, 2008);
