#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

namespace {

constexpr std::array<std::array<int, 4>, 3> kLight{{
    {{0, 1, 6, 8}},
    {{0, 2, 12, 16}},
    {{0, 4, 24, 32}},
}};
constexpr std::array<std::array<int, 2>, 3> kThrees{{
    {{1, 2}}, {{2, 4}}, {{4, 8}},
}};
constexpr std::array<std::array<int, 2>, 3> kTwos{{
    {{3, 4}}, {{6, 8}}, {{12, 16}},
}};
constexpr std::array<std::array<int, 4>, 3> kOnes{{
    {{5, 6, 7, 8}}, {{10, 12, 14, 16}}, {{20, 24, 28, 32}},
}};

bool matches(int template_index, const std::array<int, 128>& product) {
  std::array<int, 64> expected{};
  for (int distance : kOnes[template_index]) expected[distance] = 1;
  for (int distance : kTwos[template_index]) expected[distance] = 2;
  for (int distance : kThrees[template_index]) expected[distance] = 3;
  for (int distance = 1; distance < 64; ++distance) {
    if (std::abs(product[distance]) != expected[distance]) return false;
  }
  return true;
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
  if (argc != 2) return 2;
  const int template_index = std::atoi(argv[1]);
  if (template_index < 0 || template_index >= 3) return 2;
  const auto& light = kLight[template_index];
  std::array<bool, 128> occupied{};
  for (int position : light) occupied[position] = true;
  std::vector<int> allowed;
  for (int position = 0; position < 128; ++position) {
    if (!occupied[position]) allowed.push_back(position);
  }

  std::uint64_t supports = 0;
  std::uint64_t vectors = 0;
  std::uint64_t count = 0;
  std::uint64_t full_conductor = 0;
  std::array<int, 7> witness_positions{};
  std::array<int, 7> witness_coefficients{};
  std::vector<std::pair<std::array<int, 7>, std::array<int, 7>>> vectors_found;
  for (int first = 0; first < static_cast<int>(allowed.size()) - 2; ++first) {
    for (int second = first + 1; second < static_cast<int>(allowed.size()) - 1; ++second) {
      for (int third = second + 1; third < static_cast<int>(allowed.size()); ++third) {
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
              const int reverse_exponent = positions[right] == 0 ? 0 : 128 - positions[right];
              const int reverse_coefficient =
                  positions[right] == 0 ? coefficients[right] : -coefficients[right];
              const int exponent = positions[left] + reverse_exponent;
              product[exponent % 128] += (exponent >= 128 ? -1 : 1) *
                  coefficients[left] * reverse_coefficient;
            }
          }
          if (product[0] != 16) return 3;
          for (int difference = 1; difference < 64; ++difference) {
            if (product[128 - difference] != -product[difference]) return 4;
          }
          if (!matches(template_index, product)) continue;
          ++count;
          full_conductor += conductor == 1;
          vectors_found.emplace_back(positions, coefficients);
          if (count == 1) {
            witness_positions = positions;
            witness_coefficients = coefficients;
          }
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"template\":" << template_index
            << ",\"light\":";
  print_array(light);
  std::cout << ",\"supports\":" << supports << ",\"vectors\":" << vectors
            << ",\"count\":" << count
            << ",\"full_conductor\":" << full_conductor
            << ",\"witness\":{\"positions\":";
  print_array(witness_positions);
  std::cout << ",\"coefficients\":";
  print_array(witness_coefficients);
  std::cout << "},\"matches\":[";
  for (std::size_t index = 0; index < vectors_found.size(); ++index) {
    if (index) std::cout << ',';
    std::cout << "{\"positions\":";
    print_array(vectors_found[index].first);
    std::cout << ",\"coefficients\":";
    print_array(vectors_found[index].second);
    std::cout << '}';
  }
  std::cout << "]}\n";
  return 0;
}
