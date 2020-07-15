#include <bits/stdc++.h>
using namespace std;

#define ROW 6
#define COL 6
int main()
{
    vector<vector<int>> arr(6);
    int sum = INT_MIN;
    arr[0] = {1, 1, 1, 0, 0, 0};
    arr[1] = {0, 1, 0, 0, 0, 0};
    arr[2] = {1, 1, 1, 0, 0, 0};
    arr[3] = {0, 0, 2, 4, 4, 0};
    arr[4] = {0, 0, 0, 2, 0, 0};
    arr[5] = {0, 0, 1, 2, 4, 0};

    for (int r = 0; r < arr.size() - 2; r++)
    {
        for (int c = 0; c < arr[r].size() - 2; c++)
        {
            int s = (arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]);
            if (s > sum)
            {
                sum = s;
            }
        }
    }
    cout << sum << endl;
}
