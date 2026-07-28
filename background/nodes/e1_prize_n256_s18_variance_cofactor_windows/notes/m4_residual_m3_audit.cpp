#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace {

constexpr int kShards = 32;
constexpr int kEnergyCount = 20;

int EnergyIndex(int energy) {
  if (energy < 5 || energy > 81 || energy % 4 != 1) return -1;
  return (energy - 5) / 4;
}

void AddPair(int left_position, int left_coefficient, int right_position,
             int right_coefficient, std::array<int, 64>& values,
             std::array<int, 64>& marks, int epoch,
             std::array<int, 15>& touched, int& touched_count) {
  int difference = std::abs(right_position - left_position);
  if (difference == 64) return;
  int sign = 1;
  if (difference > 64) {
    difference = 128 - difference;
    sign = -1;
  }
  if (marks[difference] != epoch) {
    marks[difference] = epoch;
    values[difference] = 0;
    touched[touched_count++] = difference;
  }
  values[difference] += sign * left_coefficient * right_coefficient;
}

std::vector<std::vector<std::pair<int, int>>> BuildAssignments() {
  struct Job {
    int first;
    int second;
    uint64_t weight;
  };
  std::vector<Job> jobs;
  for (int first = 0; first < 126; ++first) {
    for (int second = first + 1; second < 126; ++second) {
      const uint64_t remaining = 125 - second;
      const uint64_t combinations = remaining * (remaining - 1) / 2;
      if (combinations) jobs.push_back({first, second, 32 * combinations});
    }
  }
  std::sort(jobs.begin(), jobs.end(), [](const Job& left, const Job& right) {
    return std::tie(left.weight, left.first, left.second) >
           std::tie(right.weight, right.first, right.second);
  });
  std::vector<uint64_t> loads(kShards, 0);
  std::vector<std::vector<std::pair<int, int>>> assignments(kShards);
  for (const Job& job : jobs) {
    const int shard = static_cast<int>(
        std::min_element(loads.begin(), loads.end()) - loads.begin());
    assignments[shard].push_back({job.first, job.second});
    loads[shard] += job.weight;
  }
  return assignments;
}

int EnergyCorrelation(const std::array<int, 6>& positions,
                      const std::array<int, 6>& coefficients,
                      std::array<int, 64>& values,
                      std::array<int, 64>& marks, int epoch,
                      std::array<int, 128>& correlation) {
  std::array<int, 15> touched{};
  int touched_count = 0;
  for (int left = 0; left < 6; ++left) {
    for (int right = left + 1; right < 6; ++right) {
      AddPair(positions[left], coefficients[left], positions[right],
              coefficients[right], values, marks, epoch, touched,
              touched_count);
    }
  }
  correlation.fill(0);
  int energy = 0;
  for (int index = 0; index < touched_count; ++index) {
    const int difference = touched[index];
    const int value = values[difference];
    energy += value * value;
    correlation[difference] = value;
    correlation[128 - difference] = -value;
  }
  return energy;
}

int ThirdMoment(const std::array<int, 128>& correlation) {
  std::array<int, 30> support{};
  int support_size = 0;
  for (int index = 0; index < 128; ++index) {
    if (correlation[index] != 0) support[support_size++] = index;
  }
  std::array<int, 128> square{};
  for (int left_index = 0; left_index < support_size; ++left_index) {
    const int left = support[left_index];
    for (int right_index = 0; right_index < support_size; ++right_index) {
      const int right = support[right_index];
      const int exponent = left + right;
      const int product = correlation[left] * correlation[right];
      if (exponent >= 128) {
        square[exponent - 128] -= product;
      } else {
        square[exponent] += product;
      }
    }
  }
  int moment = 0;
  for (int exponent = 1; exponent < 128; ++exponent) {
    moment -= square[exponent] * correlation[128 - exponent];
  }
  return moment;
}

bool Gate() {
  const std::array<int, 6> positions = {0, 2, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  std::array<int, 64> values{};
  std::array<int, 64> marks{};
  std::array<int, 128> correlation{};
  return EnergyCorrelation(positions, coefficients, values, marks, 1,
                           correlation) == 133 &&
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
    std::cout << "M4_RESIDUAL_M3_AUDIT_GATE_PASS\n";
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
  const auto assignments = BuildAssignments();
  std::array<uint64_t, kEnergyCount> counts{};
  std::array<int, kEnergyCount> minima{};
  std::array<int, kEnergyCount> maxima{};
  std::array<std::array<int, 6>, kEnergyCount> maximum_positions{};
  std::array<std::array<int, 6>, kEnergyCount> maximum_coefficients{};
  minima.fill(std::numeric_limits<int>::max());
  maxima.fill(std::numeric_limits<int>::min());
  std::array<int, 64> values{};
  std::array<int, 64> marks{};
  int epoch = 0;
  const auto started = std::chrono::steady_clock::now();
  for (const auto& [first, second] : assignments[shard]) {
    for (int third = second + 1; third < 126; ++third) {
      for (int fourth = third + 1; fourth < 126; ++fourth) {
        const std::array<int, 6> positions = {
            0, 2, available[first], available[second], available[third],
            available[fourth]};
        for (int mask = 0; mask < 32; ++mask) {
          const std::array<int, 6> coefficients = {
              1, (mask & 1) ? 1 : -1,
              (mask & 2) ? 2 : -2, (mask & 4) ? 2 : -2,
              (mask & 8) ? 2 : -2, (mask & 16) ? 2 : -2};
          std::array<int, 128> correlation{};
          const int index = EnergyIndex(EnergyCorrelation(
              positions, coefficients, values, marks, ++epoch, correlation));
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
  const double seconds = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - started).count();
  std::cout << "{\"complete\":true,\"shard\":" << shard << ",\"rows\":[";
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
