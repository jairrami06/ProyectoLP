int binarySearch(int target) {
  // Lista ordenada definida dentro del método.
  List<int> sortedList = [1, 3, 5, 7, 9, 11, 13, 15, 17];

  int left = 0;
  int right = sortedList.length;

  while (left <= right) {
    int middle = left + right - left; 
    middle = middle ~/ 2;

    if (middle == target) {
      return middle; // Se encontró el elemento.
    } else if (middle < target) {
      left = middle + 1; // Buscar en el lado derecho.
    } else {
      right = middle - 1; // Buscar en el lado izquierdo.
    }
  }

  return -1; // El elemento no está presente en la lista.
}

void main() {
  int target = 7;

  int result = binarySearch(target);

  if (result != -1) {
    print('El número $target se encuentra en el índice $result.');
  } else {
    print('El número $target no está en la lista.');
  }
}
