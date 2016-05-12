#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;

void swap(int *a, int *b)
{
int tmp=*a;
*a=*b;
*b=tmp;
}

void bubble(int *arr, int N)
{
for (int i=N-1; i>=0; --i)
	for (int j=0; j!=i; ++j)
		if (arr[j] > arr[j+1]) 
			swap(arr+j, arr+j+1);		
}

void bubble2(int *arr, int N)
{
bool swapped = true;
int swapped_pos = 0;
for (int i=N-1; i>=0 && swapped; --i){
	swapped = false;
	for (int j=0; j!=i; ++j){
		if (arr[j] > arr[j+1]){
			swap(arr+j, arr+j+1);
			swapped = true;
			swapped_pos = j;
		}
	}
	i = swapped_pos+1;
}
}

void bubble3(int *arr, int N)
{
for (int i=0; i!=N; ++i)
	for (int j=N-1; j>i; --j)
		if (arr[j] < arr[j-1])
			swap(arr+j, arr+j-1);
}

void bubble4(int *arr, int N)
{
bool swapped = true;
int swapped_pos = N-1;
for (int i=0; i!=N && swapped; ++i){
	swapped = false;
	for (int j=N-1; j>i; --j){
		if (arr[j] < arr[j-1]){
			swap(arr+j, arr+j-1);
			swapped = true;
			swapped_pos = j;
		}
	}
	i = swapped_pos-1;
}
}

int main()
{
int arr[] = {3, 2, 4, 1, 6, 4, 9, 6, 3};

bubble4(arr, sizeof(arr)/sizeof(int));
copy(arr, arr+sizeof(arr)/sizeof(int), ostream_iterator<int>(cout, " "));
cout << endl;
}
