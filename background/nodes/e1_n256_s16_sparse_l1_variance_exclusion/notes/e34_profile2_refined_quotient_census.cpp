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
  std::array<int, kCategories> ones{};
  std::array<int, kCategories> twos{};
  std::array<int, 4> components{};
};

struct Search {
  int order = 128;
  int shard = 0;
  int shards = 1;
  std::array<int, kCategories> capacity{};
  std::array<int, kCategories> total{};
  std::array<int, kCategories> two{};
  std::uint64_t outer_index = 0;
  std::uint64_t tested = 0;
  Candidate best;
  Candidate best_refined;
  Candidate best_inside_four;
  Candidate best_outside_four;

  using Residues = std::array<int, kModulus>;

  static Residues residues(const std::array<int, kCategories>& counts) {
    Residues result{};
    result[0] = 2 * counts[0];
    result[8] = 2 * counts[8];
    for (int residue = 1; residue < 8; ++residue) {
      result[residue] = counts[residue];
      result[16 - residue] = counts[residue];
    }
    return result;
  }

  static int directed_bound(const Residues& left, const Residues& right,
                            const Residues& target, int left_total,
                            int right_total) {
    int answer = 0;
    for (int target_residue = 0; target_residue < 16; ++target_residue) {
      int pairs = 0;
      int per_target = 0;
      for (int left_residue = 0; left_residue < 16; ++left_residue) {
        const int right_residue =
            (32 - target_residue - left_residue) % 16;
        pairs += left[left_residue] * right[right_residue];
        per_target += std::min(left[left_residue], right[right_residue]);
      }
      if (target_residue == 0) pairs -= std::min(left_total, right_total);
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

  void retain(Candidate& candidate, int value,
              const std::array<int, 4>& components) {
    if (value <= candidate.value) return;
    candidate.value = value;
    candidate.components = components;
    for (int index = 0; index < kCategories; ++index) {
      candidate.twos[index] = two[index];
      candidate.ones[index] = total[index] - two[index];
    }
  }

  void evaluate(const Residues& outer, int aaa) {
    const auto inner = residues(two);
    const int aab = std::min(
        directed_bound(outer, outer, inner, 20, 20),
        directed_bound(outer, inner, outer, 20, 16));
    const int abb = std::min(
        directed_bound(outer, inner, inner, 20, 16),
        directed_bound(inner, inner, outer, 16, 16));
    const int bbb = triple_bound(inner, inner, inner, 16, 16, 16);
    const std::array<int, 4> components{{aaa, aab, abb, bbb}};
    const int objective = aaa + 3 * aab + 3 * abb + bbb;
    const bool inner_even = !(two[1] || two[3] || two[5] || two[7]);
    const bool inner_four =
        !(two[1] || two[2] || two[3] || two[5] || two[6] || two[7]);
    const int refined = objective - bbb +
                        ((order == 64 || inner_even) ? std::min(bbb, 174)
                                                     : bbb);
    ++tested;
    retain(best, objective, components);
    retain(best_refined, refined, components);
    if (inner_four) {
      retain(best_inside_four, refined, components);
    } else {
      retain(best_outside_four, refined, components);
    }
  }

  void enumerate_two(int index, int left, const Residues& outer, int aaa) {
    if (index == kCategories) {
      if (left == 0) evaluate(outer, aaa);
      return;
    }
    int later = 0;
    for (int next = index + 1; next < kCategories; ++next) {
      later += total[next];
    }
    const int minimum = std::max(0, left - later);
    const int maximum = std::min(total[index], left);
    for (int value = minimum; value <= maximum; ++value) {
      two[index] = value;
      enumerate_two(index + 1, left - value, outer, aaa);
    }
  }

  void enumerate_outer(int index, int left) {
    if (index == kCategories) {
      if (left != 0 || !(total[1] || total[3] || total[5] || total[7])) return;
      const std::uint64_t index_here = outer_index++;
      if (index_here % shards != static_cast<std::uint64_t>(shard)) return;
      const auto outer_residues = residues(total);
      const int aaa = triple_bound(outer_residues, outer_residues,
                                   outer_residues, 20, 20, 20);
      enumerate_two(0, 8, outer_residues, aaa);
      return;
    }
    int later = 0;
    for (int next = index + 1; next < kCategories; ++next) {
      later += capacity[next];
    }
    const int minimum = std::max(0, left - later);
    const int maximum = std::min(capacity[index], left);
    for (int value = minimum; value <= maximum; ++value) {
      total[index] = value;
      enumerate_outer(index + 1, left - value);
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
              << ",\"ones\":";
    print_array(candidate.ones);
    std::cout << ",\"twos\":";
    print_array(candidate.twos);
    std::cout << ",\"components\":[" << candidate.components[0] << ','
              << candidate.components[1] << ',' << candidate.components[2]
              << ',' << candidate.components[3] << "]}";
  }

  void run() {
    enumerate_outer(0, 10);
    std::cout << "{\"complete\":true,\"order\":" << order
              << ",\"shard\":" << shard << ",\"shards\":" << shards
              << ",\"tested\":" << tested;
    print_candidate("best", best);
    print_candidate("best_refined", best_refined);
    print_candidate("best_inside_four", best_inside_four);
    print_candidate("best_outside_four", best_outside_four);
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
