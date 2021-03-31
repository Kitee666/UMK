typedef unsigned char BYTE;
#include <iostream>
using namespace std;
int main() {
    int liczbaT;
    float liczba;
    BYTE * temp =( BYTE * ) & liczba;
    int * temp2 =( int * ) & liczba;
    cin >> liczbaT;

    while( liczbaT ) {
        cin >> liczba;
        cout << hex <<( int ) *( temp + 3 ) << " " <<( int ) *( temp + 2 ) << " " <<( int ) *( temp + 1 ) << " " <<( int ) *( temp ) << endl;
        liczbaT--;
    }
}
