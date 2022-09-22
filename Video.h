#ifndef VIDEO_H
#define VIDEO_H
#include <string>
using namespace std; 

class Video {
    protected: //protected para pasarlos a sus clases derivadas 
        int id; 
        string tipoVideo; 
        string nombreVideo;
        string genero;
        int calificacion; 
        int añoLanzamiento; 
        int duracion; 

    public: 
        Video();
        Video(int, string, string, string, int, int, int);
        string getNombreVideo();
        void calificaVideo(int);
        virtual void muestraDatos(void);

};

#endif