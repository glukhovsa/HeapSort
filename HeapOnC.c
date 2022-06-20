#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void SWAP(int *array, int x, int y){
    int z=array[x];
    array[x]=array[y];
    array[y]=z;
}


void heapify(int *arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i){
        SWAP(arr, i, largest);
        heapify(arr, n, largest);
    }
}

void heapSort(int *arr, int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i >= 0; i--) {
        SWAP(arr, 0, i);
        heapify(arr, i, 0);
    }
}

int main(){
    return 0;
}
