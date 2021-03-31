#include <iostream>
#include <cstdio>
using namespace std;
int max(int a, int b)
{
	if (a > b)
	{
		return a;
	}
	else
	{
		return b;
	}
}

int szukaj(int start, int koniec, string ciag)
{
	if (start == koniec)
	{
		if (ciag[start] == '0')
			return 1;
		else
			return 0;
	}
	int srodek = (start + koniec) / 2;
	if (srodek == start)
	{
		if (ciag[srodek] == '0')
			return 1 + szukaj(srodek + 1, koniec, ciag);
		else
			return szukaj(srodek + 1, koniec, ciag);
	}
	else
	{
		if (ciag[srodek] == '0')
			return 1 + szukaj(start, srodek - 1, ciag) + szukaj(srodek + 1, koniec, ciag);
		else
			return max(szukaj(start, srodek - 1, ciag), szukaj(srodek + 1, koniec, ciag));
	}
}
int main()
{
	int i, z, d, x;
	cin >> d >> x;
	string ciag;
	cin >> ciag;
	for (i = 0; i < x; i++)
	{
		cin >> z;
		z--;
		if (ciag[z] == '0')
			ciag[z] = '1';
		else
			ciag[z] = '0';
		cout << szukaj(0, d - 1, ciag) << endl;
	}
	return 0;
}
