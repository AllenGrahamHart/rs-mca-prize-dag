#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

namespace {

struct Match {
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
  int conductor = 0;
  int m3 = 0;
};

int third_moment(const std::array<int, 128>& product) {
  std::array<int, 128> weights{};
  std::vector<int> support;
  for (int difference = 1; difference < 64; ++difference) {
    const int magnitude = std::abs(product[difference]);
    if (!magnitude) continue;
    weights[difference] = weights[128 - difference] = magnitude;
    support.push_back(difference);
    support.push_back(128 - difference);
  }
  int answer = 0;
  for (int left : support) {
    for (int right : support) {
      answer += weights[left] * weights[right] *
                weights[(256 - left - right) % 128];
    }
  }
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
  std::uint64_t profile_count = 0;
  std::uint64_t above_cutoff = 0;
  std::uint64_t full_above_cutoff = 0;
  int maximum_m3 = -1;
  int maximum_full_m3 = -1;
  std::vector<Match> matches;
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
          bool above_two = false;
          for (int difference = 1; difference < 64; ++difference) {
            const int magnitude = std::abs(product[difference]);
            ones += magnitude == 1;
            twos += magnitude == 2;
            above_two = above_two || magnitude > 2;
          }
          if (above_two || ones != 6 || twos != 6) continue;
          ++profile_count;
          const int m3 = third_moment(product);
          maximum_m3 = std::max(maximum_m3, m3);
          if (conductor == 1) maximum_full_m3 = std::max(maximum_full_m3, m3);
          if (m3 <= 1087) continue;
          ++above_cutoff;
          full_above_cutoff += conductor == 1;
          matches.push_back({positions, coefficients, conductor, m3});
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"template\":" << template_index
            << ",\"light\":";
  print_array(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_count\":" << profile_count
            << ",\"above_cutoff\":" << above_cutoff
            << ",\"full_above_cutoff\":" << full_above_cutoff
            << ",\"maximum_m3\":" << maximum_m3
            << ",\"maximum_full_m3\":" << maximum_full_m3
            << ",\"matches\":[";
  for (std::size_t index = 0; index < matches.size(); ++index) {
    if (index) std::cout << ',';
    const Match& match = matches[index];
    std::cout << "{\"positions\":";
    print_array(match.positions);
    std::cout << ",\"coefficients\":";
    print_array(match.coefficients);
    std::cout << ",\"conductor\":" << match.conductor
              << ",\"m3\":" << match.m3 << '}';
  }
  std::cout << "]}\n";
  return 0;
}
