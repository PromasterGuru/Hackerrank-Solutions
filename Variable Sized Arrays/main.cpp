#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, q, size, y, z, elem;
    vector<vector<int>> elems;
    cin >> n >> q;
    for (int i = 0; i < n; i++)
    {
        vector<int> ar;
        cin >> size;
        for (int j = 0; j < size; j++)
        {
            cin >> elem;
            ar.push_back(elem);
        }
        elems.push_back(ar);
    }

    for (int x = 0; x < q; x++)
    {
        cin >> y >> z;
        cout << elems[y][z] << endl;
    }
    return 0;
}

/**
2 2
3 1 5 4
5 1 2 8 9 3
0 1
1 3
**/
