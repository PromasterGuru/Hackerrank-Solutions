#include <bits/stdc++.h>
using namespace std;
class Difference
{
protected:
    vector<int> elements;

public:
    int maximumDifference;
    Difference(vector<int> elems)
    {
        this->elements = elems;
    };

    void computeDifference()
    {
        int max = 1;
        int min = 100;
        for (int i = 0; i < elements.size(); i++)
        {
            if (elements.at(i) > max)
            {
                max = elements.at(i);
            }
            if (elements.at(i) < min)
            {
                min = elements.at(i);
            }
        }
        maximumDifference = max - min;
    };
};
int main()
{
    int N;
    cin >> N;

    vector<int> a;

    for (int i = 0; i < N; i++)
    {
        int e;
        cin >> e;

        a.push_back(e);
    }

    Difference d(a);

    d.computeDifference();

    cout << d.maximumDifference;

    return 0;
}