#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

std::array<int, 4> light_template(int index) {
  constexpr std::array<std::array<int, 4>, 6> templates{{
      {{0, 1, 64, 65}},
      {{0, 2, 64, 66}},
      {{0, 4, 64, 68}},
      {{0, 8, 64, 72}},
      {{0, 16, 64, 80}},
      {{0, 32, 64, 96}},
  }};
  return templates[index];
}

int main(int argc, char** argv) {
  if (argc != 2) return 2;
  const int template_index = std::atoi(argv[1]);
  if (template_index < 0 || template_index >= 6) return 2;

  const auto light = light_template(template_index);
  std::array<bool, 128> occupied{};
  for (int position : light) occupied[position] = true;
  std::vector<int> allowed;
  for (int position = 0; position < 128; ++position) {
    if (!occupied[position]) allowed.push_back(position);
  }

  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::uint64_t profile_08 = 0;
  std::uint64_t full_conductor = 0;
  int maximum_m3 = -1;
  int maximum_full_conductor_m3 = -1;

  for (int first = 0; first < static_cast<int>(allowed.size()) - 2; ++first) {
    for (int second = first + 1; second < static_cast<int>(allowed.size()) - 1;
         ++second) {
      for (int third = second + 1; third < static_cast<int>(allowed.size());
           ++third) {
        ++supports;
        const std::array<int, 7> positions{{
            allowed[first], allowed[second], allowed[third],
            light[0], light[1], light[2], light[3],
        }};
        int conductor = 256;
        for (int position : positions) conductor = std::gcd(conductor, position);

        for (int mask = 0; mask < 64; ++mask) {
          ++vectors;
          const std::array<int, 7> coefficients{{
              2,
              (mask & 1) ? -2 : 2,
              (mask & 2) ? -2 : 2,
              (mask & 4) ? -1 : 1,
              (mask & 8) ? -1 : 1,
              (mask & 16) ? -1 : 1,
              (mask & 32) ? -1 : 1,
          }};

          std::array<int, 128> product{};
          for (int left = 0; left < 7; ++left) {
            for (int right = 0; right < 7; ++right) {
              const int reverse_exponent =
                  positions[right] == 0 ? 0 : 128 - positions[right];
              const int reverse_coefficient =
                  positions[right] == 0 ? coefficients[right] : -coefficients[right];
              const int exponent = positions[left] + reverse_exponent;
              const int residue = exponent % 128;
              const int wrap_sign = exponent >= 128 ? -1 : 1;
              product[residue] +=
                  wrap_sign * coefficients[left] * reverse_coefficient;
            }
          }
          if (product[0] != 16) return 3;
          for (int difference = 1; difference < 64; ++difference) {
            if (product[128 - difference] != -product[difference]) return 4;
          }

          int ones = 0;
          int twos = 0;
          bool other = false;
          for (int difference = 1; difference < 64; ++difference) {
            const int magnitude = std::abs(product[difference]);
            ones += magnitude == 1;
            twos += magnitude == 2;
            other = other || magnitude > 2;
          }
          if (ones != 0 || twos != 8 || other) continue;
          ++profile_08;

          std::array<int, 128> weight{};
          for (int difference = 1; difference < 64; ++difference) {
            weight[difference] = std::abs(product[difference]);
            weight[128 - difference] = weight[difference];
          }
          int m3 = 0;
          for (int left = 0; left < 128; ++left) {
            if (!weight[left]) continue;
            for (int right = 0; right < 128; ++right) {
              if (!weight[right]) continue;
              m3 += weight[left] * weight[right] *
                    weight[(256 - left - right) % 128];
            }
          }
          maximum_m3 = std::max(maximum_m3, m3);
          if (conductor == 1) {
            ++full_conductor;
            maximum_full_conductor_m3 =
                std::max(maximum_full_conductor_m3, m3);
          }
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"template\":" << template_index
            << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_08\":" << profile_08
            << ",\"full_conductor\":" << full_conductor
            << ",\"maximum_m3\":" << maximum_m3
            << ",\"maximum_full_conductor_m3\":"
            << maximum_full_conductor_m3 << "}\n";
  return 0;
}
