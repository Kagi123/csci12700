//Name:  Sangheum Park
//Email:  sangheum.park27@myhunter.cuny.edu
//Date:  April 11 2022
//Season Greetings


#include <iostream>

using namespace std;

int main(){
  int number;
  cout << "Enter a number: " << endl;
  cin >> number;
  for(int i=0; i<number; i++){
    for(int j=0; j<i+1; j++){
      cout<<"*";
    }
    cout<<endl;
  }
  
}


