#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
void wypisz1(int blad)
{
	char skos = 92;
	string l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14;
	// 0 bledow
	l1 = "+---------------------+\n";
	l2 = "|    ____________     |\n";
	l3 = "|    |/               |\n";
	l4 = "|    |                |\n";
	l5 = "|    |                |\n";
	l6 = "|    |                |\n";
	l7 = "|    |                |\n";
	l8 = "|    |                |\n";
	l9 = "|    |                |\n";
	l10 = "|    |                |\n";
	l11 = "|    |                |\n";
	l12 = "|    |                |\n";
	l13 = "|  __|__              |\n";
	l14 = "+---------------------+\n";
	//1 blad
	if (blad >= 1)
	{
		l3 = "|    |/         |     |\n";
		l4 = "|    |          |     |\n";
		l5 = "|    |          |     |\n";
		l6 = "|    |          &     |\n";
	}
	// 2 blady
	if (blad >= 2)
	{
		l5 = "|    |         (_)    |\n";
		l6 = "|    |          &     |\n";
	}
	// 3 bledy
	if (blad >= 3)
	{
		l7 = "|    |          |     |\n";
		l8 = "|    |          |     |\n";
		l9 = "|    |          |     |\n";
	}
	// 4 bledy
	if (blad >= 4)
	{
		l7 = "|    |         /|     |\n";
		l8 = "|    |        / |     |\n";
		l9 = "|    |          |     |\n";
	}
	// 5 bledow
	if (blad >= 5)
	{
		l7 = "|    |         /|";
		l7 += skos;
		l7 += "    |\n";
		l8 = "|    |        / | ";
		l8 += skos;
		l8 += "   |\n";
		l9 = "|    |          |     |\n";
	}
	// 6 bledow
	if (blad >= 6)
	{
		l10 = "|    |         /      |\n";
		l11 = "|    |        /       |\n";
	}
	// 7 bledow
	if (blad >= 7)
	{
		l10 = "|    |         / ";
		l10 += skos;
		l10 += "    |\n";
		l11 = "|    |        /   ";
		l11 += skos;
		l11 += "   |\n";
	}

	cout << l1 << l2 << l3 << l4 << l5 << l6 << l7 << l8 << l9 << l10 << l11 << l12 << l13 << l14;
}

int main()
{
	int i, j, k, l, a, b, c, bledy, zostalo;
	string slowo, sekret, proby, znaki, poprawne;
	char znak;
	bool prawda, wstaw, wypis;
	cin >> a;
	for (i = 0; i < a; i++)
	{
		bledy = 0;
		slowo = "";
		proby = "-";

		cout << "Welcome to the Hangman Game!\n";
		wypisz1(bledy);
		cout << "Secret word:\n";
		cin >> sekret;

		for (j = 0; j < sekret.size(); j++)
			sekret[j] = toupper(sekret[j]);
		poprawne = sekret;
		zostalo = sekret.size();
		for (j = 0; j < zostalo; j++)
		{
			if (j > 0)
				cout << " ";
			slowo += "_";
			cout << slowo[j];
		}
		cout << endl
			 << endl;
		znaki = "";
		cin >> b;
		for (j = 0; j < b; j++)
		{
			cin >> znak;
			znaki += znak;
		}
		for (j = 0; j < b; j++)
		{
			znak = znaki[j];
			wypis = false;
			cout << "Number of mistakes left: " << 7 - bledy << endl;
			cout << "Guesses: " << proby << endl;
			if (j == 0)
				proby = "";
			cout << "Please guess a letter!\n";
			cout << "Your choice: " << znak << endl;
			int ascii = znak;
			// nie litera
			if (ascii < 65 || (ascii > 90 && ascii < 97) || ascii > 122)
			{
				cout << "Only Latin alphabet letters!\n";
				bledy++;
				wypis = true;
			}
			else
			{
				znak = toupper(znak);
				prawda = true;
				for (k = 0; k < proby.size(); k++)
				{
					if (proby[k] == znak)
					{
						prawda = false;
						break;
					}
				}
				// czy byla juz uzyta
				if (!prawda)
				{
					cout << "You've already guessed that letter!\n";
					bledy++;
					wypis = true;
				}
				else
				{
					wstaw = false;
					proby += znak;
					for (k = 0; k < sekret.size(); k++)
					{
						if (sekret[k] == znak)
						{
							wstaw = true;
							slowo[k] = znak;
							zostalo--;
						}
					}
					// czy byla w slowie
					if (!wstaw)
					{
						cout << "Nope!\n";
						bledy++;
						wypis = true;
					}
					else
					{
						// czy wstawiona
						if (wstaw && zostalo > 0)
						{
							cout << "Nice!\n";
							cout << "Secret word:\n";
							for (k = 0; k < slowo.size(); k++)
							{
								if (k > 0)
									cout << " ";
								cout << slowo[k];
							}
							cout << endl;
						}
						else // czy wygrana
							if (wstaw && zostalo == 0)
						{
							cout << "\n";
							cout << "You won!\n"
								 << "Secret: " << poprawne;
							j = b;
						}
					}
				}
			}
			// czy jakis blad
			if (wypis)
				wypisz1(bledy);
			cout << "\n";
			// limit bledow przegrana
			if (bledy == 7)
			{
				cout << "Game Over!\n"
					 << "Secret: " << poprawne << endl;
				j = b;
			}
		}
		cout << endl;
	}
	return 0;
}
