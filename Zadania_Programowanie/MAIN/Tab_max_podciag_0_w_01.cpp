#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int i, z, d, x, j;
	scanf("%i %i", &d, &x);
	int maxyma[500001] = {0}, max[500001] = {0}, max1 = 0, max2 = 0, max3 = 0, start, koniec;
	string ciag;
	cin >> ciag;
	/* Dopisujemy do tablic lewo i prawo stronne ciagi */
	for (i = 0; i < d; i++)
	{
		if (ciag[i] == '0')
			max1++;
		if (max1 > max3)
			max3 = max1;
		if (ciag[i] == '1')
		{
			max[i] = -1;
			max1 = 0;
		}
		else if (ciag[i] == '0' && i == d - 1)
		{
			max[i] = max1;
			max[i - max1 + 1] = max1;
			maxyma[max1]++;
			max1 = 0;
		}
		else if (ciag[i] == '0' && ciag[i + 1] == '1')
		{
			max[i] = max1;
			max[i - max1 + 1] = max1;
			maxyma[max1]++;
			max1 = 0;
		}
	}
	for (i = 0; i < x; i++)
	{

		scanf("%i", &z);
		z--;
		start = -1;
		koniec = -1;
		/* Jezeli bylo 1 to zamieniamy na 0 */
		if (ciag[z] == '1')
		{
			if (z == 0)
				start = 0;
			if (z == d - 1)
				koniec = z;
			/* Jezeli jest to poczatek */
			if (start == z)
			{

				if (max[z + 1] == -1)
				{
					/* Jezeli nastepna jest 1 to zamien wartosc na 1*/
					max[z] = 1;
					maxyma[1]++;
					if (max[z] > max3)
						max3 = max[z];
				}
				else
				{
					/* Jezeli nastepna jest 0 to zamien i dodaj 1 oraz na koniec przedzialu dodaj 1*/
					koniec = max[start + 1];
					maxyma[max[koniec]]--;
					max[1] = 0;
					max[koniec] = koniec + 1;
					max[z] = max[koniec];
					maxyma[max[z]]++;
					if (max[koniec] > max3)
						max3 = max[koniec];
				}
			}
			else if (koniec == z)
			{
				/* Jezeli koniec */
				/* Jezeli poprzednia jest 1 to zamien wartosc i dodaj wynik */
				if (max[z - 1] == -1)
				{
					maxyma[1]++;
					max[z] = 1;
					if (max[z] > max3)
						max3 = max[z];
				}
				else
				{
					/* Jezeli poprzednia jest 0 to zamien i dodaj 1 oraz na poczatek przedzialu dodaj 1 */
					start = z - max[z - 1];
					maxyma[max[z - 1]]--;
					max2 = max[z - 1];
					max[z - 1] = 0;
					max[start] = max2 + 1;
					max[koniec] = max[start];
					maxyma[max[koniec]]++;
					if (max[koniec] > max3)
						max3 = max[koniec];
				}
			}
			else
			{
				/* Jezeli zamiana jest pomiedzy */
				/* Jezeli poprzednia jest 1 */
				if (max[z - 1] == -1)
				{
					/* Jezeli poprzednia i nastepna jest 1 to zamien wartosc na 1*/
					if (max[z + 1] == -1)
					{
						max[z] = 1;
						maxyma[max[z]]++;
						if (max[z] > max3)
							max3 = max[z];
					}
					else
					{
						/* Jezeli poprzednia jest 1 a nastepna jest 0 to zamien i dodaj 1 oraz na koniec przedzialu dodaj 1*/
						start = z;
						koniec = z + max[z + 1];
						maxyma[max[koniec]]--;
						max[z] = koniec - start + 1;
						max[z + 1] = 0;
						max[koniec] = max[z];
						maxyma[max[koniec]]++;
						if (max[koniec] > max3)
							max3 = max[koniec];
					}
				}
				else if (max[z + 1] == -1)
				{
					/* Jezeli nastpena jest 1 a poprzednia 0 */
					koniec = z;
					start = z - max[z - 1];
					maxyma[max[z - 1]]--;
					max[koniec] = koniec - start + 1;
					max[z - 1] = 0;
					max[start] = max[koniec];
					maxyma[max[z]]++;
					if (max[start] > max3)
						max3 = max[start];
				}
				else
				{
					/* Jezeli poprzednia i nastepna jest 0 */
					start = z - max[z - 1];
					koniec = z + max[z + 1];
					maxyma[max[z - 1]]--;
					maxyma[max[z + 1]]--;
					max[z] = 0;
					max[z - 1] = 0;
					max[z + 1] = 0;
					max[start] = koniec - start + 1;
					max[koniec] = max[start];
					maxyma[max[start]]++;
					if (max[start] > max3)
						max3 = max[start];
				}
			}
			ciag[z] = '0';
		}
		else
		{
			/* Jezeli bylo 0 to zamieniamy na 1 */
			/* Jezeli jest to poczatek */
			if (z == 0)
			{
				/* Jezeli suma to 1, bylo tylko jedno 0 na poczatku */
				if (max[z] == 1)
				{
					max[z] = -1;
					maxyma[1]--;
				}
				else
				{
					/* Jezeli nastepne to 0, roznica dodaj jeden i zastap oraz na koniec przedzialu */
					start = z + 1;
					koniec = max[z] - 1;
					maxyma[max[z]]--;
					max[start] = koniec - start + 1;
					max[z] = -1;
					max[koniec] = max[start];
					maxyma[max[koniec]]++;
				}
			}
			else if (z == d - 1)
			{
				/* Jezeli jest to koniec */
				/* Jezeli suma to 1, bylo tylko jedno 0 na koncu */
				if (max[z] == 1)
				{
					max[z] = -1;
					maxyma[1]--;
				}
				else
				{
					/* Jezeli poprzednie to 0, roznica dodaj jeden i zastap oraz na koniec przedzialu */
					koniec = z - 1;
					start = z - max[z];
					maxyma[max[z]]--;
					max[z] = -1;
					max[start] = koniec - start + 1;
					max[koniec] = max[start];
					maxyma[max[start]]++;
				}
			}
			else
			{
				/* Jezeli zamiana jest pomiedzy */
				/* Jezeli poprzednia jest 1 */
				if (max[z - 1] == -1)
				{
					/* Jezeli nastepna jest 1, to suma jeden*/
					if (max[z + 1] == -1)
					{
						max[z] = -1;
						maxyma[1]--;
					}
					else
					{
						/* Jezeli poprzednia jest 1 a nastepna 0 zastap sume minus jeden i zamien na koncu przedzialu*/
						start = z + 1;
						koniec = max[z] + z - 1;
						maxyma[max[z]]--;
						max[z] = -1;
						max[start] = koniec - start + 1;
						max[koniec] = max[start];
						maxyma[max[start]]++;
					}
				}
				else if (max[z + 1] == -1)
				{
					/* Jezeli nastepna jest 1 a poprzednia 0, zastap sume minus jeden i zamien na poczatku przedzialu*/
					koniec = z - 1;
					start = z - max[z] + 1;
					maxyma[max[start]]--;
					max[z] = -1;
					max[koniec] = koniec - start + 1;
					max[start] = max[koniec];
					maxyma[max[start]]++;
				}
				else
				{
					/* Jezeli trafilismy na same 0 kolo nas, szukaj poczatku przedzialu */
					start = z;
					while (max[start] == 0)
						start--;
					maxyma[max[start]]--;
					max[z] = -1;
					koniec = max[start] + start - 1;
					/* Zamien przedzial od poczatku do zamienionej minus jeden */
					max[start] = z - start;
					max[z - 1] = max[start];
					maxyma[max[start]]++;
					/* Zamien przedzial od zmienionej plus do konca */
					max[koniec] = koniec - z;
					max[z + 1] = max[koniec];
					maxyma[max[koniec]]++;
				}
			}
			ciag[z] = '1';
			if (maxyma[max3] == 0)
				for (j = max3; j > 0; j--)
					if (maxyma[j] != 0)
					{
						max3 = j;
						break;
					}
		}
		printf("%i\n", max3);
	}
	return 0;
}
