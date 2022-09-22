#include <iostream>
#include "Video.h"
#include "Pelicula.h"
#include "Serie.h"
using namespace std; 

int main() {
    Video *videos[3];;
    videos[0]=new Pelicula(1, "Pelicula", "Interestellar", "Ciencia ficcion", 100, 2014, 210, "Paramount Pictures", "Christopher Nolan", "Matthew McCounaghey", "Estadounidense");
    videos[1]=new Pelicula(2, "Pelicula", "Inception", "Ciencia ficcion", 99, 2010, 210, "Warner Bros", "Christopher Nolan", "Leonardo di Caprio", "Estadounidense");
    videos[2]=new Serie(3, "Serie", "Dark", "Ciencia Ficcion", 90, 2017, 60, "Baran bo Odar", "Aleman", 3, 26);
    videos[3]=new Serie(4, "Serie", "Peaky Blinders", "Drama", 85, 2013, 60, "Steven Knight", "Ingles", 6, 36);

    int option{}, calNueva{}, res{}, res2{}, res3{}, res4{}, res5{}; 
    do {
        cout << endl << "Bienvenido a tu servicio de calificacion de streaming" << endl; 
        cout << "-----------------------------" << endl; 
        cout << "Elige la opcion" << endl;
        cout << "1. Revisa los videos" << endl;
        cout << "2. Califica un video" << endl;
        cout << "3. Salir" << endl;

        cin >> option;
        if (option == 1){
            //Consulta los videos existentes
            cout << "Que datos desea ver? 1. Peliculas 2. Series: " << endl; 
            cin >> res;
            if (res==1){
                cout << "Pelicula 1." << videos[0]->getNombreVideo() << endl; 
                cout << "Pelicula 2." << videos[1]->getNombreVideo() << endl;
                cout << "Seleccionar: " << endl; 
                cin >> res2;
                if (res2==1) {
                    videos[0]->muestraDatos();

                } else if (res2==2){
                    videos[1]->muestraDatos();

                }

            } else if (res==2) {
                cout << "Serie 1." << videos[2]->getNombreVideo() << endl; 
                cout << "Serie 2." << videos[3]->getNombreVideo() << endl;
                cout << "Seleccionar: " << endl; 
                cin >> res3;
                if (res3==1) {
                    videos[2]->muestraDatos();

                } else if (res3==2){
                    videos[3]->muestraDatos();

                }

            }

        } else if (option == 2){
            //Califica un video 
            cout << "Calificar 1. Peliculas o 2. Videos : "<< endl;
            if (res4==1){
                cout << "Pelicula 1." << videos[0]->getNombreVideo() << endl; 
                cout << "Pelicula 2." << videos[1]->getNombreVideo() << endl;
                cout << "Seleccionar: " << endl; 
                cin >> res5;
                if (res5==1) {
                    cout << "Nueva calificación: " << endl; 
                    cin >> calNueva;
                    videos[0]->calificaVideo(calNueva);

                } else if (res5==2){
                    cout << "Nueva calificación: " << endl; 
                    cin >> calNueva;
                    videos[1]->calificaVideo(calNueva);

                }

            } else if (res4==2){
                cout << "Serie 1." << videos[2]->getNombreVideo() << endl; 
                cout << "Serie 2." << videos[3]->getNombreVideo() << endl;
                cout << "Seleccionar: " << endl; 
                cin >> res5;
                if (res5==1) {
                    cout << "Nueva calificación: " << endl; 
                    cin >> calNueva;
                    videos[2]->calificaVideo(calNueva);

                } else if (res5==2){
                    cout << "Nueva calificación: " << endl; 
                    cin >> calNueva;
                    videos[3]->calificaVideo(calNueva);

                }

            }

        }

    } while(option != 3);
    cout << "Gracias por usar el sistema de calificaicones :)" << endl; 

    return 0; 
}