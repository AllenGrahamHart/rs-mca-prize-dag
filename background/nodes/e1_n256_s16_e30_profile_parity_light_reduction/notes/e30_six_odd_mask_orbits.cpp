#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>

namespace {

constexpr int kOrder = 128;

int folded(int value) {
  value %= kOrder;
  if (value < 0) value += kOrder;
  return std::min(value, kOrder - value);
}

std::uint64_t distance_mask(const std::array<int, 4>& support) {
  std::uint64_t mask = 0;
  for (int left = 0; left < 4; ++left) {
    for (int right = left + 1; right < 4; ++right) {
      const int distance = folded(support[right] - support[left]);
      if (distance == 0 || distance == 64) return 0;
      const std::uint64_t bit = std::uint64_t{1} << (distance - 1);
      if (mask & bit) return 0;
      mask |= bit;
    }
  }
  return mask;
}

std::uint64_t canonical_mask(const std::array<int, 4>& support) {
  std::uint64_t best = ~std::uint64_t{0};
  for (int unit = 1; unit < kOrder; unit += 2) {
    std::array<int, 4> image{};
    for (int index = 0; index < 4; ++index) image[index] = support[index] * unit % kOrder;
    std::sort(image.begin(), image.end());
    best = std::min(best, distance_mask(image));
  }
  return best;
}

std::array<int, 4> canonical_support(const std::array<int, 4>& support) {
  std::array<int, 4> best{{128, 128, 128, 128}};
  for (int anchor : support) {
    for (int unit = 1; unit < kOrder; unit += 2) {
      std::array<int, 4> image{};
      for (int index = 0; index < 4; ++index) {
        image[index] = ((support[index] - anchor + kOrder) % kOrder) * unit % kOrder;
      }
      std::sort(image.begin(), image.end());
      if (image < best) best = image;
    }
  }
  return best;
}

template <typename Values>
void print_array(const Values& values) {
  std::cout << '[';
  for (std::size_t index = 0; index < values.size(); ++index) {
    if (index) std::cout << ',';
    std::cout << values[index];
  }
  std::cout << ']';
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 3) return 2;
  const int shard = std::atoi(argv[1]);
  const int shards = std::atoi(argv[2]);
  if (shards <= 0 || shard < 0 || shard >= shards) return 2;

  std::map<std::uint64_t, std::set<std::array<int, 4>>> rows;
  std::uint64_t normalized = 0;
  std::uint64_t index = 0;
  for (int first = 1; first < 128; ++first) {
    for (int second = first + 1; second < 128; ++second) {
      for (int third = second + 1; third < 128; ++third) {
        const std::array<int, 4> support{{0, first, second, third}};
        if (!distance_mask(support)) continue;
        const std::uint64_t here = index++;
        if (here % shards != static_cast<std::uint64_t>(shard)) continue;
        ++normalized;
        rows[canonical_mask(support)].insert(canonical_support(support));
      }
    }
  }

  std::cout << "{\"complete\":true,\"shard\":" << shard
            << ",\"shards\":" << shards
            << ",\"normalized_six_odd_supports\":" << normalized
            << ",\"rows\":[";
  bool first_row = true;
  for (const auto& [mask, orbits] : rows) {
    if (!first_row) std::cout << ',';
    first_row = false;
    std::cout << "{\"odd_mask\":" << mask << ",\"orbits\":[";
    bool first_orbit = true;
    for (const auto& orbit : orbits) {
      if (!first_orbit) std::cout << ',';
      first_orbit = false;
      print_array(orbit);
    }
    std::cout << "]}";
  }
  std::cout << "]}\n";
  return 0;
}
