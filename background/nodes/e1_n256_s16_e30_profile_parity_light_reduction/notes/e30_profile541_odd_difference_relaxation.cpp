#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>

namespace {

constexpr int kOrder = 128;
constexpr int kThreshold = 1087;

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

struct Canonical {
  std::uint64_t mask = 0;
  std::array<int, 4> support{};
};

Canonical canonicalize(const std::array<int, 4>& support) {
  Canonical best{~std::uint64_t{0}, {{128, 128, 128, 128}}};
  for (int unit = 1; unit < kOrder; unit += 2) {
    std::array<int, 4> image{};
    for (int index = 0; index < 4; ++index) image[index] = support[index] * unit % kOrder;
    std::sort(image.begin(), image.end());
    const std::uint64_t mask = distance_mask(image);
    if (mask < best.mask || (mask == best.mask && image < best.support)) best = {mask, image};
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

using Kernel = std::array<std::array<std::array<unsigned char, 64>, 64>, 64>;

Kernel make_kernel() {
  Kernel kernel{};
  for (int first = 1; first < 64; ++first) {
    for (int second = 1; second < 64; ++second) {
      for (int third = 1; third < 64; ++third) {
        int count = 0;
        for (int first_sign : {-1, 1}) {
          for (int second_sign : {-1, 1}) {
            for (int third_sign : {-1, 1}) {
              int sum = first_sign * first + second_sign * second + third_sign * third;
              sum %= kOrder;
              if (sum < 0) sum += kOrder;
              count += sum == 0;
            }
          }
        }
        kernel[first][second][third] = static_cast<unsigned char>(count);
      }
    }
  }
  return kernel;
}

int base_cube(const std::vector<int>& odd, const std::array<int, 64>& weight,
              const Kernel& kernel) {
  int answer = 0;
  for (int first : odd) {
    for (int second : odd) {
      for (int third : odd) {
        answer += weight[first] * weight[second] * weight[third] *
                  kernel[first][second][third];
      }
    }
  }
  return answer;
}

int base_base_unit(const std::vector<int>& odd, const std::array<int, 64>& weight,
                   int unit, const Kernel& kernel) {
  int answer = 0;
  for (int first : odd) {
    for (int second : odd) {
      answer += weight[first] * weight[second] * kernel[first][second][unit];
    }
  }
  return answer;
}

int base_unit_unit(const std::vector<int>& odd, const std::array<int, 64>& weight,
                   int first, int second, const Kernel& kernel) {
  int answer = 0;
  for (int distance : odd) answer += weight[distance] * kernel[distance][first][second];
  return answer;
}

struct Witness {
  int m3 = -1;
  std::uint64_t odd_mask = 0;
  std::array<int, 4> light{};
  std::array<int, 6> odd{};
  int promoted = 0;
  std::array<int, 4> even{};
};

template <typename Values>
void print_array(const Values& values) {
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
  std::cout << ",\"promoted_to_three\":" << witness.promoted
            << ",\"even_classes\":";
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
  std::uint64_t normalized_supports = 0;
  for (int first = 1; first < 128; ++first) {
    for (int second = first + 1; second < 128; ++second) {
      for (int third = second + 1; third < 128; ++third) {
        const std::array<int, 4> support{{0, first, second, third}};
        if (!distance_mask(support)) continue;
        ++normalized_supports;
        const Canonical canonical = canonicalize(support);
        masks.try_emplace(canonical.mask, canonical.support);
      }
    }
  }

  const Kernel kernel = make_kernel();
  Witness best;
  std::vector<Witness> exceptional;
  std::map<int, std::uint64_t> above_histogram;
  std::uint64_t tested_masks = 0;
  std::uint64_t assignments = 0;
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
    for (int promoted_index = 0; promoted_index < 6; ++promoted_index) {
      std::array<int, 64> weight{};
      for (int distance : odd) weight[distance] = 1;
      weight[odd[promoted_index]] = 3;
      const int constant = base_cube(odd, weight, kernel);
      std::array<int, 64> single{};
      std::array<std::array<int, 64>, 64> pair{};
      for (int distance : outside) {
        single[distance] =
            6 * base_base_unit(odd, weight, distance, kernel) +
            12 * base_unit_unit(odd, weight, distance, distance, kernel) +
            8 * kernel[distance][distance][distance];
      }
      for (std::size_t left = 0; left < outside.size(); ++left) {
        for (std::size_t right = left + 1; right < outside.size(); ++right) {
          const int first_even = outside[left];
          const int second_even = outside[right];
          pair[first_even][second_even] = pair[second_even][first_even] =
              24 * base_unit_unit(odd, weight, first_even, second_even, kernel) +
              24 * kernel[first_even][first_even][second_even] +
              24 * kernel[first_even][second_even][second_even];
        }
      }
      for (std::size_t first = 0; first + 3 < outside.size(); ++first) {
        const int a = outside[first];
        for (std::size_t second = first + 1; second + 2 < outside.size(); ++second) {
          const int b = outside[second];
          for (std::size_t third = second + 1; third + 1 < outside.size(); ++third) {
            const int c = outside[third];
            const int partial = constant + single[a] + single[b] + single[c] +
                                pair[a][b] + pair[a][c] + pair[b][c] +
                                48 * kernel[a][b][c];
            for (std::size_t fourth = third + 1; fourth < outside.size(); ++fourth) {
              const int d = outside[fourth];
              const int m3 = partial + single[d] + pair[a][d] + pair[b][d] +
                             pair[c][d] + 48 * (kernel[a][b][d] +
                                                kernel[a][c][d] +
                                                kernel[b][c][d]);
              ++assignments;
              Witness candidate{
                  m3,
                  mask,
                  light,
                  {{odd[0], odd[1], odd[2], odd[3], odd[4], odd[5]}},
                  odd[promoted_index],
                  {{a, b, c, d}},
              };
              if (m3 > kThreshold) {
                ++above_histogram[m3];
                exceptional.push_back(candidate);
              }
              if (m3 > best.m3) {
                best = candidate;
              }
            }
          }
        }
      }
    }
  }

  std::uint64_t above_total = 0;
  for (const auto& [m3, count] : above_histogram) above_total += count;
  std::cout << "{\"complete\":true,\"shard\":" << shard
            << ",\"shards\":" << shards
            << ",\"normalized_six_odd_supports\":" << normalized_supports
            << ",\"distinct_odd_masks\":" << masks.size()
            << ",\"tested_masks\":" << tested_masks
            << ",\"assignments\":" << assignments
            << ",\"above_threshold\":" << above_total
            << ",\"above_histogram\":{";
  bool first_histogram = true;
  for (const auto& [m3, count] : above_histogram) {
    if (!first_histogram) std::cout << ',';
    first_histogram = false;
    std::cout << '\"' << m3 << "\":" << count;
  }
  std::cout << "},\"threshold\":" << kThreshold
            << ",\"maximum_m3\":" << best.m3 << ",\"witness\":";
  print_witness(best);
  std::cout << ",\"exceptional\":[";
  for (std::size_t index = 0; index < exceptional.size(); ++index) {
    if (index) std::cout << ',';
    print_witness(exceptional[index]);
  }
  std::cout << "]}\n";
  return 0;
}
