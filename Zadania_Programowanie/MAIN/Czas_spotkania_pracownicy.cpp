#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <stack>
using namespace std;
struct przedzial
{
	int a, b, id;
	przedzial(int A = 0, int B = 0, int Id = 0)
	{
		a = A;
		b = B;
		id = Id;
	}
	bool operator<(przedzial drugi) const
	{

		return a < drugi.a;
	}
};
struct przedzialkolej
{
	int a, b, id;
	przedzialkolej(int A = 0, int B = 0, int Id = 0)
	{
		a = A;
		b = B;
		id = Id;
	}
	bool operator<(przedzialkolej drugi) const
	{

		return b > drugi.b;
	}
};

przedzial przedzialy[1 << 20];
priority_queue<przedzialkolej> q;
stack<int> temp1;
int tab[1 << 20], miejsce[1 << 20];
int main()
{
	int n, m, temp2, temp3, w = 1;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		scanf("%d %d", &temp3, &temp2);
		przedzialy[i] = przedzial(temp3, temp2, i + 1);
	}
	int ilosc = 0, max = 0;
	sort(przedzialy, przedzialy + n);
	/*	for(int i=0;i<n;i++){
		cout << przedzialy[i].a <<  " "<< przedzialy[i].b << endl;
 
	}
	*/
	//	cout << "XXXXXXXXXXXXXXX" << endl;
	int licz = 0;
	for (int i = 0; i < n; i++)
	{

		while (!q.empty() && q.top().b < przedzialy[i].a)
		{
			//	cout << q.top().b<< " " << przedzialy[i].a << endl;

			if (tab[q.top().id])
			{
				temp1.push(tab[q.top().id]);
				//	cout << temp1<< " " << q.top().id << "h" << endl ;
				tab[q.top().id] = 0;
			}
			q.pop();
		}
		//	cout << endl;
		q.push(przedzialkolej(przedzialy[i].a, przedzialy[i].b, przedzialy[i].id));
		if (licz < m)
		{
			tab[przedzialy[i].id] = w;
			miejsce[w] = przedzialy[i].id;

			w++;
			licz++;
		}
		if (q.size() > m)
		{
			//	cout << q.top().a << " " << q.top().b << endl;
			if (tab[q.top().id])
			{
				temp1.push(tab[q.top().id]);
				//	cout << temp1<< " " << q.top().id << "h" << endl ;
				tab[q.top().id] = 0;
			}
			q.pop();
		}
		if (q.size() >= m)
		{

			//	cout << q.top().b-przedzialy[i].a << endl;
			int h = 0;
			if (q.top().b - przedzialy[i].a > max)
			{
				while (!temp1.empty())
				{

					miejsce[temp1.top()] = przedzialy[i - h].id;
					//	cout << temp1.top() << " " << miejsce[temp1.top()]<< endl;
					temp1.pop();
					h++;
				}
				//	cout << endl;
				//for(int j=1;j<w;j++)cout << miejsce[j] << " ";
				//	cout << endl;
				//	cout << temp1 << "x" << endl;
				//	cout <<"HHHHA:"<< q.top().b << " " << przedzialy[i].a << endl;
				max = q.top().b - przedzialy[i].a;
			}
		}
	}
	printf("%d\n", max);
	for (int i = 1; i < w; i++)
		printf("%d ", miejsce[i]);
}
