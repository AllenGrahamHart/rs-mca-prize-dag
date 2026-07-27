#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

namespace {

struct Witness {
  std::array<int, 7> positions{};
  std::array<int, 7> coefficients{};
  int m3 = -1;
};

struct Ledger {
  std::uint64_t count = 0;
  std::uint64_t full_conductor = 0;
  int maximum_m3 = -1;
  int maximum_full_conductor_m3 = -1;
  Witness witness;
  Witness full_conductor_witness;
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

void update(Ledger& ledger, const std::array<int, 7>& positions,
            const std::array<int, 7>& coefficients, int conductor,
            const std::array<int, 64>& half) {
  ++ledger.count;
  const int m3 = third_moment(half);
  if (m3 > ledger.maximum_m3) {
    ledger.maximum_m3 = m3;
    ledger.witness = {positions, coefficients, m3};
  }
  if (conductor == 1) {
    ++ledger.full_conductor;
    if (m3 > ledger.maximum_full_conductor_m3) {
      ledger.maximum_full_conductor_m3 = m3;
      ledger.full_conductor_witness = {positions, coefficients, m3};
    }
  }
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 6) return 2;
  const int template_index = std::atoi(argv[1]);
  const std::array<int, 4> light{{
      std::atoi(argv[2]), std::atoi(argv[3]),
      std::atoi(argv[4]), std::atoi(argv[5]),
  }};
  if (template_index < 0 || template_index >= 8) return 2;

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
  Ledger profile_37;
  Ledger profile_251;
  Ledger profile_132;

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
          int threes = 0;
          bool above_three = false;
          for (int difference = 1; difference < 64; ++difference) {
            const int magnitude = std::abs(half[difference]);
            ones += magnitude == 1;
            twos += magnitude == 2;
            threes += magnitude == 3;
            above_three = above_three || magnitude > 3;
          }
          if (!above_three && ones == 3 && twos == 7 && threes == 0) {
            update(profile_37, positions, coefficients, conductor, half);
          }
          if (!above_three && ones == 2 && twos == 5 && threes == 1) {
            update(profile_251, positions, coefficients, conductor, half);
          }
          if (!above_three && ones == 1 && twos == 3 && threes == 2) {
            update(profile_132, positions, coefficients, conductor, half);
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
  auto print_ledger = [&](const Ledger& ledger) {
    std::cout << "{\"count\":" << ledger.count
              << ",\"full_conductor\":" << ledger.full_conductor
              << ",\"maximum_m3\":" << ledger.maximum_m3
              << ",\"maximum_full_conductor_m3\":"
              << ledger.maximum_full_conductor_m3 << ",\"witness\":";
    print_witness(ledger.witness);
    std::cout << ",\"full_conductor_witness\":";
    print_witness(ledger.full_conductor_witness);
    std::cout << '}';
  };

  std::cout << "{\"complete\":true,\"template\":" << template_index
            << ",\"light\":";
  print_array(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"profile_37\":";
  print_ledger(profile_37);
  std::cout << ",\"profile_251\":";
  print_ledger(profile_251);
  std::cout << ",\"profile_132\":";
  print_ledger(profile_132);
  std::cout << "}\n";
  return 0;
}
