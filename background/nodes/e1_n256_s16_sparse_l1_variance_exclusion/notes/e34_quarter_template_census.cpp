#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

struct Witness {
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
  int m3 = 0;
};

int main(int argc, char** argv) {
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);

  std::vector<int> allowed;
  for (int value = 0; value < 128; ++value) {
    if (value != 0 && value != 32 && value != 64 && value != 96) {
      allowed.push_back(value);
    }
  }
  if (shard < 0 || shard + 3 >= static_cast<int>(allowed.size())) return 3;

  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::uint64_t energy_34 = 0;
  std::uint64_t profile_67 = 0;
  std::uint64_t full_conductor = 0;
  int maximum_m3 = -1;
  std::vector<Witness> witnesses;

  const int first = allowed[shard];
  for (int j = shard + 1; j < static_cast<int>(allowed.size()) - 2; ++j) {
    for (int k = j + 1; k < static_cast<int>(allowed.size()) - 1; ++k) {
      for (int l = k + 1; l < static_cast<int>(allowed.size()); ++l) {
        ++supports;
        const std::array<int, 7> positions = {
            0, 32, 64, first, allowed[j], allowed[k], allowed[l]};
        for (int middle_sign : {-1, 1}) {
          for (int mask = 0; mask < 16; ++mask) {
            ++vectors;
            const std::array<int, 7> coefficients = {
                2,
                2 * middle_sign,
                -2,
                (mask & 1) ? -1 : 1,
                (mask & 2) ? -1 : 1,
                (mask & 4) ? -1 : 1,
                (mask & 8) ? -1 : 1,
            };

            std::array<int, 64> half{};
            for (int left_index = 0; left_index < 7; ++left_index) {
              for (int right_index = left_index + 1; right_index < 7; ++right_index) {
                int left = positions[left_index];
                int right = positions[right_index];
                if (left > right) std::swap(left, right);
                const int difference = right - left;
                const int product = coefficients[left_index] * coefficients[right_index];
                if (difference == 64) continue;
                if (difference < 64) {
                  half[difference] += product;
                } else {
                  half[128 - difference] -= product;
                }
              }
            }

            int energy = 0;
            int l1 = 0;
            std::array<int, 8> profile{};
            for (int difference = 1; difference < 64; ++difference) {
              const int magnitude = std::abs(half[difference]);
              energy += magnitude * magnitude;
              l1 += magnitude;
              if (magnitude < static_cast<int>(profile.size())) ++profile[magnitude];
            }
            if (energy != 34) continue;
            ++energy_34;
            if (l1 != 20 || profile[1] != 6 || profile[2] != 7) continue;
            bool other = false;
            for (int magnitude = 3; magnitude < static_cast<int>(profile.size()); ++magnitude) {
              other = other || profile[magnitude] != 0;
            }
            if (other) continue;
            ++profile_67;

            int conductor = 256;
            for (int position : positions) conductor = std::gcd(conductor, position);
            if (conductor != 1) continue;
            ++full_conductor;

            std::array<int, 128> weight{};
            for (int difference = 1; difference < 64; ++difference) {
              weight[difference] = std::abs(half[difference]);
              weight[128 - difference] = weight[difference];
            }
            int m3 = 0;
            for (int x = 0; x < 128; ++x) {
              if (!weight[x]) continue;
              for (int y = 0; y < 128; ++y) {
                if (!weight[y]) continue;
                const int z = (256 - x - y) % 128;
                m3 += weight[x] * weight[y] * weight[z];
              }
            }
            maximum_m3 = std::max(maximum_m3, m3);
            if (witnesses.size() < 3) witnesses.push_back({positions, coefficients, m3});
          }
        }
      }
    }
  }

  std::cout << "{\"complete\":true"
            << ",\"shard\":" << shard
            << ",\"supports\":" << supports
            << ",\"vectors\":" << vectors
            << ",\"energy_34\":" << energy_34
            << ",\"profile_67\":" << profile_67
            << ",\"full_conductor\":" << full_conductor
            << ",\"maximum_m3\":" << maximum_m3
            << ",\"witnesses\":[";
  for (std::size_t index = 0; index < witnesses.size(); ++index) {
    if (index) std::cout << ',';
    std::cout << "{\"positions\":[";
    for (int i = 0; i < 7; ++i) {
      if (i) std::cout << ',';
      std::cout << witnesses[index].positions[i];
    }
    std::cout << "],\"coefficients\":[";
    for (int i = 0; i < 7; ++i) {
      if (i) std::cout << ',';
      std::cout << witnesses[index].coefficients[i];
    }
    std::cout << "],\"m3\":" << witnesses[index].m3 << '}';
  }
  std::cout << "]}\n";
  return 0;
}
