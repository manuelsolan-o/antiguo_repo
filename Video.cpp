#include <string>
#include <iostream>
#include "Video.h"
using namespace std; 

Video::Video() 
    : id{0}, tipoVideo{""}, nombreVideo{""}, genero{""}, calificacion{0}, añoLanzamiento{0}, duracion{0}{

}

Video::Video(int ID, string tipoV, string nombre, string gen, int cal, int año, int dur)
    : id{ID}, tipoVideo{tipoV}, nombreVideo{nombre}, genero{gen}, calificacion{cal}, añoLanzamiento{año}, duracion{dur} {

}

void Video::calificaVideo(int cal){
    if (cal < 0 || cal >= 6){
        cout << "Calificacion inválida" << endl; 
        return; 
    }
    calificacion = cal; 
}

string Video::getNombreVideo(void){
    return nombreVideo; 
}

void Video::muestraDatos(void){
    cout << "ID: " << id << endl; 
    cout << "Tipo: " << tipoVideo << endl;
    cout << "Nombre: " << nombreVideo << endl;
    cout << "Genero: " << genero << endl;
    cout << "Calificacion: " << calificacion << endl;
    cout << "Ano Lanzamiento: " << añoLanzamiento << endl;
    cout << "Duracion (minutos): " << duracion << endl;
}
