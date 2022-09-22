#ifndef SERIE_H
#define SERIE_H
#include <string>
#include "Video.h"
using namespace std; 

class Serie: public Video {
    private: 
        string director; 
        string idioma; 
        int numTemporadas; 
        int capitulos_totales;
    public: 
        Serie();
        Serie(int, string, string, string, int, int, int, string, string, int, int);
        void muestraDatos(void);

};

#endif