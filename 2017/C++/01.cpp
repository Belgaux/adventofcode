#include <fstream>
#include <iostream>
#include <vector>
#include <cstddef>

// TODO: Extract this to some utils library?
std::vector<std::string> read_lines(const std::string &filename)
{
    std::vector<std::string> vec;
    std::ifstream f(filename);
    std::string s;
    while (std::getline(f, s)) {
        vec.push_back(s);
    }
    return vec;
}

int char_to_int(char c)
{
    int n = c - '0';
    return n;
}

int captcha_sum_naive(std::string str, bool halfway=false)
{
    int sum = 0;
    for (std::size_t i = 0; i < str.size(); ++i) {
        std::size_t i_next;
        if (halfway)
            i_next = (i + str.size() / 2) % str.size();
        else
            i_next = i < (str.size() - 1) ? i + 1 : 0;
        int num = char_to_int(str[i]);
        int next_num = char_to_int(str[i_next]);
        if (num == next_num)
            sum += num;
    }

    return sum;
}

int main()
{
    auto v = read_lines("../../inputs/01.txt");
    for (const auto& e : v) {
        std::cout << captcha_sum_naive(e) << std::endl;
        std::cout << captcha_sum_naive(e, true) << std::endl;
    }

    return 0;
}
