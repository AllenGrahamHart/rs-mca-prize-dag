#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

struct Witness {
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
  int m3 = 0;
};

bool contains(const std::array<int, 4>& light, int value) {
  return std::find(light.begin(), light.end(), value) != light.end();
}

int main(int argc, char** argv) {
  if (argc != 2) return 2;
  const int t = std::atoi(argv[1]);
  if (t < 1 || t > 31) return 3;

  std::vector<int> allowed;
  for (int value = 0; value < 128; ++value) {
    if (value != 0 && value != 64 && value != t) allowed.push_back(value);
  }

  const std::array<int, 3> common = {64 - t, 64 + t, 128 - t};
  const std::array<int, 2> exceptional = {2 * t, 64 + 2 * t};
  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::uint64_t energy_34 = 0;
  std::uint64_t profile_67 = 0;
  std::uint64_t full_conductor = 0;
  int maximum_m3 = -1;
  std::vector<Witness> witnesses;

  for (int i = 0; i < static_cast<int>(allowed.size()) - 3; ++i) {
    for (int j = i + 1; j < static_cast<int>(allowed.size()) - 2; ++j) {
      for (int k = j + 1; k < static_cast<int>(allowed.size()) - 1; ++k) {
        for (int l = k + 1; l < static_cast<int>(allowed.size()); ++l) {
          const std::array<int, 4> light = {
              allowed[i], allowed[j], allowed[k], allowed[l]};
          const bool common_weld =
              contains(light, common[0]) || contains(light, common[1]) ||
              contains(light, common[2]);
          const bool paired_weld =
              contains(light, exceptional[0]) && contains(light, exceptional[1]);
          if (!common_weld && !paired_weld) continue;
          ++supports;

          const std::array<int, 7> positions = {
              0, 64, t, light[0], light[1], light[2], light[3]};
          for (int antipodal_sign : {-1, 1}) {
            for (int third_sign : {-1, 1}) {
              for (int mask = 0; mask < 16; ++mask) {
                ++vectors;
                const std::array<int, 7> coefficients = {
                    2,
                    2 * antipodal_sign,
                    2 * third_sign,
                    (mask & 1) ? -1 : 1,
                    (mask & 2) ? -1 : 1,
                    (mask & 4) ? -1 : 1,
                    (mask & 8) ? -1 : 1,
                };

                std::array<int, 64> half{};
                for (int left_index = 0; left_index < 7; ++left_index) {
                  for (int right_index = left_index + 1; right_index < 7;
                       ++right_index) {
                    int left = positions[left_index];
                    int right = positions[right_index];
                    if (left > right) std::swap(left, right);
                    const int difference = right - left;
                    const int product =
                        coefficients[left_index] * coefficients[right_index];
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
                  if (magnitude < static_cast<int>(profile.size())) {
                    ++profile[magnitude];
                  }
                }
                if (energy != 34) continue;
                ++energy_34;
                if (l1 != 20 || profile[1] != 6 || profile[2] != 7) continue;
                bool other = false;
                for (int magnitude = 3;
                     magnitude < static_cast<int>(profile.size()); ++magnitude) {
                  other = other || profile[magnitude] != 0;
                }
                if (other) continue;
                ++profile_67;

                int conductor = 256;
                for (int position : positions) conductor = std::gcd(conductor, position);
                if (conductor != 1) continue;
                ++full_conductor;

                std::array<int, 128> weight{};
                std::vector<int> active;
                for (int difference = 1; difference < 64; ++difference) {
                  weight[difference] = std::abs(half[difference]);
                  weight[128 - difference] = weight[difference];
                  if (weight[difference]) {
                    active.push_back(difference);
                    active.push_back(128 - difference);
                  }
                }
                int m3 = 0;
                for (int x : active) {
                  for (int y : active) {
                    m3 += weight[x] * weight[y] * weight[(256 - x - y) % 128];
                  }
                }
                maximum_m3 = std::max(maximum_m3, m3);
                if (witnesses.size() < 3) {
                  witnesses.push_back({positions, coefficients, m3});
                }
              }
            }
          }
        }
      }
    }
  }

  std::cout << "{\"complete\":true"
            << ",\"t\":" << t
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
