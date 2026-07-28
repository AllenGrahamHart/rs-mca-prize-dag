#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

namespace {

constexpr int kThreshold = 228;
constexpr int kProfiles = 4;

struct Match {
  int profile = 0;
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
  int m3 = 0;
};

int identify_profile(const std::array<int, 128>& product) {
  int ones = 0;
  int twos = 0;
  int threes = 0;
  int fours = 0;
  for (int difference = 1; difference < 64; ++difference) {
    const int magnitude = std::abs(product[difference]);
    if (magnitude > 4) return -1;
    ones += magnitude == 1;
    twos += magnitude == 2;
    threes += magnitude == 3;
    fours += magnitude == 4;
  }
  if (ones == 6 && twos == 5 && threes == 0 && fours == 0) return 0;
  if (ones == 5 && twos == 3 && threes == 1 && fours == 0) return 1;
  if (ones == 4 && twos == 1 && threes == 2 && fours == 0) return 2;
  if (ones == 6 && twos == 1 && threes == 0 && fours == 1) return 3;
  return -1;
}

int moment_three(const std::array<int, 128>& product) {
  std::array<int, 128> weight{};
  std::vector<int> support;
  for (int difference = 1; difference < 64; ++difference) {
    const int magnitude = std::abs(product[difference]);
    if (!magnitude) continue;
    weight[difference] = weight[128 - difference] = magnitude;
    support.push_back(difference);
    support.push_back(128 - difference);
  }
  int result = 0;
  for (int first : support) {
    for (int second : support) {
      result += weight[first] * weight[second] *
                weight[(256 - first - second) % 128];
    }
  }
  return result;
}

template <typename Values>
void print_values(const Values& values) {
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
  std::array<std::uint64_t, kProfiles> profile_counts{};
  std::array<std::uint64_t, kProfiles> above_cutoff{};
  std::array<std::uint64_t, kProfiles> full_above_cutoff{};
  std::array<int, kProfiles> maximum_m3{{-1, -1, -1, -1}};
  std::array<int, kProfiles> maximum_full_m3{{-1, -1, -1, -1}};
  std::vector<Match> matches;
  for (int first = 0; first < static_cast<int>(allowed.size()) - 2; ++first) {
    for (int second = first + 1; second < static_cast<int>(allowed.size()) - 1;
         ++second) {
      for (int third = second + 1; third < static_cast<int>(allowed.size());
           ++third) {
        ++supports;
        const std::array<int, 7> positions{{
            allowed[first], allowed[second], allowed[third], light[0],
            light[1], light[2], light[3],
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
              product[exponent % 128] +=
                  (exponent >= 128 ? -1 : 1) * coefficients[left] *
                  reverse_coefficient;
            }
          }
          if (product[0] != 16) return 3;
          for (int difference = 1; difference < 64; ++difference) {
            if (product[128 - difference] != -product[difference]) return 4;
          }
          const int profile = identify_profile(product);
          if (profile < 0) continue;
          ++profile_counts[profile];
          const int m3 = moment_three(product);
          maximum_m3[profile] = std::max(maximum_m3[profile], m3);
          if (conductor == 1) {
            maximum_full_m3[profile] = std::max(maximum_full_m3[profile], m3);
          }
          if (m3 <= kThreshold) continue;
          ++above_cutoff[profile];
          if (conductor != 1) continue;
          ++full_above_cutoff[profile];
          matches.push_back({profile, positions, coefficients, m3});
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"template\":" << template_index
            << ",\"light\":";
  print_values(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_counts\":";
  print_values(profile_counts);
  std::cout << ",\"above_cutoff\":";
  print_values(above_cutoff);
  std::cout << ",\"full_above_cutoff\":";
  print_values(full_above_cutoff);
  std::cout << ",\"maximum_m3\":";
  print_values(maximum_m3);
  std::cout << ",\"maximum_full_m3\":";
  print_values(maximum_full_m3);
  std::cout << ",\"matches\":[";
  for (std::size_t index = 0; index < matches.size(); ++index) {
    if (index) std::cout << ',';
    const Match& match = matches[index];
    std::cout << "{\"profile\":" << match.profile << ",\"positions\":";
    print_values(match.positions);
    std::cout << ",\"coefficients\":";
    print_values(match.coefficients);
    std::cout << ",\"m3\":" << match.m3 << '}';
  }
  std::cout << "]}\n";
  return 0;
}
