#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <utility>

namespace {

constexpr int kShards = 32;
constexpr int kEnergyCount = 20;

int EnergyIndex(int energy) {
  if (energy < 5 || energy > 81 || energy % 4 != 1) return -1;
  return (energy - 5) / 4;
}

int Energy(const std::array<int, 6>& positions,
           const std::array<int, 6>& coefficients,
           std::array<int, 128>& correlation) {
  correlation.fill(0);
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

int ThirdMoment(const std::array<int, 128>& correlation) {
  std::array<int, 30> support{};
  int support_size = 0;
  for (int index = 0; index < 128; ++index) {
    if (correlation[index] != 0) support[support_size++] = index;
  }
  int moment = 0;
  for (int left_index = 0; left_index < support_size; ++left_index) {
    const int left = support[left_index];
    for (int right_index = 0; right_index < support_size; ++right_index) {
      const int right = support[right_index];
      const int third = (256 - left - right) % 128;
      if (correlation[third] == 0) continue;
      const int wraps = (left + right + third) / 128;
      const int sign = wraps % 2 == 0 ? 1 : -1;
      moment += sign * correlation[left] * correlation[right] *
                correlation[third];
    }
  }
  return moment;
}

bool Gate() {
  const std::array<int, 6> positions = {0, 2, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  std::array<int, 128> correlation{};
  return Energy(positions, coefficients, correlation) == 133 &&
         ThirdMoment(correlation) == 3624;
}

void PrintArray(const std::array<int, 6>& values) {
  std::cout << '[';
  for (int index = 0; index < 6; ++index) {
    if (index) std::cout << ',';
    std::cout << values[index];
  }
  std::cout << ']';
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M4_RESIDUAL_M3_FRONTIER_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int cursor = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 2) available[cursor++] = position;
  }
  uint64_t global_combination = 0;
  std::array<uint64_t, kEnergyCount> counts{};
  std::array<int, kEnergyCount> minima{};
  std::array<int, kEnergyCount> maxima{};
  std::array<std::array<int, 6>, kEnergyCount> maximum_positions{};
  std::array<std::array<int, 6>, kEnergyCount> maximum_coefficients{};
  minima.fill(std::numeric_limits<int>::max());
  maxima.fill(std::numeric_limits<int>::min());
  const auto started = std::chrono::steady_clock::now();
  for (int first = 0; first < 123; ++first) {
    for (int second = first + 1; second < 124; ++second) {
      for (int third = second + 1; third < 125; ++third) {
        for (int fourth = third + 1; fourth < 126; ++fourth) {
          const bool assigned = global_combination % kShards ==
                                static_cast<uint64_t>(shard);
          ++global_combination;
          if (!assigned) continue;
          const std::array<int, 6> positions = {
              0, 2, available[first], available[second], available[third],
              available[fourth]};
          for (int singleton_sign : {-1, 1}) {
            for (int mask = 0; mask < 16; ++mask) {
              const std::array<int, 6> coefficients = {
                  1, singleton_sign,
                  (mask & 1) ? 2 : -2, (mask & 2) ? 2 : -2,
                  (mask & 4) ? 2 : -2, (mask & 8) ? 2 : -2};
              std::array<int, 128> correlation{};
              const int index =
                  EnergyIndex(Energy(positions, coefficients, correlation));
              if (index < 0) continue;
              ++counts[index];
              const int moment = ThirdMoment(correlation);
              minima[index] = std::min(minima[index], moment);
              if (moment > maxima[index]) {
                maxima[index] = moment;
                maximum_positions[index] = positions;
                maximum_coefficients[index] = coefficients;
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
            << ",\"rows\":[";
  for (int index = 0; index < kEnergyCount; ++index) {
    if (index) std::cout << ',';
    std::cout << "{\"count\":" << counts[index]
              << ",\"minimum_m3\":" << minima[index]
              << ",\"maximum_m3\":" << maxima[index]
              << ",\"maximum_positions\":";
    PrintArray(maximum_positions[index]);
    std::cout << ",\"maximum_coefficients\":";
    PrintArray(maximum_coefficients[index]);
    std::cout << '}';
  }
  std::cout << "],\"wall_seconds\":" << seconds << "}\n";
  return 0;
}
