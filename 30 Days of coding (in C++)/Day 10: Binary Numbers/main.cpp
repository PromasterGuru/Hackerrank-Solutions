#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int count = 0;
    
    //SOLUTION ONE
    while(n != 0){
        n = n & (n<<1);
        count ++;
    }
    cout<<count<<endl;

    // SOLUTION TWO
    int n;
    string binary = "";
    int count = 0;
    int i = 0;
    int len = 0;

    cin >> n;
    
    while(n > 0){
        binary = to_string(n%2) + binary;
        n = floor(n/2);
        len ++;
    }
    while(i < len){
        int j = 0;
        while(binary[i] == '1'){
            j++;
            i++;
        }
        if(j > count){
            count = j;
        }
        i++;
    }
    cout<<count<<endl;
    return 0;
}