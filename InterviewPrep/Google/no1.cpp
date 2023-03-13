#include <iostream> 
#include<bits/stdc++.h> 
using namespace std; 
int main() {     
    int t;     
    cin>>t;     
    while(t--){     
        string s;     
        cin>>s;     
        int n = s.size();     
        int currA = 0, currC = 0, maxA = 0, maxC = 0;     
        for(int i=0;i<n;i++){         
            if(s[i] == 'A'){             
                currA++;             
                currC--;         
            }         
            else if(s[i] == 'C'){             
                currC++;             
                currA--;         
            }         
            else{             
                currC++;             
                currA++;         
            }         
                maxA = max(maxA,currA);         
                maxC = max(maxC,currC);     
        }     
        cout<<max(maxA,maxC)<<endl;     
    } 
}

#https://www.hackerearth.com/problem/algorithm/free-walk-0f675f40-0d59a400/discussion/easy-solution-on-c2553b35/