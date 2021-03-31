#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
long long int x1 = 0, y12 = 0, x2 = 0, y2 = 0, x3 = 0, y3 = 0, x4 = 0, y4 = 0, xp = 0, yp = 0, ym = 0, xm = 0;
unsigned long long int suma1 = 0, suma2 = 0, suma3 = 0, suma4 = 0;
unsigned long long int nowa1(long long x, long long y, unsigned long long int ss)
{
    unsigned long long int suma;
    suma = x * x + y * y;
    if (suma > ss)
    {
        x1 = x;
        y12 = y;
    }
    return suma;
}
unsigned long long int nowa2(long long x, long long y, unsigned long long int ss)
{
    unsigned long long int suma;
    suma = x * x + y * y;
    if (suma > ss)
    {
        x2 = x;
        y2 = y;
    }
    return suma;
}
unsigned long long int nowa3(long long x, long long y, unsigned long long int ss)
{
    unsigned long long int suma;
    suma = x * x + y * y;
    if (suma > ss)
    {
        x3 = x;
        y3 = y;
    }
    return suma;
}
unsigned long long int nowa4(long long x, long long y, unsigned long long int ss)
{
    unsigned long long int suma;
    suma = x * x + y * y;
    if (suma > ss)
    {
        x4 = x;
        y4 = y;
    }
    return suma;
}
void sprawdzanie(int x, int y, long long x1, long long x2, long long x3, long long x4, long long y12, long long y2, long long y3, long long y4)
{
    /*
        |
    2   |   1
        |
--------+--------
        |
    3   |   4
        |

*/
    if (x == 0)
    {
        if (y > 0)
        {
            yp += y;
            return;
        }
        else
        {
            ym += y;
            return;
        }
    }
    else if (y == 0)
    {
        if (x > 0)
        {
            xp += x;
            return;
        }
        else
        {
            xm += x;
            return;
        }
    }
    if (x > 0 && y > 0)
    {
        // 1
        suma1 = max(suma1, nowa1(x1 + x, y12 + y, suma1));
        suma2 = max(suma2, nowa2(x2 + x, y2 + y, suma2));
        suma4 = max(suma4, nowa4(x4 + x, y4 + y, suma4));
        return;
    }
    else if (x < 0 && y > 0)
    {
        // 2
        suma1 = max(suma1, nowa1(x1 + x, y12 + y, suma1));
        suma2 = max(suma2, nowa2(x2 + x, y2 + y, suma2));
        suma3 = max(suma3, nowa3(x3 + x, y3 + y, suma3));
        return;
    }
    else

        if (x < 0 && y < 0)
    {
        // 3
        suma2 = max(suma2, nowa2(x2 + x, y2 + y, suma2));
        suma3 = max(suma3, nowa3(x3 + x, y3 + y, suma3));
        suma4 = max(suma4, nowa4(x4 + x, y4 + y, suma4));
        return;
    }
    else if (x > 0 && y < 0)
    {
        // 4
        suma1 = max(suma1, nowa1(x1 + x, y12 + y, suma1));
        suma3 = max(suma3, nowa3(x3 + x, y3 + y, suma3));
        suma4 = max(suma4, nowa4(x4 + x, y4 + y, suma4));
        return;
    }
}
unsigned long long int max_in()
{
    if (suma1 > suma2 && suma1 > suma3 && suma1 > suma4)
        return suma1;
    else if (suma2 > suma3 && suma2 > suma4)
        return suma2;
    else if (suma3 > suma4)
        return suma3;
    else
        return suma4;
}
int main()
{
    int n, x, y, i;
    scanf("%i", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%i", &x);
        scanf("%i", &y);
        sprawdzanie(x, y, x1, x2, x3, x4, y12, y2, y3, y4);
    }
    cout << max_in();

    return 0;
}
