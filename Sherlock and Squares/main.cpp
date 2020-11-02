#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the squares function below.
int squares(int a, int b)
{
    int n = ceil(sqrt(a));
    int counter = 0;
    while ((n * n) >= a && n * n <= b)
    {
        counter++;
        n++;
    }
    return counter;
}

int main()
{
    int a;
    int b;
    cout << "Enter the value of a:";
    cin >> a;
    cout << "Enter the value of b:";
    cin >> b;
    cout << squares(a, b) << endl;
    return 0;
}