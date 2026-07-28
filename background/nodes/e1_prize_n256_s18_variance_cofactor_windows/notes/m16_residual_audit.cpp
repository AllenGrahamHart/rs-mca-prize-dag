#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>

namespace {

constexpr int kShards = 32;
constexpr int kEnergyCount = 22;
constexpr int kL1Count = 42;

int EnergyIndex(int energy) {
  if (energy < 5 || energy > 89 || energy % 4 != 1) return -1;
  return (energy - 5) / 4;
}

std::pair<int, int> EnergyL1(const std::array<int, 6>& positions,
                             const std::array<int, 6>& coefficients) {
  std::array<int, 128> correlation{};
  for (int left = 0; left < 6; ++left) {
    for (int right = 0; right < 6; ++right) {
      if (left == right) continue;
      const int difference = positions[left] - positions[right];
      if (difference >= 0) {
        correlation[difference] += coefficients[left] * coefficients[right];
      } else {
        correlation[128 + difference] -=
            coefficients[left] * coefficients[right];
      }
    }
  }
  if (correlation[0] != 0 || correlation[64] != 0) return {-1, -1};
  int energy = 0;
  int l1 = 0;
  for (int difference = 1; difference < 64; ++difference) {
    if (correlation[128 - difference] != -correlation[difference]) {
      return {-1, -1};
    }
    energy += correlation[difference] * correlation[difference];
    l1 += std::abs(correlation[difference]);
  }
  return {energy, l1};
}

bool Gate() {
  const std::array<int, 6> positions = {0, 4, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  return EnergyL1(positions, coefficients) == std::pair<int, int>{133, 31};
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M16_RESIDUAL_AUDIT_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int available_count = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 4) available[available_count++] = position;
  }
  uint64_t global_combination = 0;
  uint64_t combinations = 0;
  uint64_t signed_vectors = 0;
  std::array<uint64_t, kEnergyCount> energy_counts{};
  std::array<std::array<uint64_t, kL1Count>, kEnergyCount> l1_counts{};
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
              0, 4, available[first], available[second], available[third],
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
              const auto [energy, l1] = EnergyL1(positions, coefficients);
              const int index = EnergyIndex(energy);
              if (index >= 0) {
                ++energy_counts[index];
                ++l1_counts[index][l1];
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
  for (int index = 0; index < kEnergyCount; ++index) {
    if (index) std::cout << ',';
    std::cout << energy_counts[index];
  }
  std::cout << "],\"l1_counts\":[";
  for (int energy_index = 0; energy_index < kEnergyCount; ++energy_index) {
    if (energy_index) std::cout << ',';
    std::cout << '[';
    for (int l1 = 0; l1 < kL1Count; ++l1) {
      if (l1) std::cout << ',';
      std::cout << l1_counts[energy_index][l1];
    }
    std::cout << ']';
  }
  std::cout << "],\"wall_seconds\":" << seconds << "}\n";
  return 0;
}
