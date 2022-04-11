//Name:  Sangheum Park
//Email:  sangheum.park27@myhunter.cuny.edu
//Date:  April 11 2022
//Season Greetings


#include <iostream>

using namespace std;

int main(){
  int number;
  cout << "Enter month (as a number): " << endl;
  cin >> number;
  if(number<3 || number > 11){
    cout << "Happy Winter"<<endl;
  } else if(number>=3 && number < 7){
    cout << "Happy Spring"<<endl;
  } else if(number>=7 && number < 9){
    cout << "Happy Summer"<<endl;
  } else cout << "Happy fall"<<endl;
  
}


