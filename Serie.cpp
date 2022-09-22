#include <iostream>
#include <string>
#include "Serie.h"
using namespace std; 

Serie::Serie()
    : Video{}, director{""}, idioma{""}, numTemporadas{0}, capitulos_totales{0}{
}

Serie::Serie(int id, string tipoVideo, string nombreVideo, string genero, int calificacion, int añoLanamiento, int duracion, string dir, string idi, int numT, int capiT)
    : director{dir}, idioma{idi}, numTemporadas{numT}, capitulos_totales{capiT}{
}

void Serie::muestraDatos(void){
    Video::muestraDatos();
    cout << "Director: " << director << endl;
    cout << "Idioma: " << idioma << endl;
    cout << "Número de Temporadas: " << numTemporadas << endl;
    cout << "Capitulos Totales: " << capitulos_totales << endl; 
}