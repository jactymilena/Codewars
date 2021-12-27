// link : https://www.codewars.com/kata/5287e858c6b5a9678200083c

#include <iostream>
#include <vector>
#include <cmath>

bool narcissistic(int value) {
  int nb_digits =  log10(value) + 1;
  int sum = 0;
  int save_value = value;
  // Separation du mot en digits et addition
  while(value > 0) {
    sum += (int) pow(value % 10, nb_digits);
    value /= 10;
  }

  return sum == save_value; 
}

int main(int argc, char const *argv[]) {
  std::cout << narcissistic(153) << std::endl;
  return 0;
}
