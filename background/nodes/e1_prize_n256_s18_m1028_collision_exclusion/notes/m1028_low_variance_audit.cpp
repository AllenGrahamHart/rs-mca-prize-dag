#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>

namespace {

constexpr int kPrime = 257;
constexpr int kRoot = 3;
constexpr int kShards = 32;

int Power(int base, int exponent) {
  int64_t result = 1;
  int64_t value = base;
  while (exponent) {
    if (exponent & 1) result = result * value % kPrime;
    value = value * value % kPrime;
    exponent >>= 1;
  }
  return static_cast<int>(result);
}

int Energy(const std::array<int, 6>& positions,
           const std::array<int, 6>& coefficients) {
  std::array<int, 128> correlation{};
  for (int left = 0; left < 6; ++left) {
    for (int right = 0; right < 6; ++right) {
      if (left == right) continue;
      const int difference = positions[left] - positions[right];
      if (difference >= 0) {
        correlation[difference] += coefficients[left] * coefficients[right];
      } else {
        correlation[128 + difference] -= coefficients[left] * coefficients[right];
      }
    }
  }
  if (correlation[0] != 0 || correlation[64] != 0) return -1;
  int energy = 0;
  for (int difference = 1; difference < 64; ++difference) {
    if (correlation[128 - difference] != -correlation[difference]) return -1;
    energy += correlation[difference] * correlation[difference];
  }
  return energy;
}

bool DivisibleBy257(const std::array<int, 6>& positions,
                    const std::array<int, 6>& coefficients) {
  for (int exponent = 1; exponent < 256; exponent += 2) {
    const int root = Power(kRoot, exponent);
    int root_power = 1;
    std::array<int, 128> powers{};
    for (int index = 0; index < 128; ++index) {
      powers[index] = root_power;
      root_power = root_power * root % kPrime;
    }
    int value = 0;
    for (int index = 0; index < 6; ++index) {
      value += coefficients[index] * powers[positions[index]];
    }
    value %= kPrime;
    if (value < 0) value += kPrime;
    if (value == 0) return true;
  }
  return false;
}

bool Gate() {
  if (Power(kRoot, 128) != -1 + kPrime || Power(kRoot, 64) == 1) return false;
  const std::array<int, 6> positions = {0, 2, 64, 66, 96, 98};
  const std::array<int, 6> coefficients = {1, 1, -2, -2, 2, -2};
  return Energy(positions, coefficients) == 9 &&
         !DivisibleBy257(positions, coefficients);
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M1028_LOW_VARIANCE_AUDIT_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int available_count = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 2) available[available_count++] = position;
  }

  uint64_t global_combination = 0;
  uint64_t combinations = 0;
  uint64_t signed_vectors = 0;
  uint64_t energy5 = 0;
  uint64_t energy9 = 0;
  uint64_t energy5_div257 = 0;
  uint64_t energy9_div257 = 0;
  const auto started = std::chrono::steady_clock::now();

  for (int first = 0; first < 123; ++first) {
    for (int second = first + 1; second < 124; ++second) {
      for (int third = second + 1; third < 125; ++third) {
        for (int fourth = third + 1; fourth < 126; ++fourth) {
          const bool assigned = global_combination % kShards ==
                                static_cast<uint64_t>(shard);
          ++global_combination;
          if (!assigned) continue;
          ++combinations;
          const std::array<int, 6> positions = {
              0, 2, available[first], available[second], available[third],
              available[fourth]};
          for (int singleton_sign : {-1, 1}) {
            for (int sign_mask = 0; sign_mask < 16; ++sign_mask) {
              ++signed_vectors;
              const std::array<int, 6> coefficients = {
                  1, singleton_sign,
                  (sign_mask & 1) ? 2 : -2,
                  (sign_mask & 2) ? 2 : -2,
                  (sign_mask & 4) ? 2 : -2,
                  (sign_mask & 8) ? 2 : -2};
              const int energy = Energy(positions, coefficients);
              if (energy != 5 && energy != 9) continue;
              const bool divisible = DivisibleBy257(positions, coefficients);
              if (energy == 5) {
                ++energy5;
                if (divisible) ++energy5_div257;
              } else {
                ++energy9;
                if (divisible) ++energy9_div257;
              }
            }
          }
        }
      }
    }
  }
  const double seconds = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - started).count();
  std::cout << "{\"complete\":true,\"shard\":" << shard
            << ",\"global_combination_count\":" << global_combination
            << ",\"combination_count\":" << combinations
            << ",\"signed_vector_count\":" << signed_vectors
            << ",\"energy5_count\":" << energy5
            << ",\"energy9_count\":" << energy9
            << ",\"energy5_div257_count\":" << energy5_div257
            << ",\"energy9_div257_count\":" << energy9_div257
            << ",\"wall_seconds\":" << seconds << "}\n";
  return 0;
}
