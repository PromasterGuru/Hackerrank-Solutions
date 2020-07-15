#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int j = 0;
        int l;
        string str;
        string odd;
        string even;
        cin >> str;
        l = str.size();
        while (j < l)
        {
            if (j % 2 == 0)
            {
                even += str[j];
            }
            else
            {
                odd += str[j];
            }
            j++;
        }
        cout << even << " " << odd << endl;
    }
    return 0;
}
