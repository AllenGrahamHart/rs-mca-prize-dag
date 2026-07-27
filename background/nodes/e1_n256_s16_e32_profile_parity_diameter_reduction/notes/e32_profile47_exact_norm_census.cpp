#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

int folded_class(int left, int right, int& orientation) {
  if (left > right) std::swap(left, right);
  const int difference = right - left;
  if (difference == 64) {
    orientation = 0;
    return 64;
  }
  if (difference < 64) {
    orientation = 1;
    return difference;
  }
  orientation = -1;
  return 128 - difference;
}

int main(int argc, char** argv) {
  if (argc != 6) return 2;
  const int template_index = std::atoi(argv[1]);
  const std::array<int, 4> light{{
      std::atoi(argv[2]), std::atoi(argv[3]),
      std::atoi(argv[4]), std::atoi(argv[5]),
  }};
  if (template_index < 0 || template_index >= 148) return 2;

  std::array<bool, 128> occupied{};
  for (int position : light) {
    if (position < 0 || position >= 128 || occupied[position]) return 2;
    occupied[position] = true;
  }
  std::vector<int> allowed;
  for (int position = 0; position < 128; ++position) {
    if (!occupied[position]) allowed.push_back(position);
  }

  for (int first = 0; first < static_cast<int>(allowed.size()) - 2; ++first) {
    for (int second = first + 1; second < static_cast<int>(allowed.size()) - 1;
         ++second) {
      for (int third = second + 1; third < static_cast<int>(allowed.size());
           ++third) {
        const std::array<int, 7> positions{{
            allowed[first], allowed[second], allowed[third],
            light[0], light[1], light[2], light[3],
        }};
        int conductor = 256;
        for (int position : positions) conductor = std::gcd(conductor, position);
        if (conductor != 1) continue;

        std::array<int, 21> chord_class{};
        std::array<int, 21> chord_orientation{};
        std::array<int, 21> chord_left{};
        std::array<int, 21> chord_right{};
        int chord = 0;
        for (int left = 0; left < 7; ++left) {
          for (int right = left + 1; right < 7; ++right) {
            chord_class[chord] = folded_class(
                positions[left], positions[right], chord_orientation[chord]);
            chord_left[chord] = left;
            chord_right[chord] = right;
            ++chord;
          }
        }

        for (int mask = 0; mask < 64; ++mask) {
          const std::array<int, 7> coefficients{{
              2,
              (mask & 1) ? -2 : 2,
              (mask & 2) ? -2 : 2,
              (mask & 4) ? -1 : 1,
              (mask & 8) ? -1 : 1,
              (mask & 16) ? -1 : 1,
              (mask & 32) ? -1 : 1,
          }};
          std::array<int, 64> half{};
          for (int index = 0; index < 21; ++index) {
            if (chord_class[index] == 64) continue;
            half[chord_class[index]] +=
                chord_orientation[index] * coefficients[chord_left[index]] *
                coefficients[chord_right[index]];
          }

          int ones = 0;
          int twos = 0;
          int threes = 0;
          bool above_three = false;
          for (int difference = 1; difference < 64; ++difference) {
            const int magnitude = std::abs(half[difference]);
            ones += magnitude == 1;
            twos += magnitude == 2;
            threes += magnitude == 3;
            above_three = above_three || magnitude > 3;
          }
          if (above_three || ones != 4 || twos != 7 || threes != 0) continue;

          for (int value : positions) std::cout << value << ' ';
          for (int index = 0; index < 7; ++index) {
            if (index) std::cout << ' ';
            std::cout << coefficients[index];
          }
          std::cout << '\n';
        }
      }
    }
  }
  return 0;
}
