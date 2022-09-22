#include <iostream>
#include <string>
#include "Pelicula.h"
using namespace std; 

Pelicula::Pelicula()
    : Video{}, estudio{""}, director{""}, actorP{""}, nacionalidad{""} {
}

Pelicula::Pelicula(int id, string tipoVideo, string nombreVideo, string genero, int calificacion, int añoLanamiento, int duracion, string est, string dir, string act, string nac)
    : estudio{est}, director{dir}, actorP(act), nacionalidad{nac} {
        
}

void Pelicula::muestraDatos(void){
    Video::muestraDatos();
    cout << "Estudio: " << estudio << endl; 
    cout << "Director: " << director << endl;
    cout << "Actores: " << actorP << endl; 
    cout << "Nacionalidad: " << nacionalidad << endl;
}