//https://www.codechef.com/problems/TOP10
#include <stdio.h>

int main() {
    int N,i;
    scanf("%d",&N);
    while(N--){
    scanf("%d",&i);
    if(i<=10)
    printf("YES\n");
    else
    printf("NO\n");
    }

}
