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

int distance(int left, int right) {
  const int delta = std::abs(left - right);
  return std::min(delta, 128 - delta);
}

int main(int argc, char** argv) {
  if (argc != 4) return 2;
  const int orbit = std::atoi(argv[1]);
  const int a = std::atoi(argv[2]);
  const int b = std::atoi(argv[3]);
  if (orbit < 0 || orbit >= 57 || a <= 0 || a >= b || b >= 128) return 3;
  const std::array<int, 3> heavy = {0, a, b};

  std::array<int, 3> lengths = {
      distance(0, a), distance(0, b), distance(a, b)};
  std::sort(lengths.begin(), lengths.end());
  if (lengths[2] == 64 || lengths[0] == lengths[1] || lengths[1] == lengths[2]) return 4;

  std::array<std::array<bool, 128>, 3> weld{};
  for (int index = 0; index < 3; ++index) {
    for (int h : heavy) {
      for (int sign : {-1, 1}) {
        const int light = (h + sign * lengths[index] + 128) % 128;
        if (std::find(heavy.begin(), heavy.end(), light) == heavy.end()) {
          weld[index][light] = true;
        }
      }
    }
  }

  std::vector<int> allowed;
  for (int value = 0; value < 128; ++value) {
    if (std::find(heavy.begin(), heavy.end(), value) == heavy.end()) {
      allowed.push_back(value);
    }
  }

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
          bool eligible = true;
          for (int weld_index = 0; weld_index < 3; ++weld_index) {
            bool hit = false;
            for (int position : light) hit = hit || weld[weld_index][position];
            eligible = eligible && hit;
          }
          if (!eligible) continue;
          ++supports;

          const std::array<int, 7> positions = {
              0, a, b, light[0], light[1], light[2], light[3]};
          for (int second_sign : {-1, 1}) {
            for (int third_sign : {-1, 1}) {
              for (int mask = 0; mask < 16; ++mask) {
                ++vectors;
                const std::array<int, 7> coefficients = {
                    2,
                    2 * second_sign,
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

  std::cout << "{\"complete\":true,\"orbit\":" << orbit
            << ",\"heavy\":[0," << a << ',' << b << ']'
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
