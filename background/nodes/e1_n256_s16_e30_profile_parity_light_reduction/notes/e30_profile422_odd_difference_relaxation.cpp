#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <vector>

namespace {

constexpr int kOrder = 128;
constexpr int kThreshold = 1087;

int folded_class(int value) {
  value %= kOrder;
  if (value < 0) value += kOrder;
  return value <= 64 ? value : kOrder - value;
}

std::uint64_t distance_mask(const std::array<int, 4>& support) {
  std::uint64_t mask = 0;
  for (int left = 0; left < 4; ++left) {
    for (int right = left + 1; right < 4; ++right) {
      const int distance = folded_class(support[right] - support[left]);
      if (distance == 0 || distance == 64) return 0;
      const std::uint64_t bit = std::uint64_t{1} << (distance - 1);
      if (mask & bit) return 0;
      mask |= bit;
    }
  }
  return mask;
}

struct Canonical {
  std::uint64_t mask = 0;
  std::array<int, 4> support{};
};

Canonical canonicalize(const std::array<int, 4>& support) {
  Canonical best;
  best.mask = ~std::uint64_t{0};
  for (int unit = 1; unit < kOrder; unit += 2) {
    std::array<int, 4> image{};
    for (int index = 0; index < 4; ++index) {
      image[index] = support[index] * unit % kOrder;
    }
    std::sort(image.begin(), image.end());
    const std::uint64_t mask = distance_mask(image);
    if (mask < best.mask || (mask == best.mask && image < best.support)) {
      best = {mask, image};
    }
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

std::vector<int> classes(std::uint64_t mask) {
  std::vector<int> result;
  for (int distance = 1; distance < 64; ++distance) {
    if (mask & (std::uint64_t{1} << (distance - 1))) result.push_back(distance);
  }
  return result;
}

int base_cube(const std::array<int, kOrder>& base) {
  int answer = 0;
  for (int left = 0; left < kOrder; ++left) {
    if (!base[left]) continue;
    for (int right = 0; right < kOrder; ++right) {
      if (!base[right]) continue;
      const int target = (2 * kOrder - left - right) % kOrder;
      answer += base[left] * base[right] * base[target];
    }
  }
  return answer;
}

bool in_unit_pair(int residue, int distance) {
  return residue == distance || residue == kOrder - distance;
}

int base_base_unit(const std::array<int, kOrder>& base, int distance) {
  int answer = 0;
  for (int left = 0; left < kOrder; ++left) {
    if (!base[left]) continue;
    for (int right = 0; right < kOrder; ++right) {
      if (!base[right]) continue;
      const int target = (2 * kOrder - left - right) % kOrder;
      if (in_unit_pair(target, distance)) answer += base[left] * base[right];
    }
  }
  return answer;
}

int base_unit_unit(const std::array<int, kOrder>& base, int first, int second) {
  int answer = 0;
  for (int left : {first, kOrder - first}) {
    for (int right : {second, kOrder - second}) {
      answer += base[(2 * kOrder - left - right) % kOrder];
    }
  }
  return answer;
}

int unit_unit_unit(int first, int second, int third) {
  int answer = 0;
  for (int left : {first, kOrder - first}) {
    for (int middle : {second, kOrder - second}) {
      for (int right : {third, kOrder - third}) {
        if ((left + middle + right) % kOrder == 0) ++answer;
      }
    }
  }
  return answer;
}

struct Witness {
  int m3 = -1;
  std::uint64_t odd_mask = 0;
  std::array<int, 4> light{};
  std::array<int, 6> odd{};
  std::array<int, 2> promoted{};
  std::array<int, 2> even{};
};

void print_array(const auto& values) {
  std::cout << '[';
  for (std::size_t index = 0; index < values.size(); ++index) {
    if (index) std::cout << ',';
    std::cout << values[index];
  }
  std::cout << ']';
}

void print_witness(const Witness& witness) {
  std::cout << "{\"m3\":" << witness.m3
            << ",\"odd_mask\":" << witness.odd_mask << ",\"light\":";
  print_array(witness.light);
  std::cout << ",\"odd_classes\":";
  print_array(witness.odd);
  std::cout << ",\"promoted_to_three\":";
  print_array(witness.promoted);
  std::cout << ",\"even_classes\":";
  print_array(witness.even);
  std::cout << '}';
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 3) return 2;
  const int shard = std::atoi(argv[1]);
  const int shards = std::atoi(argv[2]);
  if (shards <= 0 || shard < 0 || shard >= shards) return 2;

  std::map<std::uint64_t, std::array<int, 4>> masks;
  std::map<std::uint64_t, std::set<std::array<int, 4>>> support_orbits;
  std::uint64_t normalized_supports = 0;
  for (int first = 1; first < 128; ++first) {
    for (int second = first + 1; second < 128; ++second) {
      for (int third = second + 1; third < 128; ++third) {
        const std::array<int, 4> support{{0, first, second, third}};
        if (!distance_mask(support)) continue;
        ++normalized_supports;
        const Canonical canonical = canonicalize(support);
        const std::array<int, 4> orbit = canonical_support(support);
        masks.try_emplace(canonical.mask, orbit);
        support_orbits[canonical.mask].insert(orbit);
      }
    }
  }

  Witness best;
  std::uint64_t tested_masks = 0;
  std::uint64_t assignments = 0;
  std::map<int, std::uint64_t> above_threshold;
  std::vector<Witness> exceptional;
  std::uint64_t mask_index = 0;
  for (const auto& [mask, light] : masks) {
    if (mask_index++ % shards != static_cast<std::uint64_t>(shard)) continue;
    ++tested_masks;
    const std::vector<int> odd = classes(mask);
    if (odd.size() != 6) return 3;
    std::vector<int> outside;
    for (int distance = 1; distance < 64; ++distance) {
      if (!(mask & (std::uint64_t{1} << (distance - 1)))) outside.push_back(distance);
    }
    if (outside.size() != 57) return 3;

    for (int first_promoted = 0; first_promoted < 6; ++first_promoted) {
      for (int second_promoted = first_promoted + 1; second_promoted < 6;
           ++second_promoted) {
        std::array<int, kOrder> base{};
        for (int distance : odd) {
          base[distance] = base[kOrder - distance] = 1;
        }
        for (int index : {first_promoted, second_promoted}) {
          const int distance = odd[index];
          base[distance] = base[kOrder - distance] = 3;
        }
        const int constant = base_cube(base);
        std::array<int, 64> single{};
        for (int distance : outside) {
          single[distance] =
              6 * base_base_unit(base, distance) +
              12 * base_unit_unit(base, distance, distance) +
              8 * unit_unit_unit(distance, distance, distance);
        }
        for (std::size_t left = 0; left < outside.size(); ++left) {
          const int first_even = outside[left];
          for (std::size_t right = left + 1; right < outside.size(); ++right) {
            const int second_even = outside[right];
            const int pair =
                24 * base_unit_unit(base, first_even, second_even) +
                24 * unit_unit_unit(first_even, first_even, second_even) +
                24 * unit_unit_unit(first_even, second_even, second_even);
            const int m3 = constant + single[first_even] + single[second_even] + pair;
            ++assignments;
            if (m3 > kThreshold) {
              ++above_threshold[m3];
              exceptional.push_back({m3, mask, light,
                                     {{odd[0], odd[1], odd[2], odd[3], odd[4], odd[5]}},
                                     {{odd[first_promoted], odd[second_promoted]}},
                                     {{first_even, second_even}}});
            }
            if (m3 > best.m3) {
              best.m3 = m3;
              best.odd_mask = mask;
              best.light = light;
              std::copy(odd.begin(), odd.end(), best.odd.begin());
              best.promoted = {{odd[first_promoted], odd[second_promoted]}};
              best.even = {{first_even, second_even}};
            }
          }
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"shard\":" << shard
            << ",\"shards\":" << shards
            << ",\"normalized_six_odd_supports\":" << normalized_supports
            << ",\"distinct_odd_masks\":" << masks.size()
            << ",\"tested_masks\":" << tested_masks
            << ",\"assignments\":" << assignments
            << ",\"above_threshold\":";
  std::uint64_t above_total = 0;
  for (const auto& [m3, count] : above_threshold) above_total += count;
  std::cout << above_total << ",\"above_histogram\":{";
  bool first_histogram = true;
  for (const auto& [m3, count] : above_threshold) {
    if (!first_histogram) std::cout << ',';
    first_histogram = false;
    std::cout << '\"' << m3 << "\":" << count;
  }
  std::cout << '}'
            << ",\"threshold\":" << kThreshold
            << ",\"maximum_m3\":" << best.m3
            << ",\"witness\":";
  print_witness(best);
  std::cout << ",\"exceptional\":[";
  for (std::size_t index = 0; index < exceptional.size(); ++index) {
    if (index) std::cout << ',';
    print_witness(exceptional[index]);
  }
  std::cout << "],\"exceptional_light_orbits\":[";
  std::set<std::uint64_t> printed_masks;
  bool first_mask = true;
  for (const Witness& witness : exceptional) {
    if (!printed_masks.insert(witness.odd_mask).second) continue;
    if (!first_mask) std::cout << ',';
    first_mask = false;
    std::cout << "{\"odd_mask\":" << witness.odd_mask << ",\"orbits\":[";
    bool first_orbit = true;
    for (const auto& orbit : support_orbits.at(witness.odd_mask)) {
      if (!first_orbit) std::cout << ',';
      first_orbit = false;
      print_array(orbit);
    }
    std::cout << "]}";
  }
  std::cout << "]}\n";
  return 0;
}
