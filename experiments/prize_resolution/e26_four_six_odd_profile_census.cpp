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
constexpr std::array<std::array<int, 4>, kProfiles> kProfileCounts{{
    {{6, 5, 0, 0}}, {{5, 3, 1, 0}}, {{4, 1, 2, 0}}, {{6, 1, 0, 1}},
}};

struct Match {
  int profile = 0;
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
  int m3 = 0;
};

int folded_class(int left, int right, int& orientation) {
  if (left > right) std::swap(left, right);
  const int difference = right - left;
  if (difference == 64) {
    orientation = 0;
    return 64;
  }
  if (difference < 64) {
    orientation = 1;
    return difference;
  }
  orientation = -1;
  return 128 - difference;
}

int profile_of(const std::array<int, 64>& half) {
  std::array<int, 4> counts{};
  for (int difference = 1; difference < 64; ++difference) {
    const int magnitude = std::abs(half[difference]);
    if (magnitude > 4) return -1;
    if (magnitude) ++counts[magnitude - 1];
  }
  for (int profile = 0; profile < kProfiles; ++profile) {
    if (counts == kProfileCounts[profile]) return profile;
  }
  return -1;
}

int third_moment(const std::array<int, 64>& half) {
  std::array<int, 128> weights{};
  std::vector<int> support;
  for (int difference = 1; difference < 64; ++difference) {
    const int magnitude = std::abs(half[difference]);
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
        std::array<int, 21> chord_class{};
        std::array<int, 21> chord_orientation{};
        std::array<int, 21> chord_left{};
        std::array<int, 21> chord_right{};
        int chord = 0;
        for (int left = 0; left < 7; ++left) {
          for (int right = left + 1; right < 7; ++right) {
            chord_class[chord] = folded_class(
                positions[left], positions[right], chord_orientation[chord]);
            chord_left[chord] = left;
            chord_right[chord] = right;
            ++chord;
          }
        }
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
          std::array<int, 64> half{};
          for (int index = 0; index < 21; ++index) {
            if (chord_class[index] == 64) continue;
            half[chord_class[index]] +=
                chord_orientation[index] * coefficients[chord_left[index]] *
                coefficients[chord_right[index]];
          }
          const int profile = profile_of(half);
          if (profile < 0) continue;
          ++profile_counts[profile];
          const int m3 = third_moment(half);
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
  print_array(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_counts\":";
  print_array(profile_counts);
  std::cout << ",\"above_cutoff\":";
  print_array(above_cutoff);
  std::cout << ",\"full_above_cutoff\":";
  print_array(full_above_cutoff);
  std::cout << ",\"maximum_m3\":";
  print_array(maximum_m3);
  std::cout << ",\"maximum_full_m3\":";
  print_array(maximum_full_m3);
  std::cout << ",\"matches\":[";
  for (std::size_t index = 0; index < matches.size(); ++index) {
    if (index) std::cout << ',';
    const Match& match = matches[index];
    std::cout << "{\"profile\":" << match.profile << ",\"positions\":";
    print_array(match.positions);
    std::cout << ",\"coefficients\":";
    print_array(match.coefficients);
    std::cout << ",\"m3\":" << match.m3 << '}';
  }
  std::cout << "]}\n";
  return 0;
}
