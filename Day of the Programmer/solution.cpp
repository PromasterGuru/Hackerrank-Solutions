#include <bits/stdc++.h>

using namespace std;

//Check whether the given year is leap year
bool isLeapYear(int year)
{
    if (year < 1918)
    {
        return year % 4 == 0;
    }
    else
    {
        return (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0));
    }
    return false;
}

// Complete the dayOfProgrammer function below.
string dayOfProgrammer(int year)
{
    int month = 256 / 31;
    int days = 256 - ((31 * month) - 2);
    string result;
    std::stringstream ss_day,ss_month;

    if (isLeapYear(year))
    {
        days += 2;
    }
    else
    {
        days += 3;
    }

    if (year == 1918)
    {
        days += 13;
    }

    if (days > 0)
    {
        month += 1;
    }
    ss_day << setfill('0') << setw(2) << days;
    ss_month << setfill('0') << setw(2) << month;
    return (ss_day.str() + "." + ss_month.str() + "." + to_string(year));
}

int main()
{
    int year = 0;
    while (year != -1)
    {
        cout << "\nEnter year: ";
        cin >> year;
        cout << dayOfProgrammer(year);
    }
    return 0;
}