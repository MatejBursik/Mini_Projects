#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    fstream file;
    file.open("input.txt", ios::in);
    
    if (file.is_open()){
        string line;
        while (getline(file,line)){
            cout << line << endl;
        }
    }else if (!file.is_open()){
        cout << "Unable to open file";
    }
    file.close();

    return 0;
}

// for some reason it does not want to open the text file, HELP