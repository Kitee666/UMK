#include <iostream>
using namespace std;
int wartosc(char znak)
{
    if (znak >= '0' && znak <= '9')
        return znak - 48;
    else if (znak >= 'A' && znak <= 'Z')
        return znak - 55;
    else if (znak >= 'a' && znak <= 'z')
        return znak - 61;
}
int sprawdzanie(int dlugosc, string liczba, int podstawa)
{
    if (podstawa < 2 || podstawa > 62)
        return -1;
    if (dlugosc >= 0)
        return (wartosc(liczba[dlugosc]) + sprawdzanie(dlugosc - 1, liczba, podstawa)) % podstawa;
    else
        return 0;
}

int main()
{
    string liczba;
    int podstawa = 1;
    while (cin >> liczba >> podstawa)
    {
        if (podstawa == 0)
            break;
        cout << "Liczba " << liczba << "(" << podstawa << "): ";
        if (sprawdzanie(liczba.size() - 1, liczba, podstawa - 1) == 0)
            cout << "jest podsystemowa\n";
        else
            cout << "jest normalna\n";
    }
    return 0;
}
