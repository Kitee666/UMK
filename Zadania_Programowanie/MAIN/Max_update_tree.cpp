#include <iostream>
#include <cstdio>
#include <cmath>
#include <limits.h>
int maks(int x, int y)
{
    return (x > y) ? x : y;
}
int srodkowy(int s, int e)
{
    return s + (e - s) / 2;
}
int szukajwartosci(int *tree, int poczatek, int koniec, int start, int meta, int index)
{
    if (start <= poczatek && meta >= koniec)
        return tree[index];
    if (koniec < start || poczatek > meta)
        return -INT_MAX;
    int srodek = srodkowy(poczatek, koniec);
    return maks(szukajwartosci(tree, poczatek, srodek, start, meta, 2 * index + 1), szukajwartosci(tree, srodek + 1, koniec, start, meta, 2 * index + 2));
}

int szukaj(int *tree, int n, int start, int meta)
{
    return szukajwartosci(tree, 0, n - 1, start, meta, 0);
}

int tworzeniedrzewa(int tab[], int poczatek, int koniec, int *tree, int aktualny)
{
    if (poczatek == koniec)
    {
        tree[aktualny] = tab[poczatek];
        return tab[poczatek];
    }
    int srodek = srodkowy(poczatek, koniec);
    tree[aktualny] = maks(tworzeniedrzewa(tab, poczatek, srodek, tree, aktualny * 2 + 1),
                          tworzeniedrzewa(tab, srodek + 1, koniec, tree, aktualny * 2 + 2));
    return tree[aktualny];
}
int *drzewo(int tab[], int n)
{
    int x = (int)(ceil(log2(n)));
    int max_size = 2 * (int)pow(2, x) - 1;
    int *tree = new int[max_size];
    tworzeniedrzewa(tab, 0, n - 1, tree, 0);
    return tree;
}
void updatetree(int *tree, int poczatek, int koniec, int i, int nowa, int aktualny)
{
    if (i < poczatek || i > koniec)
        return;
    if (koniec != poczatek)
    {
        int srodek = srodkowy(poczatek, koniec);
        updatetree(tree, poczatek, srodek, i, nowa, 2 * aktualny + 1);
        updatetree(tree, srodek + 1, koniec, i, nowa, 2 * aktualny + 2);
    }
    if (koniec == poczatek)
    {
        if (poczatek == i)
        {
            tree[aktualny] = nowa;
            return;
        }
    }
    tree[aktualny] = maks(tree[aktualny * 2 + 1], tree[aktualny * 2 + 2]);
}
void update(int tab[], int *tree, int n, int i, int nowa)
{
    tab[i] = nowa;
    updatetree(tree, 0, n - 1, i, nowa, 0);
}
int main()
{
    int n, i, y, a, b;
    scanf("%d %d", &n, &y);
    char co[6];
    int tab[200000];
    for (i = 0; i < n; i++)
        scanf("%d", &tab[i]);
    n = sizeof(tab) / sizeof(tab[0]);
    int *tree = drzewo(tab, n);
    for (i = 0; i < y; i++)
    {
        scanf("%s", &co);
        scanf("%d %d", &a, &b);
        if (co[0] == 'M')
            printf("%d\n", szukaj(tree, n, a - 1, b - 1));
        else
            update(tab, tree, n, a - 1, b);
    }
    return 0;
}
