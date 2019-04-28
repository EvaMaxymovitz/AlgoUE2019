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

int main(int argc, char** argv)
{
     if (argc == 2 && strcmp(argv[1], "--help")==0) {
        cout<<"enter a number n behind the file to see the n-th Fibonaci number. Append __-all__ to see all terms." <<endl;
    }

    else if (argc == 3 && strcmp(argv[2], "--all")==0) {     
        int input = atoi(argv[1]);  
        int a = 0, b = 1, next = 0;
        
        for (int i = 1; i <= input; ++i)
        {
            if(i == 1)
        {
            cout << " " << a;
            continue;
        }
            
            if(i == 2)
            {
                cout << b << " ";
                continue;
            }
            next = a + b;
            a = b;
            b = next;
            
            cout << next << " ";
        }
    }
     else 
     {
        int input = atoi(argv[1]);
        int number[input] = {0, 1};
        for (int i = 2; i <= input; i++) 
        {
            number[i] = number[i - 1] + number[i - 2];
        }
        cout << number[input] << " " << endl;
     }

return 0;
}