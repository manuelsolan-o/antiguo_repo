#ifndef PELICULA_H
#define PELICULA_H
#include <string>
#include <vector>
#include "Video.h"
using namespace std; 

class Pelicula : public Video {
    private: 
        string estudio;
        string director; 
        string actorP;
        string nacionalidad; 
    public: 
        Pelicula();
        Pelicula(int, string, string, string, int, int, int, string, string, string, string); 
        void muestraDatos(void); 
    
};

#endif