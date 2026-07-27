#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using Triple = std::array<int, 3>;

int distance(int left, int right) {
  const int delta = std::abs(left - right);
  return std::min(delta, 128 - delta);
}

int encode(const Triple& triple) {
  return (triple[0] << 14) | (triple[1] << 7) | triple[2];
}

Triple decode(int key) {
  return {(key >> 14) & 127, (key >> 7) & 127, key & 127};
}

bool generic(const Triple& heavy) {
  std::array<int, 3> lengths = {
      distance(heavy[0], heavy[1]), distance(heavy[0], heavy[2]),
      distance(heavy[1], heavy[2])};
  if (std::find(lengths.begin(), lengths.end(), 64) != lengths.end()) return false;
  std::sort(lengths.begin(), lengths.end());
  return lengths[0] != lengths[1] && lengths[1] != lengths[2];
}

int canonical(const Triple& heavy) {
  int best = 1 << 30;
  for (int origin : heavy) {
    for (int unit = 1; unit < 128; unit += 2) {
      Triple image{};
      for (int i = 0; i < 3; ++i) {
        image[i] = (unit * ((heavy[i] - origin + 128) % 128)) % 128;
      }
      std::sort(image.begin(), image.end());
      best = std::min(best, encode(image));
    }
  }
  return best;
}

std::uint64_t choose4(int n) {
  if (n < 4) return 0;
  return static_cast<std::uint64_t>(n) * (n - 1) * (n - 2) * (n - 3) / 24;
}

std::set<int> weld_set(const Triple& heavy, int length) {
  std::set<int> result;
  for (int light = 0; light < 128; ++light) {
    if (std::find(heavy.begin(), heavy.end(), light) != heavy.end()) continue;
    for (int h : heavy) {
      if (distance(light, h) == length) result.insert(light);
    }
  }
  return result;
}

std::set<int> unite(const std::set<int>& left, const std::set<int>& right) {
  std::set<int> result = left;
  result.insert(right.begin(), right.end());
  return result;
}

std::set<int> intersect(const std::set<int>& left, const std::set<int>& right) {
  std::set<int> result;
  std::set_intersection(left.begin(), left.end(), right.begin(), right.end(),
                        std::inserter(result, result.begin()));
  return result;
}

void print_row(int key, std::uint64_t heavy_triples) {
  const Triple heavy = decode(key);
  std::array<int, 3> lengths = {
      distance(heavy[0], heavy[1]), distance(heavy[0], heavy[2]),
      distance(heavy[1], heavy[2])};
  std::sort(lengths.begin(), lengths.end());
  const std::array<std::set<int>, 3> welds = {
      weld_set(heavy, lengths[0]), weld_set(heavy, lengths[1]),
      weld_set(heavy, lengths[2])};
  const auto union01 = unite(welds[0], welds[1]);
  const auto union02 = unite(welds[0], welds[2]);
  const auto union12 = unite(welds[1], welds[2]);
  const auto union012 = unite(union01, welds[2]);
  const auto intersection01 = intersect(welds[0], welds[1]);
  const auto intersection02 = intersect(welds[0], welds[2]);
  const auto intersection12 = intersect(welds[1], welds[2]);
  const auto intersection012 = intersect(intersection01, welds[2]);
  const std::uint64_t supports =
      choose4(125) - choose4(125 - welds[0].size()) -
      choose4(125 - welds[1].size()) - choose4(125 - welds[2].size()) +
      choose4(125 - union01.size()) + choose4(125 - union02.size()) +
      choose4(125 - union12.size()) - choose4(125 - union012.size());

  std::cout << "{\"heavy\":[" << heavy[0] << ',' << heavy[1] << ',' << heavy[2]
            << "],\"heavy_triples\":" << heavy_triples
            << ",\"lengths\":[" << lengths[0] << ',' << lengths[1] << ','
            << lengths[2] << "],\"weld_sizes\":[" << welds[0].size() << ','
            << welds[1].size() << ',' << welds[2].size()
            << "],\"pair_intersections\":[" << intersection01.size() << ','
            << intersection02.size() << ',' << intersection12.size()
            << "],\"triple_intersection\":" << intersection012.size()
            << ",\"union_size\":" << union012.size()
            << ",\"supports\":" << supports
            << ",\"census_vectors\":" << 64 * supports << '}';
}

int main() {
  std::map<int, std::uint64_t> orbit_counts;
  std::uint64_t generic_triples = 0;
  for (int a = 0; a < 126; ++a) {
    for (int b = a + 1; b < 127; ++b) {
      for (int c = b + 1; c < 128; ++c) {
        const Triple heavy = {a, b, c};
        if (!generic(heavy)) continue;
        ++generic_triples;
        ++orbit_counts[canonical(heavy)];
      }
    }
  }

  std::cout << "{\"complete\":true,\"generic_triples\":" << generic_triples
            << ",\"orbits\":" << orbit_counts.size() << ",\"rows\":[";
  bool first = true;
  for (const auto& [key, count] : orbit_counts) {
    if (!first) std::cout << ',';
    first = false;
    print_row(key, count);
  }
  std::cout << "]}\n";
  return 0;
}
