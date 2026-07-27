#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>

using Light = std::array<int, 4>;

int distance_class(int left, int right) {
  const int forward = (left - right + 128) % 128;
  return std::min(forward, 128 - forward);
}

Light orbit_key(const Light& support) {
  Light answer{{128, 128, 128, 128}};
  for (int multiplier = 1; multiplier < 128; multiplier += 2) {
    for (bool swap_diameter : {false, true}) {
      Light image{};
      for (int index = 0; index < 4; ++index) {
        image[index] =
            (multiplier * support[index] + (swap_diameter ? 64 : 0)) % 128;
      }
      std::sort(image.begin(), image.end());
      if (image < answer) answer = image;
    }
  }
  return answer;
}

std::vector<Light> classify_lights() {
  std::set<Light> orbits;
  for (int x = 1; x < 128; ++x) {
    if (x == 64) continue;
    for (int y = x + 1; y < 128; ++y) {
      if (y == 64) continue;
      Light support{{0, 64, x, y}};
      std::array<int, 65> multiplicity{};
      for (int left = 0; left < 4; ++left) {
        for (int right = left + 1; right < 4; ++right) {
          ++multiplicity[distance_class(support[left], support[right])];
        }
      }
      if (multiplicity[64] != 1) continue;
      bool sidon = true;
      for (int distance = 1; distance < 64; ++distance) {
        sidon = sidon && multiplicity[distance] <= 1;
      }
      if (sidon) orbits.insert(orbit_key(support));
    }
  }
  return {orbits.begin(), orbits.end()};
}

int main(int argc, char** argv) {
  if (argc != 2) return 2;
  const int template_index = std::atoi(argv[1]);
  const auto templates = classify_lights();
  if (templates.size() != 100 || template_index < 0 ||
      template_index >= static_cast<int>(templates.size())) {
    return 2;
  }
  const Light light = templates[template_index];

  std::array<bool, 128> occupied{};
  for (int position : light) occupied[position] = true;
  std::vector<int> available;
  for (int position = 0; position < 128; ++position) {
    if (!occupied[position]) available.push_back(position);
  }

  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::uint64_t profile_57 = 0;
  std::uint64_t full_conductor = 0;
  int maximum_m3 = -1;
  int maximum_full_conductor_m3 = -1;

  for (int a = 0; a < static_cast<int>(available.size()) - 2; ++a) {
    for (int b = a + 1; b < static_cast<int>(available.size()) - 1; ++b) {
      for (int c = b + 1; c < static_cast<int>(available.size()); ++c) {
        ++supports;
        const std::array<int, 7> positions{{
            available[a], available[b], available[c],
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

          // Form F(X)F(X^-1) directly in Z[X]/(X^128+1).
          std::array<int, 128> product{};
          for (int left = 0; left < 7; ++left) {
            for (int right = 0; right < 7; ++right) {
              const int reverse_exponent =
                  positions[right] == 0 ? 0 : 128 - positions[right];
              const int reverse_coefficient =
                  positions[right] == 0 ? coefficients[right] : -coefficients[right];
              const int exponent = positions[left] + reverse_exponent;
              product[exponent % 128] +=
                  (exponent >= 128 ? -1 : 1) * coefficients[left] *
                  reverse_coefficient;
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
          if (ones != 5 || twos != 7 || other) continue;
          ++profile_57;

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

  std::cout << "{\"complete\":true,\"templates\":" << templates.size()
            << ",\"template\":" << template_index << ",\"light\":[";
  for (int index = 0; index < 4; ++index) {
    if (index) std::cout << ',';
    std::cout << light[index];
  }
  std::cout << "],\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_57\":" << profile_57
            << ",\"full_conductor\":" << full_conductor
            << ",\"maximum_m3\":" << maximum_m3
            << ",\"maximum_full_conductor_m3\":"
            << maximum_full_conductor_m3 << "}\n";
  return 0;
}
