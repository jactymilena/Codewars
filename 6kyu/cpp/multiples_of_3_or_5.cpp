// link : https://www.codewars.com/kata/514b92a657cdc65150000006

#include <iostream>

int solution(int number) {
  int sum = 0;
  for(int i = 0; i < number; i++) {
    if(i % 3 == 0 || i % 5 == 0)
      sum +=i;
  }
  
  return sum;
}

int main(int argc, char const *argv[]) {
  std::cout << solution(10) << std::endl;

  return 0;
}
