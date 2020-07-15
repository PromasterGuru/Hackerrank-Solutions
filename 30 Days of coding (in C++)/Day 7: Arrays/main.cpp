#include <iostream>
using namespace std;
int main()
{
    int arr[4] = {1, 4, 3, 2};
    for(int i = (*(&arr + 1) - arr); i > 0; i--){
        cout<<arr[i-1]<<" ";
    }
    return 0;
}
