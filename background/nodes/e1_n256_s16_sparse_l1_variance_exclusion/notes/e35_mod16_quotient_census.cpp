#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>

namespace {

constexpr int kModulus = 16;
constexpr int kCategories = 9;

struct Search {
  int profile = 0;
  int order = 128;
  int shard = 0;
  int shards = 1;
  int one_count = 3;
  int two_count = 8;
  int outer_total = 24;
  int inner_total = 16;
  std::array<int, kCategories> capacity{};
  std::array<int, kCategories> total{};
  std::array<int, kCategories> two{};
  std::array<int, kCategories> best_one{};
  std::array<int, kCategories> best_two{};
  std::array<int, 4> best_components{};
  std::array<int, kCategories> best_not4_one{};
  std::array<int, kCategories> best_not4_two{};
  std::array<int, 4> best_not4_components{};
  std::array<int, kCategories> best_inner4_one{};
  std::array<int, kCategories> best_inner4_two{};
  std::array<int, 4> best_inner4_components{};
  std::uint64_t outer_index = 0;
  std::uint64_t tested = 0;
  int best = -1;
  int best_not4 = -1;
  int best_inner4_refined = -1;

  static std::array<int, kModulus> residues(
      const std::array<int, kCategories>& counts) {
    std::array<int, kModulus> result{};
    result[0] = 2 * counts[0];
    result[8] = 2 * counts[8];
    for (int residue = 1; residue < 8; ++residue) {
      result[residue] = counts[residue];
      result[kModulus - residue] = counts[residue];
    }
    return result;
  }

  static int pair_bound(const std::array<int, kModulus>& left,
                        const std::array<int, kModulus>& right,
                        const std::array<int, kModulus>& target,
                        int left_total, int right_total) {
    int bound = 0;
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
      bound += std::min(pairs, target[target_residue] * per_target);
    }
    return bound;
  }

  void evaluate(const std::array<int, kModulus>& outer, int aaa) {
    const auto inner = residues(two);
    const int aab =
        std::min(pair_bound(outer, outer, inner, outer_total, outer_total),
                 pair_bound(outer, inner, outer, outer_total, inner_total));
    const int abb =
        std::min(pair_bound(outer, inner, inner, outer_total, inner_total),
                 pair_bound(inner, inner, outer, inner_total, inner_total));
    const int bbb = pair_bound(inner, inner, inner, inner_total, inner_total);
    const int objective = aaa + 3 * aab + 3 * abb + bbb;
    ++tested;
    const bool inner_reducible = inner_total &&
        (order == 64 || !(two[1] || two[3] || two[5] || two[7]));
    if (!inner_reducible && objective > best_not4) {
      best_not4 = objective;
      for (int index = 0; index < kCategories; ++index) {
        best_not4_two[index] = two[index];
        best_not4_one[index] = total[index] - two[index];
      }
      best_not4_components = {aaa, aab, abb, bbb};
    }
    if (inner_reducible) {
      const int refined = aaa + 3 * aab + 3 * abb + std::min(bbb, 174);
      if (refined > best_inner4_refined) {
        best_inner4_refined = refined;
        for (int index = 0; index < kCategories; ++index) {
          best_inner4_two[index] = two[index];
          best_inner4_one[index] = total[index] - two[index];
        }
        best_inner4_components = {aaa, aab, abb, bbb};
      }
    }
    if (objective > best) {
      best = objective;
      for (int index = 0; index < kCategories; ++index) {
        best_two[index] = two[index];
        best_one[index] = total[index] - two[index];
      }
      best_components = {aaa, aab, abb, bbb};
    }
  }

  void enumerate_two(int index, int remaining,
                     const std::array<int, kModulus>& outer, int aaa) {
    if (index == kCategories) {
      if (remaining == 0) evaluate(outer, aaa);
      return;
    }
    int later_capacity = 0;
    for (int later = index + 1; later < kCategories; ++later) {
      later_capacity += total[later];
    }
    const int minimum = std::max(0, remaining - later_capacity);
    const int maximum = std::min(total[index], remaining);
    for (int value = minimum; value <= maximum; ++value) {
      two[index] = value;
      enumerate_two(index + 1, remaining - value, outer, aaa);
    }
  }

  void enumerate_outer(int index, int remaining) {
    if (index == kCategories) {
      if (remaining != 0) return;
      if (!(total[1] || total[3] || total[5] || total[7])) return;
      const std::uint64_t index_here = outer_index++;
      if (index_here % shards != static_cast<std::uint64_t>(shard)) return;
      const auto outer = residues(total);
      const int aaa =
          pair_bound(outer, outer, outer, outer_total, outer_total);
      enumerate_two(0, two_count, outer, aaa);
      return;
    }
    int later_capacity = 0;
    for (int later = index + 1; later < kCategories; ++later) {
      later_capacity += capacity[later];
    }
    const int minimum = std::max(0, remaining - later_capacity);
    const int maximum = std::min(capacity[index], remaining);
    for (int value = minimum; value <= maximum; ++value) {
      total[index] = value;
      enumerate_outer(index + 1, remaining - value);
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
    enumerate_outer(0, one_count + two_count);
    std::cout << "{\"complete\":true,\"profile\":" << profile
              << ",\"order\":" << order << ",\"shard\":" << shard
              << ",\"shards\":" << shards << ",\"tested\":" << tested
              << ",\"best\":" << best << ",\"ones\":";
    print_array(best_one);
    std::cout << ",\"twos\":";
    print_array(best_two);
    std::cout << ",\"components\":[" << best_components[0] << ','
              << best_components[1] << ',' << best_components[2] << ','
              << best_components[3] << "],\"best_outside_inner2\":"
              << best_not4 << ",\"outside_inner2_ones\":";
    print_array(best_not4_one);
    std::cout << ",\"outside_inner2_twos\":";
    print_array(best_not4_two);
    std::cout << ",\"outside_inner2_components\":["
              << best_not4_components[0] << ','
              << best_not4_components[1] << ',' << best_not4_components[2]
              << ',' << best_not4_components[3]
              << "],\"best_inner2_refined\":" << best_inner4_refined
              << ",\"inner2_ones\":";
    print_array(best_inner4_one);
    std::cout << ",\"inner2_twos\":";
    print_array(best_inner4_two);
    std::cout << ",\"inner2_components\":[" << best_inner4_components[0]
              << ',' << best_inner4_components[1] << ','
              << best_inner4_components[2] << ',' << best_inner4_components[3]
              << "]}\n";
  }
};

}  // namespace

int main(int argc, char** argv) {
  if (argc != 5) return 2;
  Search search;
  search.profile = std::atoi(argv[1]);
  search.order = std::atoi(argv[2]);
  search.shard = std::atoi(argv[3]);
  search.shards = std::atoi(argv[4]);
  if (search.profile == 0) {
    search.one_count = 3;
    search.two_count = 8;
  } else if (search.profile == 1) {
    search.one_count = 12;
    search.two_count = 0;
  } else {
    return 2;
  }
  search.outer_total = 2 * (search.one_count + search.two_count);
  search.inner_total = 2 * search.two_count;
  if (search.order == 128) {
    search.capacity = {3, 8, 8, 8, 8, 8, 8, 8, 4};
  } else if (search.order == 64) {
    search.capacity = {1, 4, 4, 4, 4, 4, 4, 4, 2};
  } else {
    return 2;
  }
  if (search.shards <= 0 || search.shard < 0 || search.shard >= search.shards) {
    return 2;
  }
  search.run();
  return 0;
}
