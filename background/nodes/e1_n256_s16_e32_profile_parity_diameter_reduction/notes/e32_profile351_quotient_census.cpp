#include <array>
#include <cstdlib>

#define main imported_e34_nested_quotient_main
#include "e34_nested_quotient_census.cpp"
#undef main

int main(int argc, char** argv) {
  if (argc != 4) {
    return 2;
  }
  Search search;
  search.profile = 351;
  search.order = std::atoi(argv[1]);
  search.shard = std::atoi(argv[2]);
  search.shards = std::atoi(argv[3]);
  search.profile_counts = {{3, 5, 1, 0}};
  search.levels = 3;
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
