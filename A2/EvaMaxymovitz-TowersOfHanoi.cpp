// The task is to solve the n-disc Towers of Hanoi puzzle.

// Implement a program that accepts an integer via command line option -n and prints 
// instructions to STDOUT as follows:

// Move disk from X to Y

// Likewise, the tool should print the total number of disc move operations to STDERR 
// upon finishing the computation. Allow the user to obtain some information on your tool 
// via a --help option. The program should be named as

// * $githubusername-TowersOfHanoi.$suffix -n [--help]

// Measure the runtime of your tool, ensuring that STDOUT is redirected to a file rather 
// than displayed via the console (which would unnecessarily blow up runtime). 
// You might employ the concept of subshells to get this done.

// Plot the runtime of your program (in seconds) vs size of the Hanoi puzzle and create 
// a PDF graph. Your pull request should include the following files:

// - your program
// - A file containing STDOUT of your program up to at least n=25. 
//   The name of this file should be $githubusername-TowersOfHanoi.out
// - a PDF plot of runtime vs n named $githubusername-TowersOfHanoi_runtime.pdf


#include <iostream>
using namespace std;
 
void towers(int, char, char, char);
 
int main(int argc, char** argv)
{
    if (argc == 2 && strcmp(argv[1], "--help")==0) 
    {
        cout<<"enter the number of discs you want to move towards the three towers of hanoi. Please store the output file (overview of disc movements) to EvaMaxymovitz-TowersOfHanoi.out." <<endl;
    }

    else
     {
        int input = atoi(argv[1]);
        towers(input, 'A', 'C', 'B');
        
        return 0;
     }
}
    void towers(int num, char start_disc, char end_disc, char disc)
{ 
    if (num == 1)
    {
        cout<<"move disk 1 from "<<start_disc<<" to "<<end_disc << endl;
        return;
    }
    towers(num - 1, start_disc, disc, end_disc);
    cout<<"move disk "<<num<<" from "<<start_disc<<" to "<<end_disc << endl;
    towers(num - 1, disc, end_disc, start_disc);
}

 