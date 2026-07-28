#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>

namespace {

constexpr int kShards = 32;

bool IsResidualEnergy(int energy) {
  return 5 <= energy && energy <= 49 && energy % 4 == 1;
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
        correlation[128 + difference] -=
            coefficients[left] * coefficients[right];
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

void Emit(int energy, const std::array<int, 6>& positions,
          const std::array<int, 6>& coefficients) {
  std::cout << energy;
  for (int position : positions) std::cout << '\t' << position;
  for (int coefficient : coefficients) std::cout << '\t' << coefficient;
  std::cout << '\n';
}

bool Gate() {
  const std::array<int, 6> positions = {0, 1, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  return Energy(positions, coefficients) == 89;
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M2_RESIDUAL_CANDIDATES_AUDIT_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int cursor = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 1) available[cursor++] = position;
  }
  uint64_t global_combination = 0;
  for (int first = 0; first < 123; ++first) {
    for (int second = first + 1; second < 124; ++second) {
      for (int third = second + 1; third < 125; ++third) {
        for (int fourth = third + 1; fourth < 126; ++fourth) {
          const bool assigned = global_combination % kShards ==
                                static_cast<uint64_t>(shard);
          ++global_combination;
          if (!assigned) continue;
          const std::array<int, 6> positions = {
              0, 1, available[first], available[second], available[third],
              available[fourth]};
          for (int singleton_sign : {-1, 1}) {
            for (int mask = 0; mask < 16; ++mask) {
              const std::array<int, 6> coefficients = {
                  1, singleton_sign,
                  (mask & 1) ? 2 : -2, (mask & 2) ? 2 : -2,
                  (mask & 4) ? 2 : -2, (mask & 8) ? 2 : -2};
              const int energy = Energy(positions, coefficients);
              if (IsResidualEnergy(energy)) {
                Emit(energy, positions, coefficients);
              }
            }
          }
        }
      }
    }
  }
  return 0;
}
