#include <iostream>
#include <algorithm>
using namespace std;

void printArr(int arr[], int n, int step){
    cout << "Iterasi " << step << ": ";
    for(int i=0;i<n;i++) cout<<arr[i]<<" ";
    cout<<endl;
}

// Bubble
void bubble(int arr[], int n){
    int step=1;
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]) swap(arr[j],arr[j+1]);
            printArr(arr,n,step++);
        }
    }
    cout<<"Hasil Bubble: ";
    for(int i=0;i<n;i++) cout<<arr[i]<<" ";
    cout<<endl;
}

// Selection
void selection(int arr[], int n){
    int step=1;
    for(int i=0;i<n;i++){
        int min=i;
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[min]) min=j;
        }
        swap(arr[i],arr[min]);
        printArr(arr,n,step++);
    }
    cout<<"Hasil Selection: ";
    for(int i=0;i<n;i++) cout<<arr[i]<<" ";
    cout<<endl;
}

// Insertion
void insertion(int arr[], int n){
    int step=1;
    for(int i=1;i<n;i++){
        int key=arr[i];
        int j=i-1;
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;
        printArr(arr,n,step++);
    }
    cout<<"Hasil Insertion: ";
    for(int i=0;i<n;i++) cout<<arr[i]<<" ";
    cout<<endl;
}

// MAIN
int main(){
    int n;
    cout<<"Jumlah data: ";
    cin>>n;

    int *arr = new int[n];
    cout<<"Masukkan data: ";
    for(int i=0;i<n;i++) cin>>arr[i];

    int b[n], s[n], i_arr[n];
    copy(arr, arr+n, b);
    copy(arr, arr+n, s);
    copy(arr, arr+n, i_arr);

    cout<<"\n=== Bubble ===\n";
    bubble(b,n);

    cout<<"\n=== Selection ===\n";
    selection(s,n);

    cout<<"\n=== Insertion ===\n";
    insertion(i_arr,n);

    delete[] arr;
    return 0;
}
