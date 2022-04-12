//Name:  Sangheum Park
//Email:  sangheum.park27@myhunter.cuny.edu
//Date:  April 11 2022
//asks the user for the year born, and continue asking until the number entered that is 2018 or earlier.


#include <iostream>

using namespace std;

int main(){
  int num;
  cout << "Please enter year born: " << endl;
  cin >> num;

  while(num>2018){
    cout << "Please enter year born: " << endl;
    cin >> num;
  }
  cout << "You entered:  " << num<< endl;
  
}


