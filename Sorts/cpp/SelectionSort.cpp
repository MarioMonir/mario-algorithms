//Selection Sort

#include <iostream>
using namespace std;
typedef int type;

void selectionSort(int arr[] , int n);
void print_array(int arr[] , int n);

int main()
{
	  
	  int arr[5] = {5,4,3,2,1};
	   print_array(arr,5);
	  selectionSort(arr,5);
	  print_array(arr,5);
	  
	return 0;
}

/*-------------------------------*/
void selectionSort(int arr[] , int n){
	int i , j , min , temp ;
	
	for(i = 0 ; i < n-1 ; i++){
		min = i;
		for(j=i+1;j<n;j++){
			if(arr[j]<arr[min]) 
				min=j;
		}
		temp = arr[i];;
		arr[i] = arr[min];
		arr[min] = temp;
	}
}
	
/*-------------------------------*/
  void print_array(int arr[] , int n){
     cout<<"array = [ ";
      for(int i = 0 ; i < n ; i++){
        cout<<arr[i];
        if(i!=n-1){
           cout<<" , ";
        }
      }
      cout<<" ]"<<endl;
  }
/*-------------------------------*/

