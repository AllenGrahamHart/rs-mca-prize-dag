#include <array>
#include <cstdlib>

#define main imported_e34_nested_quotient_main
#include "e34_nested_quotient_census.cpp"
#undef main

int main(int argc, char** argv) {
  if (argc != 5) return 2;
  const int profile = std::atoi(argv[1]);
  Search search;
  search.profile = profile;
  search.order = std::atoi(argv[2]);
  search.shard = std::atoi(argv[3]);
  search.shards = std::atoi(argv[4]);

  constexpr std::array<std::array<int, 4>, 8> profiles{{
      {{6, 6, 0, 0}},
      {{2, 7, 0, 0}},
      {{5, 4, 1, 0}},
      {{1, 5, 1, 0}},
      {{4, 2, 2, 0}},
      {{0, 3, 2, 0}},
      {{6, 2, 0, 1}},
      {{3, 0, 3, 0}},
  }};
  constexpr std::array<int, 8> levels{{2, 2, 3, 3, 3, 3, 4, 3}};
  if (profile < 0 || profile >= static_cast<int>(profiles.size())) return 2;
  search.profile_counts = profiles[profile];
  search.levels = levels[profile];

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
