#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

namespace {

constexpr int kOrder = 128;
constexpr int kThreshold = 228;

int folded(int value) {
  value %= kOrder;
  if (value < 0) value += kOrder;
  return std::min(value, kOrder - value);
}

std::uint64_t mask_of(const std::array<int, 4>& support) {
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
    for (int index = 0; index < 4; ++index) {
      image[index] = support[index] * unit % kOrder;
    }
    std::sort(image.begin(), image.end());
    best = std::min(best, mask_of(image));
  }
  return best;
}

std::vector<int> classes(std::uint64_t mask) {
  std::vector<int> result;
  for (int distance = 1; distance < 64; ++distance) {
    if (mask & (std::uint64_t{1} << (distance - 1))) {
      result.push_back(distance);
    }
  }
  return result;
}

using Kernel = std::array<std::array<std::array<unsigned char, 64>, 64>, 64>;

Kernel make_kernel() {
  Kernel kernel{};
  for (int first = 1; first < 64; ++first) {
    for (int second = 1; second < 64; ++second) {
      for (int third = 1; third < 64; ++third) {
        for (int first_sign : {-1, 1}) {
          for (int second_sign : {-1, 1}) {
            for (int third_sign : {-1, 1}) {
              int sum = first_sign * first + second_sign * second +
                        third_sign * third;
              sum %= kOrder;
              if (sum < 0) sum += kOrder;
              kernel[first][second][third] += sum == 0;
            }
          }
        }
      }
    }
  }
  return kernel;
}

int base_cube(const std::vector<int>& base,
              const std::array<int, 64>& weight, const Kernel& kernel) {
  int answer = 0;
  for (int first : base) {
    for (int second : base) {
      for (int third : base) {
        answer += weight[first] * weight[second] * weight[third] *
                  kernel[first][second][third];
      }
    }
  }
  return answer;
}

int base_base_unit(const std::vector<int>& base,
                   const std::array<int, 64>& weight, int unit,
                   const Kernel& kernel) {
  int answer = 0;
  for (int first : base) {
    for (int second : base) {
      answer += weight[first] * weight[second] * kernel[first][second][unit];
    }
  }
  return answer;
}

int base_unit_unit(const std::vector<int>& base,
                   const std::array<int, 64>& weight, int first, int second,
                   const Kernel& kernel) {
  int answer = 0;
  for (int distance : base) {
    answer += weight[distance] * kernel[distance][first][second];
  }
  return answer;
}

struct Witness {
  int m3 = -1;
  std::uint64_t mask = 0;
  std::array<int, 2> promoted{{-1, -1}};
  std::array<int, 2> outside{{-1, -1}};
};

struct MaskRow {
  std::uint64_t mask = 0;
  std::uint64_t above = 0;
  int maximum = -1;
  std::array<int, 4> light{};
};

struct Stats {
  std::uint64_t assignments = 0;
  std::uint64_t above = 0;
  int minimum = 1 << 30;
  Witness best;
  std::map<int, std::uint64_t> histogram;
  std::vector<MaskRow> rows;

  void observe(int m3, const Witness& witness, MaskRow& row) {
    ++assignments;
    minimum = std::min(minimum, m3);
    row.maximum = std::max(row.maximum, m3);
    if (m3 > best.m3) best = witness;
    if (m3 > kThreshold) {
      ++above;
      ++row.above;
      ++histogram[m3];
    }
  }
};

void scan_412(std::uint64_t mask, const std::array<int, 4>& light,
              const std::vector<int>& odd,
              const std::vector<int>& outside, const Kernel& kernel,
              Stats& stats) {
  MaskRow row{mask, 0, -1, light};
  for (int first = 0; first < 6; ++first) {
    for (int second = first + 1; second < 6; ++second) {
      std::array<int, 64> weight{};
      for (int distance : odd) weight[distance] = 1;
      weight[odd[first]] = weight[odd[second]] = 3;
      const int constant = base_cube(odd, weight, kernel);
      for (int even : outside) {
        const int m3 =
            constant + 6 * base_base_unit(odd, weight, even, kernel) +
            12 * base_unit_unit(odd, weight, even, even, kernel) +
            8 * kernel[even][even][even];
        stats.observe(m3, {m3, mask, {{odd[first], odd[second]}}, {{even, -1}}},
                      row);
      }
    }
  }
  if (row.above) stats.rows.push_back(row);
}

