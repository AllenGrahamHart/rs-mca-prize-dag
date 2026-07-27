#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>

namespace {

constexpr int kModulus = 16;
constexpr int kCategories = 9;

struct Candidate {
  int value = -1;
  std::array<int, kCategories> unit{};
  std::array<int, kCategories> double_support{};
  std::array<int, 3> components{};
};

struct Search {
  int order = 128;
  int shard = 0;
  int shards = 1;
  std::array<int, kCategories> capacity{};
  std::array<int, kCategories> unit{};
  std::array<int, kCategories> double_support{};
  std::uint64_t allocation_index = 0;
  std::uint64_t tested = 0;
  Candidate best;
  Candidate best_refined;
  Candidate best_double_even;
  Candidate best_double_odd;

  using Residues = std::array<int, kModulus>;

  static Residues residues(const std::array<int, kCategories>& counts) {
    Residues result{};
    result[0] = 2 * counts[0];
    result[8] = 2 * counts[8];
    for (int residue = 1; residue < 8; ++residue) {
      result[residue] = counts[residue];
      result[kModulus - residue] = counts[residue];
    }
    return result;
  }

  static int directed_bound(const Residues& left, const Residues& right,
                            const Residues& target, int inverse_overlap) {
    int answer = 0;
    for (int target_residue = 0; target_residue < kModulus;
         ++target_residue) {
      int pairs = 0;
      int per_target = 0;
      for (int left_residue = 0; left_residue < kModulus; ++left_residue) {
        const int right_residue =
            (2 * kModulus - target_residue - left_residue) % kModulus;
        pairs += left[left_residue] * right[right_residue];
        per_target += std::min(left[left_residue], right[right_residue]);
      }
      if (target_residue == 0) {
        pairs -= inverse_overlap;
      }
      answer += std::min(pairs, target[target_residue] * per_target);
    }
    return answer;
  }

  void retain(Candidate& candidate, int value,
              const std::array<int, 3>& components) {
    if (value <= candidate.value) return;
    candidate.value = value;
    candidate.unit = unit;
    candidate.double_support = double_support;
    candidate.components = components;
  }

  void evaluate() {
    const Residues b = residues(double_support);
    const Residues u = residues(unit);
    const int bbb = directed_bound(b, b, b, 16);
    const int bbu = std::min(directed_bound(b, b, u, 16),
                             directed_bound(b, u, b, 0));
    const int buu = std::min(directed_bound(b, u, u, 0),
                             directed_bound(u, u, b, 2));
    const std::array<int, 3> components{{bbb, bbu, buu}};
    const int objective = 8 * bbb + 12 * bbu + 6 * buu;
    const bool b_even = !(double_support[1] || double_support[3] ||
                          double_support[5] || double_support[7]);
    const int refined_bbb =
        (order == 64 || b_even) ? std::min(bbb, 174) : bbb;
    const int refined = 8 * refined_bbb + 12 * bbu + 6 * buu;

    ++tested;
    retain(best, objective, components);
    retain(best_refined, refined, components);
    retain(b_even ? best_double_even : best_double_odd, refined, components);
  }

  void enumerate_double(int category, int left) {
    if (category == kCategories) {
      if (left != 0) return;
      const bool outer_odd =
          unit[1] || unit[3] || unit[5] || unit[7] || double_support[1] ||
          double_support[3] || double_support[5] || double_support[7];
      if (!outer_odd) return;
      const std::uint64_t index_here = allocation_index++;
      if (index_here % shards != static_cast<std::uint64_t>(shard)) return;
      evaluate();
      return;
    }
    int later_capacity = 0;
    for (int later = category + 1; later < kCategories; ++later) {
      later_capacity += capacity[later] - unit[later];
    }
    const int available = capacity[category] - unit[category];
    const int minimum = std::max(0, left - later_capacity);
    const int maximum = std::min(available, left);
    for (int value = minimum; value <= maximum; ++value) {
      double_support[category] = value;
      enumerate_double(category + 1, left - value);
    }
  }

  void enumerate_unit(int category, int left) {
    if (category == kCategories) {
      if (left == 0) enumerate_double(0, 8);
      return;
    }
    const int maximum = std::min(capacity[category], left);
    for (int value = 0; value <= maximum; ++value) {
      unit[category] = value;
      enumerate_unit(category + 1, left - value);
    }
  }

  static void print_array(const std::array<int, kCategories>& values) {
    std::cout << '[';
    for (int index = 0; index < kCategories; ++index) {
      if (index) std::cout << ',';
      std::cout << values[index];
    }
    std::cout << ']';
  }

  static void print_candidate(const char* name, const Candidate& candidate) {
    std::cout << ",\"" << name << "\":{\"value\":" << candidate.value
              << ",\"unit\":";
    print_array(candidate.unit);
    std::cout << ",\"double_support\":";
    print_array(candidate.double_support);
    std::cout << ",\"components\":[" << candidate.components[0] << ','
              << candidate.components[1] << ',' << candidate.components[2]
              << "]}";
  }

  void run() {
    enumerate_unit(0, 1);
    std::cout << "{\"complete\":true,\"order\":" << order
              << ",\"shard\":" << shard << ",\"shards\":" << shards
              << ",\"tested\":" << tested;
    print_candidate("best", best);
    print_candidate("best_refined", best_refined);
    print_candidate("best_double_even", best_double_even);
    print_candidate("best_double_odd", best_double_odd);
    std::cout << "}\n";
  }
};

}  // namespace

int main(int argc, char** argv) {
  if (argc != 4) return 2;
  Search search;
  search.order = std::atoi(argv[1]);
  search.shard = std::atoi(argv[2]);
  search.shards = std::atoi(argv[3]);
  if (search.order == 128) {
    search.capacity = {{3, 8, 8, 8, 8, 8, 8, 8, 4}};
  } else if (search.order == 64) {
    search.capacity = {{1, 4, 4, 4, 4, 4, 4, 4, 2}};
  } else {
    return 2;
  }
  if (search.shards <= 0 || search.shard < 0 || search.shard >= search.shards) {
    return 2;
  }
  search.run();
  return 0;
}
