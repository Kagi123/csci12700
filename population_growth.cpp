//Name:  Sangheum Park
//Email:  sangheum.park27@myhunter.cuny.edu
//Date:  May 04 2022
//prints the change in population of the the United States

#include <iostream> 
#include <iomanip> 

using namespace std;

int main(){
  float p,B, D;
  p = 325.7;
  B = 0.0124;
  D = 0.0084;

  int n;
  cout << "Please enter the number of years: ";
  cin >> n;
  int year = 2017;
  for(int i=0; i<n; i++){
    cout << "Year " << setw(1) << year + i << "  "
      << fixed << setprecision(2) << p << endl;
    p = p + B*p - D * p;
  }
  
  
  return 0;
}


