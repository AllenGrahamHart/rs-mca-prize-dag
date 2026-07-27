#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>

namespace {

using Light = std::array<int, 4>;

struct Witness {
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
  int m3 = -1;
};

int circular_distance(int left, int right) {
  int difference = std::abs(left - right);
  return std::min(difference, 128 - difference);
}

Light canonical_light(const Light& light) {
  Light best{{128, 128, 128, 128}};
  for (int unit = 1; unit < 128; unit += 2) {
    for (int translation : {0, 64}) {
      Light transformed{};
      for (int index = 0; index < 4; ++index) {
        transformed[index] = (unit * light[index] + translation) % 128;
      }
      std::sort(transformed.begin(), transformed.end());
      best = std::min(best, transformed);
    }
  }
  return best;
}

std::vector<Light> light_templates() {
  std::set<Light> representatives;
  for (int x = 1; x < 127; ++x) {
    if (x == 64) continue;
    for (int y = x + 1; y < 128; ++y) {
      if (y == 64) continue;
      const Light light{{0, 64, x, y}};
      int diameters = 0;
      std::set<int> non_diameter_classes;
      for (int left = 0; left < 4; ++left) {
        for (int right = left + 1; right < 4; ++right) {
          const int distance = circular_distance(light[left], light[right]);
          if (distance == 64) {
            ++diameters;
          } else {
            non_diameter_classes.insert(distance);
          }
        }
      }
      if (diameters == 1 && non_diameter_classes.size() == 5) {
        representatives.insert(canonical_light(light));
      }
    }
  }
  return {representatives.begin(), representatives.end()};
}

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
  std::array<int, 128> weight{};
  std::vector<int> support;
  for (int difference = 1; difference < 64; ++difference) {
    const int magnitude = std::abs(half[difference]);
    if (!magnitude) continue;
    weight[difference] = magnitude;
    weight[128 - difference] = magnitude;
    support.push_back(difference);
    support.push_back(128 - difference);
  }
  int answer = 0;
  for (int left : support) {
    for (int right : support) {
      answer += weight[left] * weight[right] *
                weight[(256 - left - right) % 128];
    }
  }
  return answer;
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 2) return 2;
  const int template_index = std::atoi(argv[1]);
  const auto templates = light_templates();
  if (templates.size() != 100 || template_index < 0 ||
      template_index >= static_cast<int>(templates.size())) {
    return 2;
  }

  const auto light = templates[template_index];
  std::array<bool, 128> occupied{};
  for (int position : light) occupied[position] = true;
  std::vector<int> allowed;
  for (int position = 0; position < 128; ++position) {
    if (!occupied[position]) allowed.push_back(position);
  }

  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::uint64_t profile_57 = 0;
  std::uint64_t full_conductor = 0;
  int maximum_m3 = -1;
  int maximum_full_conductor_m3 = -1;
  Witness witness;
  Witness full_conductor_witness;

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

          int ones = 0;
          int twos = 0;
          bool other = false;
          for (int difference = 1; difference < 64; ++difference) {
            const int magnitude = std::abs(half[difference]);
            ones += magnitude == 1;
            twos += magnitude == 2;
            other = other || magnitude > 2;
          }
          if (ones != 5 || twos != 7 || other) continue;
          ++profile_57;
          const int m3 = third_moment(half);
          if (m3 > maximum_m3) {
            maximum_m3 = m3;
            witness = {positions, coefficients, m3};
          }
          if (conductor == 1) {
            ++full_conductor;
            if (m3 > maximum_full_conductor_m3) {
              maximum_full_conductor_m3 = m3;
              full_conductor_witness = {positions, coefficients, m3};
            }
          }
        }
      }
    }
  }

  auto print_array = [](const auto& values) {
    std::cout << '[';
    for (std::size_t index = 0; index < values.size(); ++index) {
      if (index) std::cout << ',';
      std::cout << values[index];
    }
    std::cout << ']';
  };
  auto print_witness = [&](const Witness& value) {
    std::cout << "{\"positions\":";
    print_array(value.positions);
    std::cout << ",\"coefficients\":";
    print_array(value.coefficients);
    std::cout << ",\"m3\":" << value.m3 << '}';
  };

  std::cout << "{\"complete\":true,\"templates\":" << templates.size()
            << ",\"template\":" << template_index << ",\"light\":";
  print_array(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_57\":" << profile_57
            << ",\"full_conductor\":" << full_conductor
            << ",\"maximum_m3\":" << maximum_m3
            << ",\"maximum_full_conductor_m3\":"
            << maximum_full_conductor_m3 << ",\"witness\":";
  print_witness(witness);
  std::cout << ",\"full_conductor_witness\":";
  print_witness(full_conductor_witness);
  std::cout << "}\n";
  return 0;
}
