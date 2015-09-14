#include <iostream>
#include <algorithm>
#include <array>

int main()
{
        std::array<int, 6> v = {3, 1, 4, 1, 5, 9};
        std::make_heap(v.begin(), v.end());

        for (auto i : v)
                std::cout << i << ' ';
        std::cout << '\n';

        for (auto last = v.end(); last != v.begin(); last--)
                std::pop_heap(v.begin(), last);

        for (auto i : v)
                std::cout << i << ' ';
        std::cout << '\n';
        return 0;
}
