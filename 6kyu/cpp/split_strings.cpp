// link : https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> solution(const std::string &s) {
  std::vector<std::string> v;
  int stringSize = s.length();

  for(int i = 0; i < stringSize; i+=2) 
    v.push_back(s.substr(i, 2));

  if (stringSize % 2 != 0) 
    v[v.size() - 1] += "_";

  return v; 
}

int main(int argc, char *argv[]) {
    std::vector<std::string> v = solution("maisons");
    std::cout << "Affichage :\n";
    for (std::string c : v) {
      std::cout << c << std::endl;
    }

   return 0;
}