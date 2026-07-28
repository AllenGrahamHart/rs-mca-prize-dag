#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace {

constexpr int kPrime = 257;
constexpr int kRoot = 3;
constexpr int kShards = 32;

struct Witness {
  std::array<int, 6> positions{};
  std::array<int, 6> coefficients{};
  std::array<int, 3> autocorrelations{};
  int autocorrelation_count = 0;
  int energy = 0;
  int root_exponent = -1;
};

int ModPow(int base, int exponent) {
  int64_t answer = 1;
  int64_t power = base;
  while (exponent > 0) {
    if (exponent & 1) answer = answer * power % kPrime;
    power = power * power % kPrime;
    exponent >>= 1;
  }
  return static_cast<int>(answer);
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

int DividingRoot(const std::array<int, 6>& positions,
                 const std::array<int, 6>& coefficients,
                 const std::array<std::array<int, 128>, 128>& powers) {
  for (int row = 0; row < 128; ++row) {
    int value = 0;
    for (int index = 0; index < 6; ++index) {
      value += coefficients[index] * powers[row][positions[index]];
    }
    value %= kPrime;
    if (value < 0) value += kPrime;
    if (value == 0) return 2 * row + 1;
  }
  return -1;
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
      if (combinations != 0) jobs.push_back({first, second, 32 * combinations});
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
  if (ModPow(kRoot, 128) != 256 || ModPow(kRoot, 64) == 1) return false;
  const std::array<int, 6> positions = {0, 2, 64, 66, 96, 98};
  const std::array<int, 6> coefficients = {1, 1, -2, -2, 2, -2};
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
  std::vector<int> nonzero;
  for (int index = 0; index < touched_count; ++index) {
    const int value = values[touched[index]];
    energy += value * value;
    if (value != 0) nonzero.push_back(value);
  }
  std::sort(nonzero.begin(), nonzero.end());
  return energy == 9 && nonzero == std::vector<int>({-2, 1, 2});
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
  std::cout << "],\"autocorrelations\":[";
  for (int index = 0; index < witness.autocorrelation_count; ++index) {
    if (index) std::cout << ',';
    std::cout << witness.autocorrelations[index];
  }
  std::cout << "],\"energy\":" << witness.energy
            << ",\"root_exponent\":" << witness.root_exponent << '}';
}

}  // namespace

int main(int argc, char** argv) {
  if (!Gate()) {
    std::cerr << "gate failed\n";
    return 2;
  }
  if (argc == 2 && std::string(argv[1]) == "--gate") {
    std::cout << "M1028_LOW_VARIANCE_GATE_PASS\n";
    return 0;
  }
  if (argc != 2) {
    std::cerr << "usage: census SHARD\n";
    return 2;
  }
  const int shard = std::atoi(argv[1]);
  if (shard < 0 || shard >= kShards) return 2;

  std::array<int, 126> available{};
  int cursor = 0;
  for (int position = 0; position < 128; ++position) {
    if (position != 0 && position != 2) available[cursor++] = position;
  }
  const auto assignments = BuildAssignments();
  std::array<std::array<int, 128>, 128> powers{};
  for (int row = 0; row < 128; ++row) {
    const int root = ModPow(kRoot, 2 * row + 1);
    powers[row][0] = 1;
    for (int exponent = 1; exponent < 128; ++exponent) {
      powers[row][exponent] = powers[row][exponent - 1] * root % kPrime;
    }
  }

  uint64_t combinations = 0;
  uint64_t signed_vectors = 0;
  uint64_t energy5 = 0;
  uint64_t energy9 = 0;
  uint64_t energy5_div257 = 0;
  uint64_t energy9_div257 = 0;
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
            0, 2, available[first], available[second], available[third],
            available[fourth]};
        for (int mask = 0; mask < 32; ++mask) {
          ++signed_vectors;
          std::array<int, 6> coefficients = {
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
            const int value = values[touched[index]];
            energy += value * value;
          }
          if (energy != 5 && energy != 9) continue;
          const int root_exponent = DividingRoot(positions, coefficients, powers);
          if (energy == 5) {
            ++energy5;
            if (root_exponent >= 0) ++energy5_div257;
          } else {
            ++energy9;
            if (root_exponent >= 0) ++energy9_div257;
          }
          if (witnesses.size() < 12) {
            Witness witness;
            witness.positions = positions;
            witness.coefficients = coefficients;
            witness.energy = energy;
            witness.root_exponent = root_exponent;
            for (int index = 0; index < touched_count; ++index) {
              const int value = values[touched[index]];
              if (value != 0) {
                witness.autocorrelations[witness.autocorrelation_count++] = value;
              }
            }
            std::sort(witness.autocorrelations.begin(),
                      witness.autocorrelations.begin() + witness.autocorrelation_count);
            witnesses.push_back(witness);
          }
        }
      }
    }
  }
  const double seconds = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - started).count();
  std::cout << "{\"complete\":true,\"shard\":" << shard
            << ",\"combination_count\":" << combinations
            << ",\"signed_vector_count\":" << signed_vectors
            << ",\"energy5_count\":" << energy5
            << ",\"energy9_count\":" << energy9
            << ",\"energy5_div257_count\":" << energy5_div257
            << ",\"energy9_div257_count\":" << energy9_div257
            << ",\"wall_seconds\":" << seconds << ",\"witnesses\":[";
  for (size_t index = 0; index < witnesses.size(); ++index) {
    if (index) std::cout << ',';
    PrintWitness(witnesses[index]);
  }
  std::cout << "]}\n";
  return 0;
}
