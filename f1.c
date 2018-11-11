#include <stdio.h>
#include <string.h>

int
f(char * arg, int n)
{
    int ret = 0;
    int b = 10;
    int c = 0;
    while(c < n)
    {
        int d = *(arg + c);
        c++; //lol
        d -= 0x30;             //'0'
        if(d <= 0x39)          //'9' ; 57
        {
            ret = ret * b;
            ret += d;
        }
    }
    return ret;
}

int
main(int argc, char *argv[])
{
    if(argc < 2)
    {
        return -1;
    }

    printf("%d\n", f(argv[1], strlen(argv[1])));

    return 0;
}

// This order worked.
//set args 30 2 30 2 0 16 13 11 1 5 5 12 9 7 3 14
