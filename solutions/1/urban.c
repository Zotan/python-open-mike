#include <stdio.h>

void rev(int *a, int *b, int n) {
    b=a+n-1;
    while(a<b) {*a^=*b;*b^=*a;*a++^=*b--;}
}


int main(int argc, char *argv[])
{
  int array[]={1,2,3,4,5,6,7,8,9,10,0};
    int *a=NULL, *b=NULL;

  a=array;
    while(*a) printf("%d,",*a++);
      printf("\n");

  a=array;
    b=a+9;

  while(a<b) {*a^=*b;*b^=*a;*a++^=*b--;}

  a=array;
    while(*a) printf("%d,",*a++);
      printf("\n");

}

