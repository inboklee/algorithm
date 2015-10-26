#include <iostream>
#include <string>

void bruteforce(std::string &T, std::string &P)
{
    int n = T.length();
    int m = P.length();

    for (int i = 0; i < n-m+1; i++) {
        bool isMatch = true;
        for (int j = 0; j < m; j++) {
            if (T[i+j] != P[j]) {
                isMatch = false;
                break;
            }
        }
        if (isMatch == true) {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;
}


int main()
{
  std::string T = "Hello Hello How are you";
  std::string P = "ello";

  bruteforce(T, P);
  return 0;
}
