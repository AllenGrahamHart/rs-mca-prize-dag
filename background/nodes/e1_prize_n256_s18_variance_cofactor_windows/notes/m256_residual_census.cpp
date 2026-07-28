#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <tuple>
#include <utility>
#include <vector>

namespace {

constexpr int kShards = 32;
constexpr std::array<int, 9> kEnergies = {5, 9, 13, 17, 21, 25, 29, 33, 37};

struct Witness {
  std::array<int, 6> positions{};
  std::array<int, 6> coefficients{};
  int energy = 0;
};

int EnergyIndex(int energy) {
  for (int index = 0; index < 9; ++index) {
    if (kEnergies[index] == energy) return index;
  }
  return -1;
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
  struct Job { int first; int second; uint64_t weight; };
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

bool Gate() {
  const std::array<int, 6> positions = {0, 8, 32, 64, 96, 127};
  const std::array<int, 6> coefficients = {1, 1, 2, -2, 2, -2};
  std::array<int, 64> values{};
  std::array<int, 64> marks{};
  std::array<int, 15> touched{};
  int touched_count = 0;
  for (int left = 0; left < 6; ++left) {
    for (int right = left + 1; right < 6; ++right) {
      AddPair(positions[left], coefficients[left], positions[right],
              coefficients[right], values, marks, 1, touched, touched_count);
    }
  }
  int energy = 0;
  for (int index = 0; index < touched_count; ++index) {
    energy += values[touched[index]] * values[touched[index]];
  }
  return energy == 133;
}

void PrintWitness(const Witness& witness) {
  std::cout << "{\"positions\":[";
  for (int index = 0; index < 6; ++index) {
    if (index) std::cout << ',';
    std::cout << witness.positions[index];
  }
  std::cout << "],\"coefficients\":[";
  for (int index = 0; index < 6; ++index) {
    if (index) std::cout << ',';
    std::cout << witness.coefficients[index];
  }
  std::cout << "],\"energy\":" << witness.energy << '}';
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) return 2;
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M256_RESIDUAL_CENSUS_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) return 2;
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int cursor = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 8) available[cursor++] = position;
  }
  const auto assignments = BuildAssignments();
  uint64_t combinations = 0;
  uint64_t signed_vectors = 0;
  std::array<uint64_t, 9> energy_counts{};
  std::vector<Witness> witnesses;
  std::array<int, 64> values{};
  std::array<int, 64> marks{};
  int epoch = 0;
  const auto started = std::chrono::steady_clock::now();

  for (const auto& [first, second] : assignments[shard]) {
    for (int third = second + 1; third < 126; ++third) {
      for (int fourth = third + 1; fourth < 126; ++fourth) {
        ++combinations;
        const std::array<int, 6> positions = {
            0, 8, available[first], available[second], available[third],
            available[fourth]};
        for (int mask = 0; mask < 32; ++mask) {
          ++signed_vectors;
          const std::array<int, 6> coefficients = {
              1, (mask & 1) ? 1 : -1,
              (mask & 2) ? 2 : -2, (mask & 4) ? 2 : -2,
              (mask & 8) ? 2 : -2, (mask & 16) ? 2 : -2};
          ++epoch;
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
          const int energy_index = EnergyIndex(energy);
          if (energy_index < 0) continue;
          ++energy_counts[energy_index];
          witnesses.push_back({positions, coefficients, energy});
        }
      }
    }
  }
  const double seconds = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - started).count();
  std::cout << "{\"complete\":true,\"shard\":" << shard
            << ",\"combination_count\":" << combinations
            << ",\"signed_vector_count\":" << signed_vectors
            << ",\"energy_counts\":[";
  for (int index = 0; index < 9; ++index) {
    if (index) std::cout << ',';
    std::cout << energy_counts[index];
  }
  std::cout << "],\"wall_seconds\":" << seconds << ",\"witnesses\":[";
  for (size_t index = 0; index < witnesses.size(); ++index) {
    if (index) std::cout << ',';
    PrintWitness(witnesses[index]);
  }
  std::cout << "]}\n";
  return 0;
}
