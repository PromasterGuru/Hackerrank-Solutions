#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

class Person
{
public:
    string name;
    int age;
    virtual void getdata(){};
    virtual void putdata(){};
};
class Professor : public Person
{
private:
    int publications;
    static int cur_id;

public:
    int getCurId() { cur_id ++; return cur_id; }
    void getdata() { cin >> name >> age >> publications; }
    void putdata() { cout << name << ' ' << age << ' ' << publications << ' ' << getCurId() << endl; }
};

class Student : public Person
{
private:
    int marks[6];
    static int cur_id;

public:
    int getTotalMarks()
    {
        int sum = 0;
        for (int i = 0; i < sizeof(marks) / sizeof(marks[0]); i++)
        {
            sum += marks[i];
        }
        return sum;
    }
    int getCurId() { cur_id ++; return cur_id; }
    void getdata() { cin >> name >> age >> marks[0] >> marks[1] >> marks[2] >> marks[3] >> marks[4] >> marks[5]; }
    void putdata() { cout << name << ' ' << age << ' ' << getTotalMarks() << ' ' << getCurId() << endl; }
};

int Professor::cur_id = 0;
int Student::cur_id = 0;

int main()
{
    int n, val;
    cin >> n; //The number of objects that is going to be created.
    Person *per[n];

    for (int i = 0; i < n; i++)
    {

        cin >> val;
        if (val == 1)
        {
            // If val is 1 current object is of type Professor
            per[i] = new Professor;
        }
        else
            per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.
    }

    for (int i = 0; i < n; i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;
}
