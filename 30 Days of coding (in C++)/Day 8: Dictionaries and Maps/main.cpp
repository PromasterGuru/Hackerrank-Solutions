#include <bits/stdc++.h> 
using namespace std;
int main() {
    map<string,string> phonebook;
    int n;
    int i = 0;
    cin>>n;
    cin.ignore(1,'\n');
    while(i < n){
        string contact;
        vector<string> tokens;
        getline(cin,contact);
        stringstream token(contact);
        string temp;
        while(getline(token, temp, ' ')){
            tokens.push_back(temp);
        }

        phonebook.insert(pair<string, string>(tokens[0],tokens[1]));
        map<string,string>::iterator itr;
        i++;
    }

    string name;
    vector<string> names;
    while(cin>>name){
        if(name.empty()){
            break;
        }
        names.push_back(name);
    }

    for(string name: names){
        if(phonebook[name].empty()){
            cout<<"Not found"<<endl;
        }
        else{
            cout<<name<<"="<<phonebook[name]<<endl;
        }
    }
    return 0;
}
