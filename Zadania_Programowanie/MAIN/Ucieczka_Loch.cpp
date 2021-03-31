#include <iostream>
#include <cstdio>
#include <string>
#include <queue>
using namespace std;

int xstart, ystart, xkoniec, ykoniec;
string *labirynt;
void droga(int limitx, int limity)
{
	queue<int> pozycjax, pozycjay;
	int x, y;
	int i, j;
	pozycjax.push(xstart);
	pozycjay.push(ystart);
	while (!pozycjax.empty())
	{
		x = pozycjax.front();
		pozycjax.pop();
		y = pozycjay.front();
		pozycjay.pop();
		if (x == xkoniec && y == ykoniec)
			break;
		for (i = -1; i <= 1; i++)
		{
			for (j = -1; j <= 1; j++)
			{
				if (i != j && (!i || !j))
				{
					if ((y + i >= 0 && y + i < limity) && (x + j >= 0 && x + j < limitx))
						if (labirynt[y + i][x + j] == '.' || labirynt[y + i][x + j] == '+')
						{
							if (i == -1)
								labirynt[y + i][x + j] = 'd';
							else if (i == 1)
								labirynt[y + i][x + j] = 'g';
							else if (j == -1)
								labirynt[y + i][x + j] = 'p';
							else if (j == 1)
								labirynt[y + i][x + j] = 'l';
							pozycjax.push(x + j);
							pozycjay.push(y + i);
						}
				}
			}
		}
	}
}
int dlugosc(int limitx, int limity)
{
	char znak;
	int x, y, wynik = 0;
	x = xkoniec;
	y = ykoniec;

	while (true)
	{
		if (x == xstart && y == ystart)
			break;
		if (x < 0 || x >= limitx)
			break;
		if (y < 0 || y >= limity)
			break;
		znak = labirynt[y][x];
		switch (znak)
		{
		case 'd':
		{
			y++;
			wynik++;
			break;
		}
		case 'g':
		{
			y--;
			wynik++;
			break;
		}
		case 'p':
		{
			x++;
			wynik++;
			break;
		}
		case 'l':
		{
			x--;
			wynik++;
			break;
		}
		}
	}
	return wynik;
}
int main()
{
	int z, i, j, k, x, y;
	scanf("%i", &z);
	for (i = 0; i < z; i++)
	{
		xstart = ystart = xkoniec = ykoniec = -1;
		scanf("%i %i", &x, &y);
		labirynt = new string[x];
		for (j = 0; j < x; j++)
		{
			cin >> labirynt[j];
			for (k = 0; k < y; k++)
			{
				if (labirynt[j][k] == '@')
				{
					xstart = k;
					ystart = j;
				}
				if (labirynt[j][k] == '>')
				{
					xkoniec = k;
					ykoniec = j;
					labirynt[j][k] = '.';
				}
			}
		}
		if (xkoniec == ykoniec && xkoniec == -1)
		{
			printf("NIE\n");
		}
		else
		{
			droga(y, x);
			if (labirynt[ykoniec][xkoniec] == '.')
				printf("NIE\n");
			else
				printf("%i\n", dlugosc(y, x));
		}
	}
	return 0;
}
