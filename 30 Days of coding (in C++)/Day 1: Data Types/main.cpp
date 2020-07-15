#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main()
{
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    int a;
    double b;
    string str;

    //string and save an integer, double, and String to your variables.
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    cin >> a;
    cin >> b;
    cin.ignore();
    getline(cin, str);

    // Print the sum of both integer variables on a new line.
    cout << i + a << endl;

    // Print the sum of the double variables on a new line.
    cout << fixed << setprecision(1) << d + b << endl;

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s << str << endl;

    return 0;