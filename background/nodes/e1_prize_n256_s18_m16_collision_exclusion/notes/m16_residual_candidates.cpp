#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace {

constexpr int kShards = 32;

bool IsResidualEnergy(int energy) {
  return 5 <= energy && energy <= 53 && energy % 4 == 1;
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

int Energy(const std::array<int, 6>& positions,
           const std::array<int, 6>& coefficients,
           std::array<int, 64>& values, std::array<int, 64>& marks,
           int epoch) {
  std::array<int, 15> touched{};
  int touched_count = 0;
  for (int left = 0; left < 6; ++left) {
    for (int right = left + 1; right < 6; ++right) {
      AddPair(positions[left], coefficients[left], positions[right],
              coefficients[right], values, marks, epoch, touched,
              touched_count);
    }
  }
  int energy = 0;
  for (int index = 0; index < touched_count; ++index) {
    energy += values[touched[index]] * values[touched[index]];
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
  const std::array<int, 6> positions = {0, 4, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  std::array<int, 64> values{};
  std::array<int, 64> marks{};
  return Energy(positions, coefficients, values, marks, 1) == 133;
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M16_RESIDUAL_CANDIDATES_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int cursor = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 4) available[cursor++] = position;
  }
  const auto assignments = BuildAssignments();
  std::array<int, 64> values{};
  std::array<int, 64> marks{};
  int epoch = 0;
  for (const auto& [first, second] : assignments[shard]) {
    for (int third = second + 1; third < 126; ++third) {
      for (int fourth = third + 1; fourth < 126; ++fourth) {
        const std::array<int, 6> positions = {
            0, 4, available[first], available[second], available[third],
            available[fourth]};
        for (int mask = 0; mask < 32; ++mask) {
          const std::array<int, 6> coefficients = {
              1, (mask & 1) ? 1 : -1,
              (mask & 2) ? 2 : -2, (mask & 4) ? 2 : -2,
              (mask & 8) ? 2 : -2, (mask & 16) ? 2 : -2};
          const int energy = Energy(positions, coefficients, values, marks,
                                    ++epoch);
          if (IsResidualEnergy(energy)) Emit(energy, positions, coefficients);
        }
      }
    }
  }
  return 0;
}
