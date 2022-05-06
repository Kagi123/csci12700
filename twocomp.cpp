//Name:  Sangheum Park
//Email:  sangheum.park27@myhunter.cuny.edu
//Date:  May 06 2022
//asks the user for a whole number between -31 and 31 and prints out the number in "two's complement" notation,

#include <iostream> 
#include <iomanip> 

using namespace std;

int main(){
  int n;
  int x = 0;
  int b = 16;
  
  cout << "Enter a number: ";
  cin >> n;
  if(n<0) {
    cout << "1";
    x = 32 + n;
    }
  else {
    cout <<"0";
    x = n;
  }
  while(b > 0.5){
    if(x >= b){
      cout <<"1";
    } else {
      cout << "0";
    }
    x = x % b;
    b = b/2;
  }
  cout << "\n";
  return 0;
}


