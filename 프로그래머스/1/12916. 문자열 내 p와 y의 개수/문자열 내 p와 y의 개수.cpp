#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int count =0;
    
    // p --> add 1;
    // y --> add -1;
    for(int i =0; i < s.size(); i ++){
        s[i]= tolower(s[i]);
        if(s[i]=='p')
            count ++;
        else if (s[i]=='y')
            count --;
    }
   
   if (count !=0)
       answer =0;

    return answer;
}