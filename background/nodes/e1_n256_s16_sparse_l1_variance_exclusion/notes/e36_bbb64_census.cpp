#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>

namespace {

struct Search {
  int shard = 0;
  int shards = 16;
  std::array<int, 8> chosen{};
  std::uint64_t processed = 0;
  int best = -1;
  std::array<int, 8> best_representatives{};

  int schur_count() const {
    std::array<bool, 64> member{};
    std::array<int, 16> values{};
    int used = 0;
    for (int representative : chosen) {
      member[representative] = true;
      member[64 - representative] = true;
      values[used++] = representative;
      values[used++] = 64 - representative;
    }
    int count = 0;
    for (int left : values) {
      for (int right : values) {
        count += member[(128 - left - right) % 64];
      }
    }
    return count;
  }

  void enumerate(int index, int next) {
    if (index == 8) {
      const int value = schur_count();
      ++processed;
      if (value > best) {
        best = value;
        best_representatives = chosen;
      }
      return;
    }
    const int maximum = 31 - (7 - index);
    for (int value = next; value <= maximum; ++value) {
      chosen[index] = value;
      enumerate(index + 1, value + 1);
    }
  }

  void run() {
    for (int first = 1 + shard; first <= 24; first += shards) {
      chosen[0] = first;
      enumerate(1, first + 1);
    }
    std::cout << "{\"complete\":true,\"shard\":" << shard
              << ",\"shards\":" << shards << ",\"processed\":"
              << processed << ",\"best\":" << best
              << ",\"representatives\":[";
    for (int index = 0; index < 8; ++index) {
      if (index) std::cout << ',';
      std::cout << best_representatives[index];
    }
    std::cout << "]}\n";
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
