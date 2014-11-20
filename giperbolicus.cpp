#include <stdio.h>
#include <math.h>
//#include <iostream>

const int n=100;
//const double tmax = 0.1; // ����� ����������
const double r=0.95; 
const double pi=3.14159265;


double u[n];
double der[n];
double v[n];
double q[n];//vspomogateln massiv dlia zamenyy
double w[n];


double source(double x, double t ) { //������� ���������
       return 0;
}

/* �� left*/
double a0(double t){
       return 0;
}

double b0(double t){ // ����������� �����
       return 1.0;
}

double c0(double t){
       return 0;
}
/* �� right*/
double a1(double t){
       return 0.0;
}

double b1(double t){// ����������� �����
       return 1.0;
}

double c1(double t){
       return 0;
}

void giperbolic(double *x, double ts, double te){
     /* ��������� ��� ��������������� ���������*/
      for ( int i = 0; i < n; i++ ) {
          x[i]=1.0/n * i ; // ���������� ����� �� ��� x
      }
      double xi=1.0/n;
     double tau=xi*sqrt(r); // ��� �� ������� (�� ������� �������)
     double t=ts; // t-������� �����, ts -- ����� ������ ������������
     
     /*�������� �������� � �������� �� ��������� �����*/
     while(t < te){ //te -- ����� ����� ������������
     for ( int i = 1; i < n-1; i++ ) {
     w[i] = 2 * (1 - r) * v[i] +
            r * (v[i-1] + v[i+1]) -
            u[i] + tau * tau * source(i * xi, t);
         }

     /* �������� �������� �� �����*/


      v[0] = (c0(t) - v[1] * a0(t) / xi) / (b0(t) - a0(t) / xi);
      v[n-1] = (c1(t) + v[n-2] * a1(t) / xi) / (b1(t) + a1(t) / xi);

    for ( int i = 0; i < n; i++ ) {
        q[i]=u[i]; 
        u[i]=v[i];
        v[i]=w[i];
        w[i]=q[i];
    }
        t += tau; //���������� �������
    for ( int i = 0; i < n; i++ ) {
       double   d = (v[i] - u[i]) / tau; //������ ����������� �� �������
      }
}
}
int main( void ) { // ������� ����������� ���������
	FILE *f;
    f = fopen("fileg.txt", "w");
    double ts=0,te=1, x[n],t,tau;

    for(int i = 0; i < n; i++){// nachalnoe uslovie
        u[i] = sin(pi * i / n);
        der[i]=0;
    }
    
    /* ��������� ��� �� ���������� ������� �� �����������*/
    for ( int i = 0; i < n; i++ ) {
          v[i]=u[i]+tau*der[i]; 
      }
      
    for( double t = 0; t<1.0; t+=0.1 ) {
    giperbolic(x,t,t+0.1);
     for ( int i = 0; i < n; i++ ) {
        fprintf(f, "%f %f %f\n", t,x[i],u[i]);
       }
       fprintf(f, "\n");
       }
       fclose(f);
    getchar(); // ������� �������� ������
    return 0;
}