void scan_6101(std::uint64_t mask, const std::array<int, 4>& light,
               const std::vector<int>& odd,
               const std::vector<int>& outside, const Kernel& kernel,
               Stats& stats) {
  MaskRow row{mask, 0, -1, light};
  std::array<int, 64> weight{};
  for (int distance : odd) weight[distance] = 1;
  const int constant = base_cube(odd, weight, kernel);
  std::array<int, 64> add_two{};
  std::array<int, 64> add_four{};
  for (int distance : outside) {
    const int bbu = base_base_unit(odd, weight, distance, kernel);
    const int buu = base_unit_unit(odd, weight, distance, distance, kernel);
    const int uuu = kernel[distance][distance][distance];
    add_two[distance] = 6 * bbu + 12 * buu + 8 * uuu;
    add_four[distance] = 12 * bbu + 48 * buu + 64 * uuu;
  }
  for (int even : outside) {
    for (int four : outside) {
      if (even == four) continue;
      const int cross =
          48 * base_unit_unit(odd, weight, even, four, kernel) +
          48 * kernel[even][even][four] +
          96 * kernel[even][four][four];
      const int m3 = constant + add_two[even] + add_four[four] + cross;
      stats.observe(m3, {m3, mask, {{-1, -1}}, {{even, four}}}, row);
    }
  }
  if (row.above) stats.rows.push_back(row);
}

void print_stats(const char* profile, const Stats& stats) {
  std::cout << "{\"profile\":\"" << profile << "\",\"assignments\":"
            << stats.assignments << ",\"above_cutoff\":" << stats.above
            << ",\"exceptional_masks\":" << stats.rows.size()
            << ",\"minimum_m3\":" << stats.minimum
            << ",\"maximum_m3\":" << stats.best.m3
            << ",\"witness\":{\"mask\":" << stats.best.mask
            << ",\"promoted\":[" << stats.best.promoted[0] << ','
            << stats.best.promoted[1] << "],\"outside\":["
            << stats.best.outside[0] << ',' << stats.best.outside[1]
            << "]},\"above_histogram\":{";
  bool first = true;
  for (const auto& [m3, count] : stats.histogram) {
    if (!first) std::cout << ',';
    first = false;
    std::cout << '\"' << m3 << "\":" << count;
  }
  std::vector<MaskRow> top = stats.rows;
  std::sort(top.begin(), top.end(), [](const MaskRow& left, const MaskRow& right) {
    return std::pair(left.maximum, left.mask) > std::pair(right.maximum, right.mask);
  });
  if (top.size() > 16) top.resize(16);
  std::cout << "},\"top_masks\":[";
  for (std::size_t index = 0; index < top.size(); ++index) {
    if (index) std::cout << ',';
    const MaskRow& row = top[index];
    std::cout << "{\"mask\":" << row.mask << ",\"above\":" << row.above
              << ",\"maximum_m3\":" << row.maximum << ",\"light\":["
              << row.light[0] << ',' << row.light[1] << ',' << row.light[2]
              << ',' << row.light[3] << "]}";
  }
  std::cout << "]}";
}

}  // namespace

int main() {
  std::map<std::uint64_t, std::array<int, 4>> masks;
  std::uint64_t normalized_supports = 0;
  for (int first = 1; first < 128; ++first) {
    for (int second = first + 1; second < 128; ++second) {
      for (int third = second + 1; third < 128; ++third) {
        const std::array<int, 4> support{{0, first, second, third}};
        if (!mask_of(support)) continue;
        ++normalized_supports;
        masks.try_emplace(canonical_mask(support), support);
      }
    }
  }
  if (normalized_supports != 280720 || masks.size() != 1234) return 3;

  const Kernel kernel = make_kernel();
  Stats profile_412;
  Stats profile_6101;
  for (const auto& [mask, support] : masks) {
    (void)support;
    const std::vector<int> odd = classes(mask);
    if (odd.size() != 6) return 3;
    std::vector<int> outside;
    for (int distance = 1; distance < 64; ++distance) {
      if (!(mask & (std::uint64_t{1} << (distance - 1)))) {
        outside.push_back(distance);
      }
    }
    if (outside.size() != 57) return 3;
    scan_412(mask, support, odd, outside, kernel, profile_412);
    scan_6101(mask, support, odd, outside, kernel, profile_6101);
  }

  std::cout << "{\"schema\":\"e1-e26-six-odd-cheap-relaxation-probe-v1\","
            << "\"complete\":true,\"threshold\":" << kThreshold
            << ",\"normalized_supports\":" << normalized_supports
            << ",\"odd_masks\":" << masks.size() << ",\"profiles\":[";
  print_stats("4,1,2", profile_412);
  std::cout << ',';
  print_stats("6,1,0,1", profile_6101);
  std::cout << "]}\n";
  return 0;
}
