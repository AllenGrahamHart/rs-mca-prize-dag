#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <unordered_set>

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
  std::set<int> lengths = {
      distance(heavy[0], heavy[1]), distance(heavy[0], heavy[2]),
      distance(heavy[1], heavy[2])};
  return lengths.size() == 3 && !lengths.count(64);
}

std::uint64_t choose4(int n) {
  if (n < 4) return 0;
  return static_cast<std::uint64_t>(n) * (n - 1) * (n - 2) * (n - 3) / 24;
}

std::set<int> weld_set(const Triple& heavy, int length) {
  std::set<int> result;
  for (int h : heavy) {
    for (int sign : {-1, 1}) {
      const int light = (h + sign * length + 128) % 128;
      if (std::find(heavy.begin(), heavy.end(), light) == heavy.end()) {
        result.insert(light);
      }
    }
  }
  return result;
}

std::set<int> combine(const std::set<int>& left, const std::set<int>& right) {
  std::set<int> result = left;
  result.insert(right.begin(), right.end());
  return result;
}

int intersection_size(const std::set<int>& left, const std::set<int>& right) {
  int result = 0;
  for (int value : left) result += right.count(value);
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
  const auto union01 = combine(welds[0], welds[1]);
  const auto union02 = combine(welds[0], welds[2]);
  const auto union12 = combine(welds[1], welds[2]);
  const auto union012 = combine(union01, welds[2]);
  const auto intersection01 = [&] {
    std::set<int> out;
    for (int value : welds[0]) if (welds[1].count(value)) out.insert(value);
    return out;
  }();
  const int triple_intersection = intersection_size(intersection01, welds[2]);
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
            << "],\"pair_intersections\":["
            << intersection_size(welds[0], welds[1]) << ','
            << intersection_size(welds[0], welds[2]) << ','
            << intersection_size(welds[1], welds[2])
            << "],\"triple_intersection\":" << triple_intersection
            << ",\"union_size\":" << union012.size()
            << ",\"supports\":" << supports
            << ",\"census_vectors\":" << 64 * supports << '}';
}

int main() {
  std::unordered_set<int> unseen;
  for (int a = 0; a < 126; ++a) {
    for (int b = a + 1; b < 127; ++b) {
      for (int c = b + 1; c < 128; ++c) {
        const Triple heavy = {a, b, c};
        if (generic(heavy)) unseen.insert(encode(heavy));
      }
    }
  }
  const std::uint64_t generic_triples = unseen.size();
  std::map<int, std::uint64_t> orbit_counts;
  while (!unseen.empty()) {
    const Triple seed = decode(*unseen.begin());
    std::unordered_set<int> orbit;
    for (int shift = 0; shift < 128; ++shift) {
      for (int unit = 1; unit < 128; unit += 2) {
        Triple image{};
        for (int i = 0; i < 3; ++i) image[i] = (unit * seed[i] + shift) % 128;
        std::sort(image.begin(), image.end());
        orbit.insert(encode(image));
      }
    }
    int canonical = 1 << 30;
    for (int key : orbit) canonical = std::min(canonical, key);
    orbit_counts[canonical] = orbit.size();
    for (int key : orbit) unseen.erase(key);
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
