#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>

namespace {

constexpr int kShards = 32;
constexpr std::array<int, 9> kEnergies = {5, 9, 13, 17, 21, 25, 29, 33, 37};

int EnergyIndex(int energy) {
  for (int index = 0; index < 9; ++index) {
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

bool Gate() {
  const std::array<int, 6> positions = {0, 8, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  return Energy(positions, coefficients) == 133;
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M256_RESIDUAL_AUDIT_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int available_count = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 8) available[available_count++] = position;
  }
  uint64_t global_combination = 0;
  uint64_t combinations = 0;
  uint64_t signed_vectors = 0;
  std::array<uint64_t, 9> energy_counts{};
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
              0, 8, available[first], available[second], available[third],
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
              if (index >= 0) ++energy_counts[index];
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
  for (int index = 0; index < 9; ++index) {
    if (index) std::cout << ',';
    std::cout << energy_counts[index];
  }
  std::cout << "],\"wall_seconds\":" << seconds << "}\n";
  return 0;
}
