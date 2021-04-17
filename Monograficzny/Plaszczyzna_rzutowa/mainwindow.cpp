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

    szer2 = ui->frame->width();
    wys2 = ui->frame->height();
    poczX2 = ui->frame->x();
    poczY2 = ui->frame->y();

    img = new QImage(szer, wys, QImage::Format_RGB32);
    img2= new QImage(szer2, wys2, QImage::Format_RGB32);
    copy = new QImage(szer, wys, QImage::Format_RGB32);
    copy2 = new QImage(szer, wys, QImage::Format_RGB32);
    czysc();
    prosta(img->bits(), szer / 2, 0, szer / 2, wys, 0, 0, 0);
    prosta(img->bits(), 0, wys / 2, szer,  wys / 2, 0, 0, 0);
    prosta(img2->bits(), szer2 / 2, 0, szer2 / 2, wys2, 0, 0, 0);
    prosta(img2->bits(), 0, wys2 / 2, szer2,  wys2 / 2, 0, 0, 0);
    *copy = img->copy();
    *copy2 = img2->copy();
    punkty.push_back(make_pair(szer / 2 - 50, wys / 2 + 50));
    punkty.push_back(make_pair(szer / 2 + 50, wys / 2 - 50));
    punkt();
    update();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::paintEvent(QPaintEvent*)
{
    QPainter p(this);
    p.drawImage(poczX, poczY, *img);
    p.drawImage(poczX2, poczY2, *img2);
}

void MainWindow::czysc()
{
    kontrola = false;
    int i, j;
    for (i = 0; i < wys; i++) {
        for (j = 0; j < szer; j++) {
            rysujPiksel(img->bits(), i, j, 255, 255, 255);
            rysujPiksel(img2->bits(), i, j, 255, 255, 255);
        }
    }
}
void MainWindow::mousePressEvent(QMouseEvent* event)
{
    int x = event->x() - poczX;
    int y = event->y() - poczY;
    *img = copy->copy();
    *img2 = copy2->copy();
    if ((x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
        sprawdz(x, y);
    }
    punkt();
    update();
}
void MainWindow::mouseReleaseEvent(QMouseEvent* event)
{
    int x = event->x() - poczX;
    int y = event->y() - poczY;
    *img = copy->copy();
    *img2 = copy2->copy();
    if (kontrola == true && (x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
        pair<double, double> przesuniety;
        przesuniety = make_pair(x, y);
        *przesun = przesuniety;
        kontrola = false;
    }
    punkt();
    update();
}
void MainWindow::mouseMoveEvent(QMouseEvent* event)
{
    int x = event->x() - poczX;
    int y = event->y() - poczY;
    *img = copy->copy();
    *img2 = copy2->copy();
    if (kontrola == true && (x >= 0) && (y >= 0) && (x < szer) && (y < wys)) {
        pair<double, double> przesuniety;
        przesuniety = make_pair(x, y);
        *przesun = przesuniety;
    }
    punkt();
    update();
}

void MainWindow::rysujPunkty(unsigned char *ptr, int x, int y, int r, int g, int b, int size)
{
    int i, j;
    for (i = x - size; i <= x + size; i++) {
        for (j = y - size; j <= y + size; j++) {
            rysujPiksel(ptr, i, j, r, g, b);
        }
    }
}

void MainWindow::rysujPiksel(unsigned char *ptr, int x, int y, int r, int g, int b)
{
    if (x >= 0 && y >= 0 && x < szer && y < wys) {
        ptr[szer * 4 * y + 4 * x] = static_cast<unsigned char>(b);
        ptr[szer * 4 * y + 4 * x + 1] = static_cast<unsigned char>(g);
        ptr[szer * 4 * y + 4 * x + 2] = static_cast<unsigned char>(r);
    }
}

void MainWindow::prosta(unsigned char *ptr, int startx, int starty, int koniecx, int koniecy, int r, int g, int c)
{
    double a, b;
    double x, y;
    int pom;
    int i;
    if (abs(startx - koniecx) > abs(starty - koniecy)) {
        if (startx > koniecx) {
            swap(startx, koniecx);
            swap(starty, koniecy);
        }
        a = (koniecy - starty) / static_cast<double>(koniecx - startx);
        b = starty - a * startx;
        for (i = startx; i <= koniecx; i++) {
            pom = static_cast<int>(a * i + b);
            rysujPiksel(ptr, i, pom, r, g, c);
            x = static_cast<double>(radius * (i - szer / 2)) / sqrt(static_cast<double>((i - szer / 2) * (i - szer / 2) + radius * radius + (pom - wys / 2) * (pom - wys / 2)));
            y = static_cast<double>(radius * (pom - wys / 2)) / sqrt(static_cast<double>((i - szer / 2) * (i - szer / 2) + radius * radius + (pom - wys / 2) * (pom - wys / 2)));
            rysujPiksel(img2->bits(), static_cast<int>(x + szer2 / 2), static_cast<int>(y + wys2 / 2), r, g, c);
        }
    }
    else {
        if (starty > koniecy) {
            swap(startx, koniecx);
            swap(starty, koniecy);
        }
        a = (koniecx - startx) / static_cast<double>(koniecy - starty);
        b = startx - a * starty;
        for (i = starty; i <= koniecy; i++) {
            pom = static_cast<int>(a * i + b);
            rysujPiksel(ptr, pom, i, r, g, c);
            y = static_cast<double>(radius * (i - wys / 2)) / sqrt(static_cast<double>((i - szer / 2) * (i - szer / 2) + radius * radius + (pom - wys / 2) * (pom - wys / 2)));
            x = static_cast<double>(radius * (pom - szer / 2)) / sqrt(static_cast<double>((i - szer / 2) * (i - szer / 2) + radius * radius + (pom - wys / 2) * (pom - wys / 2)));
            rysujPiksel(img2->bits(), static_cast<int>(x + szer2 / 2), static_cast<int>(y + wys2 / 2), r, g, c);
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
    rysujPunkty(img->bits(), static_cast<int>(szer/2), static_cast<int>(wys/2), 0, 255, 0, 4);
    rysujPunkty(img2->bits(), static_cast<int>(szer2/2), static_cast<int>(wys2/2), 0, 255, 0, 4);

    if (punkty.empty())
        return;
    pair<double, double> pkt_1;
    pkt_1 = *(punkty.begin());
    for (vector<pair<double, double> >::iterator it = punkty.begin(); it != punkty.end(); it++) {
        rysujPunkty(img->bits(), static_cast<int>(it->first), static_cast<int>(it->second), 255, 0, 0, 5);
        prosta(img->bits(), static_cast<int>(pkt_1.first), static_cast<int>(pkt_1.second), static_cast<int>(it->first), static_cast<int>(it->second), 0, 0, 255);
        pkt_1 = *(it);
    }
}


void MainWindow::on_horizontalSlider_valueChanged(int value)
{
    radius = value;
    *img = copy->copy();
    *img2 = copy2->copy();
    punkt();
    update();
}
