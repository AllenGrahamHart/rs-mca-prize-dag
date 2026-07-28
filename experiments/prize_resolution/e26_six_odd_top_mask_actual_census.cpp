#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

namespace {

constexpr int kThreshold = 228;

struct Match {
  int m3 = 0;
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
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

bool matches_profile(int profile, const std::array<int, 64>& half) {
  std::array<int, 5> counts{};
  for (int difference = 1; difference < 64; ++difference) {
    const int magnitude = std::abs(half[difference]);
    if (magnitude >= static_cast<int>(counts.size())) return false;
    if (magnitude) ++counts[magnitude];
  }
  if (profile == 0) return counts == std::array<int, 5>{{0, 4, 1, 2, 0}};
  if (profile == 1) return counts == std::array<int, 5>{{0, 6, 1, 0, 1}};
  return false;
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
  if (argc != 7) return 2;
  const int task = std::atoi(argv[1]);
  const int profile = std::atoi(argv[2]);
  if (profile < 0 || profile > 1) return 2;
  const std::array<int, 4> light{{
      std::atoi(argv[3]), std::atoi(argv[4]), std::atoi(argv[5]),
      std::atoi(argv[6]),
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
  std::vector<Match> top;
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
          if (!matches_profile(profile, half)) continue;
          ++profile_count;
          const int m3 = third_moment(half);
          maximum_m3 = std::max(maximum_m3, m3);
          if (conductor == 1) maximum_full_m3 = std::max(maximum_full_m3, m3);
          if (m3 <= kThreshold) continue;
          ++above_cutoff;
          if (conductor != 1) continue;
          ++full_above_cutoff;
          top.push_back({m3, positions, coefficients});
          std::sort(top.begin(), top.end(), [](const Match& left, const Match& right) {
            return left.m3 > right.m3;
          });
          if (top.size() > 32) top.pop_back();
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"task\":" << task
            << ",\"profile\":" << profile << ",\"light\":";
  print_array(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_count\":" << profile_count
            << ",\"above_cutoff\":" << above_cutoff
            << ",\"full_above_cutoff\":" << full_above_cutoff
            << ",\"maximum_m3\":" << maximum_m3
            << ",\"maximum_full_m3\":" << maximum_full_m3
            << ",\"top\":[";
  for (std::size_t index = 0; index < top.size(); ++index) {
    if (index) std::cout << ',';
    std::cout << "{\"m3\":" << top[index].m3 << ",\"positions\":";
    print_array(top[index].positions);
    std::cout << ",\"coefficients\":";
    print_array(top[index].coefficients);
    std::cout << '}';
  }
  std::cout << "]}\n";
  return 0;
}
