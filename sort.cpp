#include <algorithm>
#include <functional>
#include <array>
#include <iostream>

bool lessthan(int a, int b)
{
        return a > b;
}
 int main()
 {
        std::array<int, 10> s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
        std::sort(s.begin(), s.end());
        for (int a : s) {
                std::cout << a << " ";
        }
        std::cout << '\n';

//      std::sort(s.begin(), s.end(), std::greater<int>());
        std::sort(s.begin(), s.end(), lessthan);

        for (int a : s) {
                std::cout << a << " ";
        }
        std::cout << '\n';
}
