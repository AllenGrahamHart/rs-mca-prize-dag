#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

namespace {

constexpr std::array<std::array<int, 4>, 8> kProfiles{{
    {{6, 4, 0, 0}},
    {{2, 5, 0, 0}},
    {{5, 2, 1, 0}},
    {{1, 3, 1, 0}},
    {{4, 0, 2, 0}},
    {{0, 1, 2, 0}},
    {{6, 0, 0, 1}},
    {{2, 1, 0, 1}},
}};

std::uint64_t content_hash(int profile, const std::array<int, 7>& positions,
                           const std::array<int, 7>& coefficients,
                           int conductor) {
  std::uint64_t answer = 1469598103934665603ULL;
  const auto mix = [&answer](std::uint64_t value) {
    answer ^= value;
    answer *= 1099511628211ULL;
  };
  mix(static_cast<std::uint64_t>(profile + 1));
  for (int value : positions) mix(static_cast<std::uint64_t>(value + 1));
  for (int value : coefficients) mix(static_cast<std::uint64_t>(value + 3));
  mix(static_cast<std::uint64_t>(conductor + 1));
  return answer;
}

template <typename Values>
void print_array(const Values& values) {
  std::cout << '[';
  for (std::size_t index = 0; index < values.size(); ++index) {
    if (index) std::cout << ',';
    std::cout << values[index];
  }
  std::cout << ']';
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 6) return 2;
  const int template_index = std::atoi(argv[1]);
  const std::array<int, 4> light{{
      std::atoi(argv[2]), std::atoi(argv[3]), std::atoi(argv[4]),
      std::atoi(argv[5]),
  }};
  std::array<bool, 128> occupied{};
  for (int position : light) {
    if (position < 0 || position >= 128 || occupied[position]) return 2;
    occupied[position] = true;
  }
  std::vector<int> allowed;
  for (int position = 0; position < 128; ++position) {
    if (!occupied[position]) allowed.push_back(position);
  }

  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::array<std::uint64_t, 8> profile_counts{};
  std::array<std::uint64_t, 8> full_conductor_counts{};
  std::array<std::uint64_t, 8> hash_sums{};
  std::array<std::uint64_t, 8> hash_xors{};

  for (int first = 0; first < static_cast<int>(allowed.size()) - 2; ++first) {
    for (int second = first + 1; second < static_cast<int>(allowed.size()) - 1;
         ++second) {
      for (int third = second + 1; third < static_cast<int>(allowed.size());
           ++third) {
        ++supports;
        const std::array<int, 7> positions{{
            allowed[first], allowed[second], allowed[third], light[0], light[1],
            light[2], light[3],
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
                  positions[right] == 0 ? coefficients[right]
                                        : -coefficients[right];
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
          std::array<int, 4> profile{};
          bool above_four = false;
          for (int difference = 1; difference < 64; ++difference) {
            const int magnitude = std::abs(product[difference]);
            if (magnitude > 4) {
              above_four = true;
            } else if (magnitude > 0) {
              ++profile[magnitude - 1];
            }
          }
          if (above_four) continue;
          const auto found = std::find(kProfiles.begin(), kProfiles.end(), profile);
          if (found == kProfiles.end()) continue;
          const int profile_index = static_cast<int>(found - kProfiles.begin());
          ++profile_counts[profile_index];
          full_conductor_counts[profile_index] += conductor == 1;
          const std::uint64_t hash =
              content_hash(profile_index, positions, coefficients, conductor);
          hash_sums[profile_index] += hash;
          hash_xors[profile_index] ^= hash;
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"template\":" << template_index
            << ",\"light\":";
  print_array(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_counts\":";
  print_array(profile_counts);
  std::cout << ",\"full_conductor_counts\":";
  print_array(full_conductor_counts);
  std::cout << ",\"hash_sums\":";
  print_array(hash_sums);
  std::cout << ",\"hash_xors\":";
  print_array(hash_xors);
  std::cout << "}\n";
  return 0;
}
