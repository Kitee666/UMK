#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <cmath>

MainWindow::MainWindow(QWidget* parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    szer = ui->rysujFrame->width();
    wys = ui->rysujFrame->height();
    poczX = ui->rysujFrame->x();
    poczY = ui->rysujFrame->y();
    img = new QImage(szer, wys, QImage::Format_RGB32);
    copy = new QImage(szer, wys, QImage::Format_RGB32);
    czysc();
    *copy = img->copy();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_exitButton_clicked()
{
    qApp->quit();
}
void MainWindow::paintEvent(QPaintEvent*)
{
    QPainter p(this);
    p.drawImage(poczX, poczY, *img);
}
void MainWindow::on_cleanButton_clicked()
{
    czysc();
    update();
}
void MainWindow::czysc()
{
    unsigned char* ptr;
    ptr = img->bits();
    licznik = 0;
    kontrola = false;
    punkty.clear();
    int i, j;
    for (i = 0; i < wys; i++) {
        for (j = 0; j < szer; j++) {
            ptr[szer * 4 * i + 4 * j] = 255;
            ptr[szer * 4 * i + 4 * j + 1] = 255;
            ptr[szer * 4 * i + 4 * j + 2] = 255;
        }
    }
    *copy = img->copy();
}
void MainWindow::mousePressEvent(QMouseEvent* event)
{
    int x = event->x();
    int y = event->y();
    *img = copy->copy();
    x -= poczX;
    y -= poczY;
    if (event->button() == Qt::LeftButton) {
        if ((x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
        }
    }
    else {
        if ((x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
            sprawdz(x, y);
        }
    }
    krzywe();
    punkt();
    update();
}
void MainWindow::mouseReleaseEvent(QMouseEvent* event)
{
    int x = event->x();
    int y = event->y();
    *img = copy->copy();
    x -= poczX;
    y -= poczY;
    if (event->button() == Qt::LeftButton) {
        if ((x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
            if (usun) {
                sprawdz(x, y);
                if (kontrola) {
                    punkty.erase(przesun);
                    licznik--;
                    kontrola = false;
                }
            }
            else if (!usun) {
                punkty.push_back(make_pair(x, y));
                licznik++;
            }
        }
    }
    else {
        if (kontrola == true && (x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
            pair<double, double> przesuniety;
            przesuniety = make_pair(x, y);
            *przesun = przesuniety;
            kontrola = false;
        }
    }
    krzywe();
    punkt();
    update();
}
void MainWindow::mouseMoveEvent(QMouseEvent* event)
{
    int x = event->x();
    int y = event->y();
    *img = copy->copy();
    x -= poczX;
    y -= poczY;
    if (event->button() == Qt::LeftButton) {
    }
    else {
        if (kontrola == true && (x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
            pair<double, double> przesuniety;
            przesuniety = make_pair(x, y);
            *przesun = przesuniety;
        }
    }
    krzywe();
    punkt();
    update();
}
void MainWindow::rysujPunkty(int x, int y, int r, int g, int b, int size)
{
    int i, j;
    for (i = x - size; i <= x + size; i++) {
        for (j = y - size; j <= y + size; j++) {
            rysujPiksel(i, j, r, g, b);
        }
    }
}
void MainWindow::rysujPiksel(int x, int y, int r, int g, int b)
{
    unsigned char* ptr;
    ptr = img->bits();
    if (x >= 0 && y >= 0 && x < szer && y < wys) {
        ptr[szer * 4 * y + 4 * x] = static_cast<unsigned char>(b);
        ptr[szer * 4 * y + 4 * x + 1] = static_cast<unsigned char>(g);
        ptr[szer * 4 * y + 4 * x + 2] = static_cast<unsigned char>(r);
    }
}
void MainWindow::prosta(int startx, int starty, int koniecx, int koniecy, int r, int g, int c)
{
    double a, b;
    int pom;
    int i;
    if (abs(startx - koniecx) > abs(starty - koniecy)) {
        if (startx > koniecx) {
            pom = startx;
            startx = koniecx;
            koniecx = pom;
            pom = starty;
            starty = koniecy;
            koniecy = pom;
        }
        a = (koniecy - starty) / static_cast<double>(koniecx - startx);
        b = starty - a * startx;
        for (i = startx; i <= koniecx; i++) {
            pom = static_cast<int>(a * i + b);
            rysujPiksel(i, pom, r, g, c);
        }
    }
    else {
        if (starty > koniecy) {
            pom = startx;
            startx = koniecx;
            koniecx = pom;
            pom = starty;
            starty = koniecy;
            koniecy = pom;
        }
        a = (koniecx - startx) / static_cast<double>(koniecy - starty);
        b = startx - a * starty;
        for (i = starty; i <= koniecy; i++) {
            pom = static_cast<int>(a * i + b);
            rysujPiksel(pom, i, r, g, c);
        }
    }
}
void MainWindow::sprawdz(int x, int y)
{
    for (vector<pair<double, double> >::iterator it = punkty.begin(); it != punkty.end(); it++) {
        if (it->first + 5 >= x && it->first - 5 <= x && it->second + 5 >= y && it->second - 5 <= y) {
            przesun = it;
            kontrola = true;
            return;
        }
    }
}
void MainWindow::punkt()
{
    if (punkty.empty())
        return;
    pair<double, double> pkt_1;
    pkt_1 = *(punkty.begin());
    for (vector<pair<double, double> >::iterator it = punkty.begin(); it != punkty.end(); it++) {
        rysujPunkty(static_cast<int>(it->first), static_cast<int>(it->second), 255, 0, 0, 5);
        prosta(static_cast<int>(pkt_1.first), static_cast<int>(pkt_1.second), static_cast<int>(it->first), static_cast<int>(it->second), 0, 0, 255);
        pkt_1 = *(it);
    }
}
void MainWindow::krzywe()
{
    if(punkty.size() <= 1) return;
    double **wzor = new double*[2];
    int i, j, n;
    vector<pair<double, double> > delta;
    pair<double, double> pkt_1, pkt_2;

    wzor[0] = new double[licznik];
    wzor[1] = new double[licznik];

    for(i = 0; i < licznik; i++) {
        wzor[0][i] = 0.0;
        wzor[1][i] = 0.0;
    }
    /* 1 t t^2 t^3 ... */
    for(i = 0; i < licznik; i++) {
        n = newton(licznik - 1, i);
        for(j = 0; j < licznik - i; j++) {
            wzor[0][j + i] += punkty[static_cast<unsigned long long>(i)].first * pow(-1, j) * newton(licznik - i - 1, j) * n;
            wzor[1][j + i] += punkty[static_cast<unsigned long long>(i)].second * pow(-1, j) * newton(licznik  - i - 1, j) * n;
        }
    }

    pkt_1 = punkty[0];
    for(i = 1; i < static_cast<int>(punkty.size()); i++) {
        pkt_2 = punkty[static_cast<unsigned long long>(i)];
        delta.push_back(make_pair(pkt_2.first - pkt_1.first, pkt_2.second - pkt_1.second));
        pkt_1 = pkt_2;
    }
    double odl = 0.0;
    for(i = 0; i < static_cast<int>(delta.size()); i++) {
        odl = max(odl, sqrt(delta[static_cast<unsigned long long>(i)].first * delta[static_cast<unsigned long long>(i)].first + delta[static_cast<unsigned long long>(i)].second * delta[static_cast<unsigned long long>(i)].second));
    }
    odl *= (licznik - 1);
    qDebug() << "Licznik" << odl;
    int step = static_cast<int>(ceil(odl));
    double x, y, t;
    for(i = 0; i <= step; i++) {
        t = static_cast<double>(i) / static_cast<double>(step);
        x = y = 0.0;
        for(j = 0; j <= licznik; j++) {
            x += wzor[0][j] * pow(t, j);
            y += wzor[1][j] * pow(t, j);
        }
        qDebug() << static_cast<int>(x) << " " << static_cast<int>(y);
        rysujPiksel(static_cast<int>(x), static_cast<int>(y), 0, 0, 0);
    }

    delete [] wzor[0];
    delete [] wzor[1];
    delete [] wzor;
}



int MainWindow::newton(int n, int k)
{
    int i, wynik = 1;
    if (k == 0 || k == n) {
        return wynik;
    }
    /* zmienic wywowylanie na rekurencje */
    for(i = 1; i <= k; i++) {
        wynik = wynik * (n - i + 1) / i;
    }
    return wynik;
}

void MainWindow::podnies_stopien()
{
    vector<pair<double, double> > old(punkty);
    unsigned long long i, n = old.size();
    pair<double, double> pkt_1, pkt_2;
    double x, y;
    punkty.clear();
    for (i = 0; i <= n; i++) {
        if (i == 0) {
            punkty.push_back(old[0]);
        }
        else if (i == n) {
            punkty.push_back(old[n - 1]);
        }
        else {
            pkt_1 = old[i - 1];
            pkt_2 = old[i];
            x = static_cast<double>(i) / static_cast<double>(n) * pkt_1.first + static_cast<double>(n - i) / static_cast<double>(n) * pkt_2.first;
            y = static_cast<double>(i) / static_cast<double>(n) * pkt_1.second + static_cast<double>(n - i) / static_cast<double>(n) * pkt_2.second;
            punkty.push_back(make_pair(x, y));
        }
    }
    licznik++;
    *img = copy->copy();
    krzywe();
    punkt();
    update();
}

void MainWindow::on_pushButton_clicked()
{
    *img = copy->copy();
    krzywe();
    punkty.clear();
    licznik = 0;
    kontrola = false;
    *copy = img->copy();
    update();
}

void MainWindow::on_checkBox_stateChanged(int arg1)
{
    if (arg1) {
        usun = true;
    }
    else {
        usun = false;
    }
}

void MainWindow::on_pushButton_2_clicked()
{
    podnies_stopien();
}
