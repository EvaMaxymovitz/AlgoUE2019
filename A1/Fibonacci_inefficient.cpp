// # Aufgabe A1
// # Fibonacci numbers

// The task is to compute the the first *n* Fibonacci numbers. Implement an ineffieient 
// as well as an efficient version as two standalone programs that should accept an integer via 
// command line option __-n__ and print the nth Fibonaci number to STDOUT. 
// Implement an optional command line switch __--all__ that prints all Fibonacci numbers 
// up to n as a comma-separated list to STDOUT.

// * fibo_inefficient -n <int> [--all]
// * fibo_efficient -n <int> [--all]

// Measure the runtime of both tools for different parameters of n, e.g. via the `time` command. 
// Plot the runtime of both approaches as a function of n in a single PDF graph. 
// The filename should be `fibo_runtime.pdf`.

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

int fibonacci(int n);

int main(int argc, char** argv)

{
 if (argc == 2 && strcmp(argv[1], "--help")==0) {
    cout<<"enter a number n behind the file to see the n-th Fibonaci number. Append __-all__ to see all terms." <<endl;
}

else if (argc == 3 && strcmp(argv[2], "--all")==0) {
   int input = atoi(argv[1]);
   int a, i;

a = 0;

for(i = 1; i <= input; i++)
{
  cout << " " <<fibonacci(a);
  a++;
}
return 0;
}

else
 {
    int input = atoi(argv[1]);
    int fibonacci [input] = {0,1};
    for (int i = 2; i <= input; i++) {
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    }
   cout << fibonacci[input] << " " << endl;

return 0;
}
 }