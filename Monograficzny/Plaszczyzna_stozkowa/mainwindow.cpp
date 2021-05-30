#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <cmath>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    szer = ui->rysujFrame->width();
    wys = ui->rysujFrame->height();
    poczX = ui->rysujFrame->x();
    poczY = ui->rysujFrame->y();
    szer2 = ui->rysujFrame_2->width();
    wys2 = ui->rysujFrame_2->height();
    poczX2 = ui->rysujFrame_2->x();
    poczY2 = ui->rysujFrame_2->y();
    img = new QImage(szer,wys,QImage::Format_RGB32);
    copy = new QImage(szer,wys,QImage::Format_RGB32);
    img2 = new QImage(szer,wys,QImage::Format_RGB32);
    copy2 = new QImage(szer,wys,QImage::Format_RGB32);
    czysc();
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
    p.drawImage(poczX,poczY,*img);
    p.drawImage(poczX2,poczY2,*img2);
}
void MainWindow::on_cleanButton_clicked()
{
    czysc();
    radius = 200;
    steps = 0.0;
    ui->horizontalSlider->setValue(radius);
    ui->dial->setValue(0);
    update();
}
void MainWindow::czysc()
{
    licznik = 0;
    kontrola = false;
    punkty.clear();
    int i,j;
    for(i=0; i<wys; i++)
    {
        for(j=0; j<szer; j++)
        {
            rysujPiksel(img->bits(), i, j, 255, 255, 255);
            rysujPiksel(img2->bits(), i, j, 255, 255, 255);
        }
    }
    rysujPunkty(img->bits(), 200, 200, 0, 255, 0, 5);
    rysujPunkty(img2->bits(), 200, 200, 0, 255, 0, 5);
    *copy = img->copy();
    *copy2 = img2->copy();
}
void MainWindow::mousePressEvent(QMouseEvent *event)
{
    int x = event->x();
    int y = event->y();
    *img = copy->copy();
    *img2 = copy2->copy();
    x -= poczX;
    y -= poczY;
    if(event->button() == Qt::LeftButton)
    {
        if((x>=0)&&(y>=0)&&(x<szer)&&(y<wys))
        {

        }
    }
    else
    {
        if((x>=0)&&(y>=0)&&(x<szer)&&(y<wys))
        {
            sprawdz(x,y);
        }

    }
    krzywe();
    punkt();
    update();
}
void MainWindow::mouseReleaseEvent(QMouseEvent *event)
{
    int x = event->x();
    int y = event->y();
    *img = copy->copy();
    *img2 = copy2->copy();
    x -= poczX;
    y -= poczY;
    if(event->button() == Qt::LeftButton)
    {
        if((x>=0)&&(y>=0)&&(x<szer)&&(y<wys)){
            if(usun){
                sprawdz(x,y);
                if(kontrola){
                    punkty.erase(przesun);
                    licznik--;
                    kontrola = false;
                }
            } else if(!usun && licznik < 3){
                punkty.push_back(make_pair(x,y));
                licznik++;
            }
        }
    }
    else
    {
        if(kontrola == true && (x>=0)&&(y>=0)&&(x<szer)&&(y<wys)){
            pair<double, double> przesuniety;
            przesuniety = make_pair(x,y);
            *przesun = przesuniety;
            kontrola = false;
        }
    }
    krzywe();
    punkt();
    update();
}
void MainWindow::mouseMoveEvent(QMouseEvent *event)
{
    int x = event->x();
    int y = event->y();
    *img = copy->copy();
    *img2 = copy2->copy();
    x -= poczX;
    y -= poczY;
    if(event->button() == Qt::LeftButton)
    {

    }
    else
    {
        if(kontrola == true && (x>=0)&&(y>=0)&&(x<szer)&&(y<wys)){
            pair<double, double> przesuniety;
            przesuniety = make_pair(x,y);
            *przesun = przesuniety;
        }
    }
    krzywe();
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

void MainWindow::sprawdz(int x, int y){
    for(vector<pair<double, double> >::iterator it = punkty.begin(); it != punkty.end(); it++){
        if(it->first + 5 >= x && it->first - 5 <= x && it->second + 5 >= y && it->second - 5 <= y){
            przesun = it;
            kontrola = true;
            return;
        }
    }
}
void MainWindow::punkt(){
    if(punkty.empty())
        return;
    for(vector<pair<double, double> >::iterator it = punkty.begin(); it != punkty.end(); it++){
        rysujPunkty(img->bits(), static_cast<int>(it->first),static_cast<int>(it->second), 255, 0, 0, 5);
    }
}
void MainWindow::krzywe(){
    vector<pair<double, double> > help, output;
    pair<double,double> pkt_1, a, b, c;
    double t = 0;
    double x, y, z, z_old, odl, x2, y2;
    double alfa = steps / 180.0 * M_PI;
    vector<pair<double, double> >::iterator it;
    if(punkty.empty() || licznik < 3)
        return;
    a = *punkty.begin();
    b = *(punkty.begin() + 1);
    c = *(punkty.begin() + 2);
    while(t <= 1.0) {
        help = wylicz(licznik, punkty, 1 - t);
        it = help.begin();
        output.push_back(*(it));
        pkt_1 = *(it);
        rysujPiksel(img->bits(), static_cast<int>(pkt_1.first), static_cast<int>(pkt_1.second), 0, 0, 255);

        x2 = x = (1 - t) * (1- t) * (a.first - szer / 2.0) + 2 * (1 - t) * t * (b.first - szer / 2.0) + t * t * (c.first - szer / 2.0);
        y2 = y = (1 - t) * (1- t) * (a.second - wys / 2.0) + 2 * (1 - t) * t * (b.second - wys / 2.0) + t * t * (c.second - wys / 2.0);
        z_old = radius;

        odl = sqrt(x2 * x2 + y2 * y2 + 200 * 200);
        x2 = x2 * 200 / odl;
        y2 = y2 * 200 / odl;
        if(z_old == 0.0){
            rysujPiksel(img->bits(), static_cast<int>(x2 + szer2/2.0), static_cast<int>(y2 + szer2 / 2.0), 255, 0, 0);
            rysujPiksel(img->bits(), static_cast<int>(-x2 + szer2/2.0), static_cast<int>(-y2 + szer2 / 2.0), 255, 0, 0);
        } else {
            rysujPiksel(img->bits(), static_cast<int>((z_old > 0 ? 1 : -1) * x2 + szer2/2.0), static_cast<int>((z_old > 0 ? 1 : -1) * y2 + szer2 / 2.0), 255, 0, 0);
        }

        x = cos(alfa) * x - sin(alfa) * z_old;
        z = sin(alfa) * x + cos(alfa) * z_old;
        odl = sqrt(x * x + y * y + z * z);
        x = x * radius / odl;
        y = y * radius / odl;
        if(z == 0.0){
            rysujPiksel(img2->bits(), static_cast<int>(x + szer2/2.0), static_cast<int>(y + szer2 / 2.0), 0, 0, 255);
            rysujPiksel(img2->bits(), static_cast<int>(-x + szer2/2.0), static_cast<int>(-y + szer2 / 2.0), 0, 0, 255);
        } else {
            rysujPiksel(img2->bits(), static_cast<int>((z > 0 ? 1 : -1) * x + szer2/2.0), static_cast<int>((z > 0 ? 1 : -1) * y + szer2 / 2.0), 0, 0, 255);
        }

        x2 = x = (1 - t) * (1- t) * (a.first - szer / 2.0) - 2 * (1 - t) * t * (b.first - szer / 2.0) + t * t * (c.first - szer / 2.0);
        y2 = y = (1 - t) * (1- t) * (a.second - wys / 2.0) - 2 * (1 - t) * t * (b.second - wys / 2.0) + t * t * (c.second - wys / 2.0);
        z_old = (1 - 2 * t) * (1 - 2 * t) * radius;

        z = (1 - 2 * t) * (1 - 2 * t) * 200;
        odl = sqrt(x2 * x2 + y2 * y2 + z * z);
        x2 = x2 * 200 / odl;
        y2 = y2 * 200 / odl;
        if(z == 0.0){
            rysujPiksel(img->bits(), static_cast<int>(x2 + szer2/2.0), static_cast<int>(y2 + szer2 / 2.0), 255, 255, 0);
            rysujPiksel(img->bits(), static_cast<int>(-x2 + szer2/2.0), static_cast<int>(-y2 + szer2 / 2.0), 255, 255, 0);
        } else {
            rysujPiksel(img->bits(), static_cast<int>((z > 0 ? 1 : -1) * x2 + szer2/2.0), static_cast<int>((z > 0 ? 1 : -1) * y2 + szer2 / 2.0), 255, 255, 0);
        }

        x = cos(alfa) * x - sin(alfa) * z_old;
        z = sin(alfa) * x + cos(alfa) * z_old;
        odl = sqrt(x * x + y * y + z * z);
        x = x * radius / odl;
        y = y * radius / odl;
        if(z == 0.0){
            rysujPiksel(img2->bits(), static_cast<int>(x + szer2/2.0), static_cast<int>(y + szer2 / 2.0), 0, 255, 0);
            rysujPiksel(img2->bits(), static_cast<int>(-x + szer2/2.0), static_cast<int>(-y + szer2 / 2.0), 0, 255, 0);
        } else {
            rysujPiksel(img2->bits(), static_cast<int>((z > 0 ? 1 : -1) * x + szer2/2.0), static_cast<int>((z > 0 ? 1 : -1) * y + szer2 / 2.0), 0, 255, 0);
        }

        t += 0.00005;
    }
}

vector<pair<double, double> > MainWindow::wylicz(int count, vector<pair<double, double> > points, double step)
{
    int i = 0;
    double x, y;
    vector<pair<double, double> > help;
    pair<double, double> tmp_1, tmp_2;
    if(count == 1) {
        return points;
    }
    for(vector<pair<double, double> >::iterator it = points.begin(); i < count - 1; i++, it += 1) {
        tmp_1 = *(it);
        tmp_2 = *(it + 1);
        x = (tmp_1.first + (1-step) * (tmp_2.first - tmp_1.first));
        y = (tmp_1.second + (1-step) * (tmp_2.second - tmp_1.second));
        help.push_back(make_pair(x, y));
    }
    return wylicz(count - 1, help, step);
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
    if(arg1){
        usun = true;
    } else {
        usun = false;
    }
}

void MainWindow::on_horizontalSlider_valueChanged(int value)
{
    radius = value;
    *img = copy->copy();
    *img2 = copy2->copy();
    krzywe();
    punkt();
    update();
}

void MainWindow::on_dial_valueChanged(int value)
{
    steps = value;
    *img = copy->copy();
    *img2 = copy2->copy();
    krzywe();
    punkt();
    update();
}
