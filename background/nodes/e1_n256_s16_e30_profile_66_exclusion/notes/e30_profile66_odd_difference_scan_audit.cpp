#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

namespace {

constexpr int kOrder = 128;
constexpr int kThreshold = 1087;
constexpr int kHistogramLimit = 46656;

int base_cube(const std::array<int, kOrder>& base) {
  int answer = 0;
  for (int left = 0; left < kOrder; ++left) {
    if (!base[left]) continue;
    for (int right = 0; right < kOrder; ++right) {
      if (!base[right]) continue;
      answer += base[left] * base[right] *
                base[(2 * kOrder - left - right) % kOrder];
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
  std::array<unsigned char, kOrder> pair_sums{};
  for (int left : {first, kOrder - first}) {
    for (int right : {second, kOrder - second}) {
      ++pair_sums[(left + right) % kOrder];
    }
  }
  return pair_sums[third] + pair_sums[kOrder - third];
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
  if (argc != 7) return 2;
  const int index = std::atoi(argv[1]);
  const std::uint64_t mask = std::strtoull(argv[2], nullptr, 10);
  std::array<int, 4> light{};
  for (int position = 0; position < 4; ++position) {
    light[position] = std::atoi(argv[position + 3]);
  }

  std::array<int, 6> odd{};
  std::array<int, 57> outside{};
  std::array<int, kOrder> base{};
  int odd_count = 0;
  int outside_count = 0;
  for (int distance = 1; distance < 64; ++distance) {
    if (mask & (std::uint64_t{1} << (distance - 1))) {
      if (odd_count >= 6) return 3;
      odd[odd_count++] = distance;
      base[distance] = base[kOrder - distance] = 1;
    } else {
      if (outside_count >= 57) return 3;
      outside[outside_count++] = distance;
    }
  }
  if (odd_count != 6 || outside_count != 57) return 3;

  const int constant = base_cube(base);
  std::array<int, 57> single{};
  std::array<std::array<int, 57>, 57> pair{};
  std::array<std::array<std::array<unsigned short, 57>, 57>, 57> triple{};
  for (int ia = 0; ia < 57; ++ia) {
    const int a = outside[ia];
    single[ia] = 6 * base_base_unit(base, a) +
                 12 * base_unit_unit(base, a, a) +
                 8 * unit_unit_unit(a, a, a);
    for (int ib = ia + 1; ib < 57; ++ib) {
      const int b = outside[ib];
      pair[ia][ib] = pair[ib][ia] =
          24 * base_unit_unit(base, a, b) +
          24 * unit_unit_unit(a, a, b) + 24 * unit_unit_unit(a, b, b);
      for (int ic = ib + 1; ic < 57; ++ic) {
        const unsigned short contribution = static_cast<unsigned short>(
            48 * unit_unit_unit(a, b, outside[ic]));
        triple[ia][ib][ic] = contribution;
        triple[ia][ic][ib] = contribution;
        triple[ib][ia][ic] = contribution;
        triple[ib][ic][ia] = contribution;
        triple[ic][ia][ib] = contribution;
        triple[ic][ib][ia] = contribution;
      }
    }
  }

  std::uint64_t assignments = 0;
  std::uint64_t above_threshold = 0;
  std::array<std::uint64_t, kHistogramLimit + 1> histogram{};
  int maximum_m3 = -1;
  std::array<int, 6> maximum_even{};
  std::array<int, 57> extension{};
  std::array<std::array<int, 57>, 57> adjusted_pair{};

  for (int ia = 0; ia + 5 < 57; ++ia) {
    for (int ib = ia + 1; ib + 4 < 57; ++ib) {
      for (int ic = ib + 1; ic + 3 < 57; ++ic) {
        const int score_c =
            constant + single[ia] + single[ib] + single[ic] + pair[ia][ib] +
            pair[ia][ic] + pair[ib][ic] + triple[ia][ib][ic];
        for (int candidate = ic + 1; candidate < 57; ++candidate) {
          extension[candidate] =
              single[candidate] + pair[ia][candidate] + pair[ib][candidate] +
              pair[ic][candidate] + triple[ia][ib][candidate] +
              triple[ia][ic][candidate] + triple[ib][ic][candidate];
        }
        for (int left = ic + 1; left + 1 < 57; ++left) {
          for (int right = left + 1; right < 57; ++right) {
            adjusted_pair[left][right] = adjusted_pair[right][left] =
                pair[left][right] + triple[ia][left][right] +
                triple[ib][left][right] + triple[ic][left][right];
          }
        }
        for (int id = ic + 1; id + 2 < 57; ++id) {
          for (int ie = id + 1; ie + 1 < 57; ++ie) {
            for (int iff = ie + 1; iff < 57; ++iff) {
              const int m3 = score_c + extension[id] + extension[ie] +
                             extension[iff] + adjusted_pair[id][ie] +
                             adjusted_pair[id][iff] + adjusted_pair[ie][iff] +
                             triple[id][ie][iff];
              ++assignments;
              if (m3 > kThreshold) {
                ++above_threshold;
                if (m3 > kHistogramLimit) return 4;
                ++histogram[m3];
              }
              if (m3 > maximum_m3) {
                maximum_m3 = m3;
                maximum_even = {{outside[ia], outside[ib], outside[ic],
                                 outside[id], outside[ie], outside[iff]}};
              }
            }
          }
        }
      }
    }
  }

  std::cout << "{\"complete\":true,\"index\":" << index
            << ",\"odd_mask\":" << mask << ",\"light\":";
  print_array(light);
  std::cout << ",\"odd_classes\":";
  print_array(odd);
  std::cout << ",\"assignments\":" << assignments
            << ",\"above_threshold\":" << above_threshold
            << ",\"above_histogram\":{";
  bool first = true;
  for (int m3 = kThreshold + 1; m3 <= kHistogramLimit; ++m3) {
    if (!histogram[m3]) continue;
    if (!first) std::cout << ',';
    first = false;
    std::cout << '\"' << m3 << "\":" << histogram[m3];
  }
  std::cout << "},\"threshold\":" << kThreshold
            << ",\"maximum_m3\":" << maximum_m3
            << ",\"maximum_even_classes\":";
  print_array(maximum_even);
  std::cout << "}\n";
  return 0;
}
