#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPainter>
#include <QImage>
#include <QMouseEvent>
#include <vector>

using namespace std;
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow() override;

private:
    Ui::MainWindow *ui;
    QImage *img;
    QImage *copy;
    QImage *img2;
    QImage *copy2;
    int szer;
    int wys;
    int poczX;
    int poczY;
    int szer2;
    int wys2;
    int poczX2;
    int poczY2;
    int licznik = 0;
    vector<pair<double, double> > punkty;
    vector<pair<double, double> >::iterator przesun;
    vector<pair<double, double> > tmp;
    bool kontrola = false;
    bool usun = false;
    double steps = 0;
    int radius = 200;
    // Deklaracje funkcji
    void czysc();
    void sprawdz(int x, int y);
    void rysujPiksel(unsigned char *ptr, int x, int y, int r, int g, int b);
    void rysujPunkty(unsigned char *ptr, int x, int y, int r, int g, int b, int size);
    void punkt();
    void krzywe();
    vector<pair<double, double> > wylicz(int count, vector<pair<double, double> > points, double step);
private slots:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void paintEvent(QPaintEvent*) override;

    void on_cleanButton_clicked();
    void on_exitButton_clicked();

    void on_pushButton_clicked();
    void on_checkBox_stateChanged(int arg1);
    void on_horizontalSlider_valueChanged(int value);
    void on_dial_valueChanged(int value);
};
#endif // MAINWINDOW_H
