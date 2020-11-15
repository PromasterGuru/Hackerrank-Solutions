#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <iterator>
using namespace std;

int dayDiff(string actual_day, string expected_day)
{
    return stoi(actual_day) - stoi(expected_day);
}
int monthDiff(string actual_month, string expected_month)
{
    return stoi(actual_month) - stoi(expected_month);
}

int yearDiff(string actual_year, string expected_year)
{
    return stoi(actual_year) - stoi(expected_year);
}

int main()
{
    int fine = 0;
    string actual_return_date, expected_return_date;
    getline(cin, actual_return_date);
    getline(cin, expected_return_date);

    istringstream is1(actual_return_date);
    istringstream is2(expected_return_date);
    vector<string> ad{istream_iterator<string>{is1}, istream_iterator<string>{}};
    vector<string> ed{istream_iterator<string>{is2}, istream_iterator<string>{}};

    if (dayDiff(ad[0], ed[0]) > 0 && monthDiff(ad[1], ed[1]) == 0 && yearDiff(ad[2], ed[2]) == 0)
    {
        fine = 15 * dayDiff(ad[0], ed[0]);
    }
    else if (monthDiff(ad[1], ed[1]) > 0 && yearDiff(ad[2], ed[2]) == 0)
    {
        fine = 500 * monthDiff(ad[1], ed[1]);
    }
    else if (yearDiff(ad[2], ed[2]) > 0)
    {
        fine = 10000;
    }
    else
    {
        fine = 0;
    }
    cout << fine << endl;
    return 0;
}
