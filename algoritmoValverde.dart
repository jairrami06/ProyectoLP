void main() {
  // Definimos el número de Avogadro
  const double numeroDeAvogadro = 6.02214076e23;

  // Función para convertir moles a moléculas
  double molesAMoleculas(double moles) {
    return moles * numeroDeAvogadro;
  }

  // Función para convertir moléculas a moles
  double moleculasAMoles(double moleculas) {
    return moleculas / numeroDeAvogadro;
  }

  double moles = 2.0;
  double moleculas = molesAMoleculas(moles);
  print('$moles moles es igual a $moleculas moléculas.');

  moleculas = 1.20442815e24;
  moles = moleculasAMoles(moleculas);
  print('$moleculas moléculas es igual a $moles moles.');
}
