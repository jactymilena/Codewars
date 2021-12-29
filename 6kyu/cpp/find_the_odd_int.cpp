// link : https://www.codewars.com/kata/54da5a58ea159efa38000836

#include <iostream>
#include <vector>
#include <map>

using V = std::vector<int>;

int findOdd(const std::vector<int>& numbers){
  std::map<int, int> occurences;
  for(int n : numbers) // nombre d'occurences 
    occurences[n]++;

  for(int n : numbers) 
    if(occurences[n] % 2 != 0) // nombre impair
      return n;
  
}

int main(int argc, char const *argv[])
{
    std::cout << findOdd(V{20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5});
    return 0;
}
