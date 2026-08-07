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
constexpr std::array<int, 6> kEnergies = {5, 9, 13, 17, 21, 25};

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

int EnergyIndex(int energy) {
  for (int index = 0; index < 6; ++index) {
    if (kEnergies[index] == energy) return index;
  }
  return -1;
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
    int value = 0;
    for (int index = 0; index < 6; ++index) {
      value += coefficients[index] * Power(root, positions[index]);
    }
    value %= kPrime;
    if (value < 0) value += kPrime;
    if (value == 0) return true;
  }
  return false;
}

bool Gate() {
  if (Power(kRoot, 128) != 256 || Power(kRoot, 64) == 1) return false;
  const std::array<int, 6> positions = {0, 1, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  return Energy(positions, coefficients) == 89;
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M514_LOW_VARIANCE_AUDIT_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int available_count = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 1) available[available_count++] = position;
  }
  uint64_t global_combination = 0;
  uint64_t combinations = 0;
  uint64_t signed_vectors = 0;
  std::array<uint64_t, 6> energy_counts{};
  std::array<uint64_t, 6> divisible_counts{};
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
              0, 1, available[first], available[second], available[third],
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
              const int index = EnergyIndex(Energy(positions, coefficients));
              if (index < 0) continue;
              ++energy_counts[index];
              if (DivisibleBy257(positions, coefficients)) {
                ++divisible_counts[index];
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
            << ",\"energy_counts\":[";
  for (int index = 0; index < 6; ++index) {
    if (index) std::cout << ',';
    std::cout << energy_counts[index];
  }
  std::cout << "],\"div257_counts\":[";
  for (int index = 0; index < 6; ++index) {
    if (index) std::cout << ',';
    std::cout << divisible_counts[index];
  }
  std::cout << "],\"wall_seconds\":" << seconds << "}\n";
  return 0;
}
