#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

bool valid_representative(int t) {
  return t == 1 || t == 2 || t == 4 || t == 8 || t == 16;
}

int circular_distance(int left, int right) {
  const int delta = std::abs(left - right);
  return std::min(delta, 128 - delta);
}

int main(int argc, char** argv) {
  if (argc != 2) return 2;
  const int t = std::atoi(argv[1]);
  if (!valid_representative(t)) return 3;

  const std::array<int, 3> heavy = {0, t, 2 * t};
  std::vector<int> allowed;
  for (int value = 0; value < 128; ++value) {
    if (value != heavy[0] && value != heavy[1] && value != heavy[2]) {
      allowed.push_back(value);
    }
  }
  const int outer_length = circular_distance(heavy[0], heavy[2]);

  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::uint64_t energy_34 = 0;
  std::uint64_t profile_67 = 0;
  std::uint64_t full_conductor = 0;
  int maximum_m3 = -1;

  for (int i = 0; i < static_cast<int>(allowed.size()) - 3; ++i) {
    for (int j = i + 1; j < static_cast<int>(allowed.size()) - 2; ++j) {
      for (int k = j + 1; k < static_cast<int>(allowed.size()) - 1; ++k) {
        for (int l = k + 1; l < static_cast<int>(allowed.size()); ++l) {
          const std::array<int, 4> light = {
              allowed[i], allowed[j], allowed[k], allowed[l]};
          bool welded = false;
          for (int light_position : light) {
            for (int heavy_position : heavy) {
              welded = welded ||
                  circular_distance(light_position, heavy_position) == outer_length;
            }
          }
          if (!welded) continue;
          ++supports;

          const std::array<int, 7> positions = {
              0, t, 2 * t, light[0], light[1], light[2], light[3]};
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

              std::array<int, 128> product_coefficients{};
              for (int left = 0; left < 7; ++left) {
                for (int right = 0; right < 7; ++right) {
                  const int reverse_exponent =
                      positions[right] == 0 ? 0 : 128 - positions[right];
                  const int reverse_coefficient =
                      positions[right] == 0 ? coefficients[right] : -coefficients[right];
                  const int exponent = positions[left] + reverse_exponent;
                  const int residue = exponent % 128;
                  const int wrap_sign = exponent >= 128 ? -1 : 1;
                  product_coefficients[residue] +=
                      wrap_sign * coefficients[left] * reverse_coefficient;
                }
              }
              if (product_coefficients[0] != 16) return 4;

              int energy = 0;
              int l1 = 0;
              std::array<int, 8> profile{};
              for (int difference = 1; difference < 64; ++difference) {
                const int magnitude = std::abs(product_coefficients[difference]);
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
              for (int difference = 1; difference < 64; ++difference) {
                weight[difference] = std::abs(product_coefficients[difference]);
                weight[128 - difference] = weight[difference];
              }
              int m3 = 0;
              for (int x = 0; x < 128; ++x) {
                if (!weight[x]) continue;
                for (int y = 0; y < 128; ++y) {
                  if (!weight[y]) continue;
                  m3 += weight[x] * weight[y] * weight[(256 - x - y) % 128];
                }
              }
              maximum_m3 = std::max(maximum_m3, m3);
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
            << ",\"maximum_m3\":" << maximum_m3 << "}\n";
  return 0;
}
