#include <array>
#include <cstdlib>

#define main imported_nested_quotient_main
#include "../../background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e34_nested_quotient_census.cpp"
#undef main

int main(int argc, char** argv) {
  if (argc != 5) return 2;
  Search search;
  search.profile = std::atoi(argv[1]);
  search.order = std::atoi(argv[2]);
  search.shard = std::atoi(argv[3]);
  search.shards = std::atoi(argv[4]);

  constexpr std::array<std::array<int, 4>, 4> profiles{{
      {{6, 5, 0, 0}},
      {{5, 3, 1, 0}},
      {{4, 1, 2, 0}},
      {{6, 1, 0, 1}},
  }};
  constexpr std::array<int, 4> levels{{2, 3, 3, 4}};
  if (search.profile < 0 || search.profile >= static_cast<int>(profiles.size())) {
    return 2;
  }
  search.profile_counts = profiles[search.profile];
  search.levels = levels[search.profile];

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
