#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>

namespace {

struct Search {
  int shard = 0;
  int shards = 1;
  std::array<int, 8> b{};
  std::array<int, 2> best_u{};
  std::array<int, 8> best_b{};
  std::uint64_t b_index = 0;
  std::uint64_t tested = 0;
  int best = -1;

  int objective(int first_u, int second_u) const {
    std::array<int, 128> weight{};
    for (int value : b) {
      weight[value] = weight[128 - value] = 2;
    }
    for (int value : {first_u, second_u}) {
      weight[value] = weight[128 - value] = 1;
    }
    int answer = 0;
    for (int left = 0; left < 128; ++left) {
      if (!weight[left]) continue;
      for (int right = 0; right < 128; ++right) {
        if (!weight[right]) continue;
        const int target = (256 - left - right) % 128;
        answer += weight[left] * weight[right] * weight[target];
      }
    }
    return answer;
  }

  void evaluate_b() {
    const std::uint64_t index_here = b_index++;
    if (index_here % shards != static_cast<std::uint64_t>(shard)) return;
    std::array<bool, 64> in_b{};
    for (int value : b) in_b[value] = true;
    for (int first = 1; first < 64; ++first) {
      if (in_b[first]) continue;
      for (int second = first + 1; second < 64; ++second) {
        if (in_b[second] || (!(first % 2) && !(second % 2))) continue;
        ++tested;
        const int value = objective(first, second);
        if (value <= best) continue;
        best = value;
        best_b = b;
        best_u = {{first, second}};
      }
    }
  }

  void choose_b(int depth, int start) {
    if (depth == 8) {
      evaluate_b();
      return;
    }
    for (int value = start; value <= 60; value += 4) {
      const int remaining_values = (60 - value) / 4;
      if (remaining_values < 7 - depth) break;
      b[depth] = value;
      choose_b(depth + 1, value + 4);
    }
  }

  template <std::size_t Size>
  static void print_array(const std::array<int, Size>& values) {
    std::cout << '[';
    for (std::size_t index = 0; index < Size; ++index) {
      if (index) std::cout << ',';
      std::cout << values[index];
    }
    std::cout << ']';
  }

  void run() {
    choose_b(0, 4);
    std::cout << "{\"complete\":true,\"shard\":" << shard
              << ",\"shards\":" << shards << ",\"tested\":" << tested
              << ",\"best\":" << best << ",\"b\":";
    print_array(best_b);
    std::cout << ",\"u\":";
    print_array(best_u);
    std::cout << "}\n";
  }
};

}  // namespace

int main(int argc, char** argv) {
  if (argc != 3) return 2;
  Search search;
  search.shard = std::atoi(argv[1]);
  search.shards = std::atoi(argv[2]);
  if (search.shards <= 0 || search.shard < 0 || search.shard >= search.shards) {
    return 2;
  }
  search.run();
  return 0;
}
