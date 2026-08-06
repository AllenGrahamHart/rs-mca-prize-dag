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
              int sum = first_sign * first + second_sign * second +
                        third_sign * third;
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

int base_cube(const std::array<int, 6>& odd, const Kernel& kernel) {
  int answer = 0;
  for (int first : odd) {
    for (int second : odd) {
      for (int third : odd) answer += kernel[first][second][third];
    }
  }
  return answer;
}

int base_base_unit(const std::array<int, 6>& odd, int unit,
                   const Kernel& kernel) {
  int answer = 0;
  for (int first : odd) {
    for (int second : odd) answer += kernel[first][second][unit];
  }
  return answer;
}

int base_unit_unit(const std::array<int, 6>& odd, int first, int second,
                   const Kernel& kernel) {
  int answer = 0;
  for (int distance : odd) answer += kernel[distance][first][second];
  return answer;
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
  int odd_count = 0;
  int outside_count = 0;
  for (int distance = 1; distance < 64; ++distance) {
    if (mask & (std::uint64_t{1} << (distance - 1))) {
      if (odd_count >= 6) return 3;
      odd[odd_count++] = distance;
    } else {
      if (outside_count >= 57) return 3;
      outside[outside_count++] = distance;
    }
  }
  if (odd_count != 6 || outside_count != 57) return 3;

  const Kernel kernel = make_kernel();
  const int constant = base_cube(odd, kernel);
  std::array<int, 57> single{};
  std::array<std::array<int, 57>, 57> pair{};
  std::array<std::array<std::array<unsigned short, 57>, 57>, 57> triple{};
  for (int index_a = 0; index_a < 57; ++index_a) {
    const int a = outside[index_a];
    single[index_a] =
        6 * base_base_unit(odd, a, kernel) +
        12 * base_unit_unit(odd, a, a, kernel) +
        8 * kernel[a][a][a];
    for (int index_b = index_a + 1; index_b < 57; ++index_b) {
      const int b = outside[index_b];
      pair[index_a][index_b] = pair[index_b][index_a] =
          24 * base_unit_unit(odd, a, b, kernel) +
          24 * kernel[a][a][b] + 24 * kernel[a][b][b];
      for (int index_c = index_b + 1; index_c < 57; ++index_c) {
        const unsigned short contribution = static_cast<unsigned short>(
            48 * kernel[a][b][outside[index_c]]);
        triple[index_a][index_b][index_c] = contribution;
        triple[index_a][index_c][index_b] = contribution;
        triple[index_b][index_a][index_c] = contribution;
        triple[index_b][index_c][index_a] = contribution;
        triple[index_c][index_a][index_b] = contribution;
        triple[index_c][index_b][index_a] = contribution;
      }
    }
  }

  std::uint64_t assignments = 0;
  std::uint64_t above_threshold = 0;
  std::array<std::uint64_t, kHistogramLimit + 1> histogram{};
  int maximum_m3 = -1;
  std::array<int, 6> maximum_even{};
  std::array<int, 57> extension{};

  for (int ia = 0; ia + 5 < 57; ++ia) {
    const int score_a = constant + single[ia];
    for (int ib = ia + 1; ib + 4 < 57; ++ib) {
      const int score_b = score_a + single[ib] + pair[ia][ib];
      for (int ic = ib + 1; ic + 3 < 57; ++ic) {
        const int score_c = score_b + single[ic] + pair[ia][ic] +
                            pair[ib][ic] + triple[ia][ib][ic];
        for (int id = ic + 1; id + 2 < 57; ++id) {
          const int score_d =
              score_c + single[id] + pair[ia][id] + pair[ib][id] +
              pair[ic][id] + triple[ia][ib][id] + triple[ia][ic][id] +
              triple[ib][ic][id];
          for (int candidate = id + 1; candidate < 57; ++candidate) {
            extension[candidate] =
                single[candidate] + pair[ia][candidate] + pair[ib][candidate] +
                pair[ic][candidate] + pair[id][candidate] +
                triple[ia][ib][candidate] + triple[ia][ic][candidate] +
                triple[ia][id][candidate] + triple[ib][ic][candidate] +
                triple[ib][id][candidate] + triple[ic][id][candidate];
          }
          for (int ie = id + 1; ie + 1 < 57; ++ie) {
            const int score_e = score_d + extension[ie];
            for (int iff = ie + 1; iff < 57; ++iff) {
              const int m3 = score_e + extension[iff] + pair[ie][iff] +
                             triple[ia][ie][iff] + triple[ib][ie][iff] +
                             triple[ic][ie][iff] + triple[id][ie][iff];
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
