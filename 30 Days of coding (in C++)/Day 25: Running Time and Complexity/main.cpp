#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    int m;
    vector<int> arr;
    int counter = 0;
    cin >> n;
    while (counter < n)
    {
        cin >> m;
        arr.push_back(m);
        counter++;
    }
    for (int i = 0; i < arr.size(); i++)
    {
        int j = 2;
        bool isPrime = true;
        if (arr[i] == 1)
        {
            isPrime = false;
        }
        else
        {
            while (j <= sqrt(arr[i]))
            {
                if (arr[i] % j == 0)
                {
                    isPrime = false;
                    break;
                }
                j++;
            }
        }
        if (isPrime)
        {
            cout << "Prime" << endl;
        }
        else
        {
            cout << "Not prime" << endl;
        }
        isPrime = false;
    }
    return 0;
}
