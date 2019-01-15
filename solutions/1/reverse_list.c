#include <stdio.h>

void reverse1(int* lst, int* r, int L) {
    int i;
    for(i=0; i < L; i++) {
        r[i] = lst[L-1-i];
    }
}

void reverse2(int* lst, int L) {
    int tmp;
    int i;
    for(i=0; i < L/2; i++) {
        tmp = lst[i];
        lst[i] = lst[L-1-i];
        lst[L-1-i] = tmp;
    }
}


int main(void){
    int myArray[4] = {1,2,3,4};
    int len = 4;
    int retArray[4];
    int i;
    
    printf("\n testing reverse1: \n");
    reverse1(myArray, retArray, len);
    for(i=0; i < len; i++) {
        printf("%d ", retArray[i]);
    }

    printf("\n inp array: \n");
    for(i=0; i < len; i++) {
        printf("%d ", myArray[i]);
    }

    printf("\n testing reverse2: \n");
    reverse2(myArray, len);
    for(i=0; i < len; i++) {
        printf("%d ", myArray[i]);
    }
    printf("done\n\n ");
    return 0;
}
