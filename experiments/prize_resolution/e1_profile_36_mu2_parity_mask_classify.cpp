#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>

namespace {

uint64_t OddChordMask(const std::array<int, 6>& support) {
  uint64_t mask = 0;
  for (int left = 0; left < 6; ++left) {
    for (int right = left + 1; right < 6; ++right) {
      int difference = support[right] - support[left];
      if (difference == 64) continue;
      const int lag = difference < 64 ? difference : 128 - difference;
      mask ^= uint64_t{1} << (lag - 1);
    }
  }
  return mask;
}

bool HasMultiplicityTwo(const std::array<int, 6>& support) {
  int derivative_one = 0;
  int derivative_two = 0;
  for (int exponent : support) {
    derivative_one ^= exponent & 1;
    derivative_two ^= (exponent >> 1) & 1;
  }
  return derivative_one == 0 && derivative_two == 1;
}

}  // namespace

int main() {
  std::array<int, 126> available{};
  int cursor = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 2) available[cursor++] = position;
  }

  uint64_t examined = 0;
  uint64_t multiplicity_two = 0;
  std::array<uint64_t, 16> raw_by_weight{};
  std::vector<uint64_t> masks;
  masks.reserve(3'000'000);
  for (int first = 0; first < 123; ++first) {
    for (int second = first + 1; second < 124; ++second) {
      for (int third = second + 1; third < 125; ++third) {
        for (int fourth = third + 1; fourth < 126; ++fourth) {
          ++examined;
          const std::array<int, 6> support = {
              0, 2, available[first], available[second], available[third],
              available[fourth]};
          std::array<int, 6> ordered = support;
          std::sort(ordered.begin(), ordered.end());
          if (!HasMultiplicityTwo(ordered)) continue;
          ++multiplicity_two;
          const uint64_t mask = OddChordMask(ordered);
          ++raw_by_weight[std::popcount(mask)];
          masks.push_back(mask);
        }
      }
    }
  }

  std::sort(masks.begin(), masks.end());
  masks.erase(std::unique(masks.begin(), masks.end()), masks.end());
  std::array<uint64_t, 16> unique_by_weight{};
  for (uint64_t mask : masks) ++unique_by_weight[std::popcount(mask)];

  std::cout << "examined=" << examined
            << " multiplicity_two=" << multiplicity_two
            << " unique_masks=" << masks.size() << '\n';
  std::cout << "raw_by_weight=";
  for (int weight = 0; weight < 16; ++weight) {
    if (raw_by_weight[weight]) {
      std::cout << weight << ':' << raw_by_weight[weight] << ',';
    }
  }
  std::cout << '\n';
  std::cout << "unique_by_weight=";
  for (int weight = 0; weight < 16; ++weight) {
    if (unique_by_weight[weight]) {
      std::cout << weight << ':' << unique_by_weight[weight] << ',';
    }
  }
  std::cout << '\n';

  if (examined != 10'009'125 || multiplicity_two == 0 || masks.empty()) {
    return 2;
  }
  std::cout << "E1_PROFILE_36_MU2_PARITY_MASK_CLASSIFY_PASS\n";
  return 0;
}
