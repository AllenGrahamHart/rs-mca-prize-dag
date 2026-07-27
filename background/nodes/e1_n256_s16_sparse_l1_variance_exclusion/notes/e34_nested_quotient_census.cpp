#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>

namespace {

constexpr int kModulus = 16;
constexpr int kCategories = 9;
constexpr int kMaxLevels = 4;

struct Search {
  int profile = 0;
  int order = 128;
  int shard = 0;
  int shards = 1;
  int levels = 2;
  std::array<int, kMaxLevels> profile_counts{};
  std::array<int, kMaxLevels> layer_totals{};
  std::array<int, kCategories> capacity{};
  std::array<int, kCategories> outer{};
  std::array<std::array<int, kCategories>, kMaxLevels> exact{};
  std::array<int, kMaxLevels> remaining{};
  std::array<std::array<int, kCategories>, kMaxLevels> best_exact{};
  std::uint64_t outer_index = 0;
  std::uint64_t tested = 0;
  int best = -1;

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
                            const Residues& target, int left_total,
                            int right_total) {
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
        pairs -= std::min(left_total, right_total);
      }
      answer += std::min(pairs, target[target_residue] * per_target);
    }
    return answer;
  }

  static int triple_bound(const Residues& first, const Residues& second,
                          const Residues& third, int first_total,
                          int second_total, int third_total) {
    return std::min(
        {directed_bound(first, second, third, first_total, second_total),
         directed_bound(first, third, second, first_total, third_total),
         directed_bound(second, third, first, second_total, third_total)});
  }

  void evaluate() {
    std::array<Residues, kMaxLevels> layers{};
    for (int level = 0; level < levels; ++level) {
      std::array<int, kCategories> nested{};
      for (int category = 0; category < kCategories; ++category) {
        for (int exact_level = level; exact_level < levels; ++exact_level) {
          nested[category] += exact[exact_level][category];
        }
      }
      layers[level] = residues(nested);
    }

    int objective = 0;
    for (int first = 0; first < levels; ++first) {
      for (int second = first; second < levels; ++second) {
        for (int third = second; third < levels; ++third) {
          int contribution = 0;
          // Nested symmetric two-point layers coincide and have no
          // zero-sum triple in a finite 2-group.
          if (!(layer_totals[first] == 2 && layer_totals[second] == 2 &&
                layer_totals[third] == 2)) {
            contribution = triple_bound(
                layers[first], layers[second], layers[third],
                layer_totals[first], layer_totals[second],
                layer_totals[third]);
          }
          const int multiplicity =
              first == third ? 1 : (first == second || second == third ? 3 : 6);
          objective += multiplicity * contribution;
        }
      }
    }

    ++tested;
    if (objective <= best) return;
    best = objective;
    best_exact = exact;
  }

  void enumerate_parts(int category, int level, int left) {
    if (level == levels - 1) {
      if (left > remaining[level]) return;
      exact[level][category] = left;
      remaining[level] -= left;
      enumerate_exact(category + 1);
      remaining[level] += left;
      return;
    }
    const int maximum = std::min(left, remaining[level]);
    for (int value = 0; value <= maximum; ++value) {
      exact[level][category] = value;
      remaining[level] -= value;
      enumerate_parts(category, level + 1, left - value);
      remaining[level] += value;
    }
  }

  void enumerate_exact(int category) {
    if (category == kCategories) {
      if (std::all_of(remaining.begin(), remaining.begin() + levels,
                      [](int value) { return value == 0; })) {
        evaluate();
      }
      return;
    }
    enumerate_parts(category, 0, outer[category]);
  }

  void enumerate_outer(int category, int left) {
    if (category == kCategories) {
      if (left != 0) return;
      if (!(outer[1] || outer[3] || outer[5] || outer[7])) return;
      const std::uint64_t index_here = outer_index++;
      if (index_here % shards != static_cast<std::uint64_t>(shard)) return;
      remaining = profile_counts;
      enumerate_exact(0);
      return;
    }
    int later_capacity = 0;
    for (int later = category + 1; later < kCategories; ++later) {
      later_capacity += capacity[later];
    }
    const int minimum = std::max(0, left - later_capacity);
    const int maximum = std::min(capacity[category], left);
    for (int value = minimum; value <= maximum; ++value) {
      outer[category] = value;
      enumerate_outer(category + 1, left - value);
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

  void run() {
    int outer_count = 0;
    for (int level = 0; level < levels; ++level) {
      outer_count += profile_counts[level];
      int nested_count = 0;
      for (int exact_level = level; exact_level < levels; ++exact_level) {
        nested_count += profile_counts[exact_level];
      }
      layer_totals[level] = 2 * nested_count;
    }
    enumerate_outer(0, outer_count);

    std::cout << "{\"complete\":true,\"profile\":" << profile
              << ",\"order\":" << order << ",\"shard\":" << shard
              << ",\"shards\":" << shards << ",\"tested\":" << tested
              << ",\"best\":" << best << ",\"profile_counts\":[";
    for (int level = 0; level < levels; ++level) {
      if (level) std::cout << ',';
      std::cout << profile_counts[level];
    }
    std::cout << "],\"exact\":[";
    for (int level = 0; level < levels; ++level) {
      if (level) std::cout << ',';
      print_array(best_exact[level]);
    }
    std::cout << "]}\n";
  }
};

}  // namespace

int main(int argc, char** argv) {
  if (argc != 5) {
    std::cerr << "usage: census PROFILE ORDER SHARD SHARDS\n";
    return 2;
  }
  Search search;
  search.profile = std::atoi(argv[1]);
  search.order = std::atoi(argv[2]);
  search.shard = std::atoi(argv[3]);
  search.shards = std::atoi(argv[4]);
  constexpr std::array<std::array<int, kMaxLevels>, 6> profiles{{
      {{6, 7, 0, 0}},
      {{9, 4, 1, 0}},
      {{2, 8, 0, 0}},
      {{12, 1, 2, 0}},
      {{5, 5, 1, 0}},
      {{14, 1, 0, 1}},
  }};
  constexpr std::array<int, 6> profile_levels{{2, 3, 2, 3, 3, 4}};
  if (search.profile < 0 || search.profile >= static_cast<int>(profiles.size())) {
    return 2;
  }
  search.profile_counts = profiles[search.profile];
  search.levels = profile_levels[search.profile];
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
