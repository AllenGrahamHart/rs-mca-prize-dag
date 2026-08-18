#!/usr/bin/env python3
"""Build an exact NTT/interpolation determinant for the cleared R76 matrix."""


PRIME = 2130706433
PRIMITIVE_ROOT = 3
NTT_SIZE = 32768
NTT_ROOT = 1168510561
DIMENSION = 16
DEGREE_BOUND = 22208
WITNESS_T = 2
WITNESS_DETERMINANT = 1087830147
HOLDOUT_T = 3


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(matrix_payload):
    row = matrix_payload["row"]
    require(matrix_payload["collection_complete"] is True and
            matrix_payload["field"] == PRIME and row["status"] == "COMPLETE" and
            row["dimension"] == DIMENSION and
            row["matrix_nonzero_entry_count"] == len(row["matrix_entries"]) == 256 and
            row["matrix_maximum_degree"] == 1388 and
            DIMENSION * row["matrix_maximum_degree"] == DEGREE_BOUND,
            "polynomial matrix bank")
    entries = sorted(row["matrix_entries"],
                     key=lambda item: (item["row"], item["column"]))
    require([(item["row"], item["column"]) for item in entries] ==
            [(i, j) for i in range(1, DIMENSION + 1)
             for j in range(1, DIMENSION + 1)], "matrix order")
    coefficient_rows = ",\n".join(
        "{" + ",".join(str(value % PRIME) for value in item["coefficients"]) + "}"
        for item in entries
    )
    program = f"""
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <omp.h>

using u32 = std::uint32_t;
using u64 = std::uint64_t;
constexpr u32 P = {PRIME}u;
constexpr int N = {NTT_SIZE};
constexpr int D = {DIMENSION};
constexpr int DEGREE_BOUND = {DEGREE_BOUND};
constexpr u32 ROOT = {NTT_ROOT}u;

const std::vector<std::vector<u32>> COEFFICIENTS = {{
{coefficient_rows}
}};

u32 multiply(u32 a, u32 b) {{
  return static_cast<u32>((static_cast<u64>(a) * b) % P);
}}

u32 power(u32 value, u64 exponent) {{
  u32 output = 1;
  while (exponent) {{
    if (exponent & 1) output = multiply(output, value);
    value = multiply(value, value);
    exponent >>= 1;
  }}
  return output;
}}

u32 add(u32 a, u32 b) {{
  u32 value = a + b;
  return value >= P ? value - P : value;
}}

u32 subtract(u32 a, u32 b) {{
  return a >= b ? a - b : a + P - b;
}}

void ntt(std::vector<u32>& values, bool inverse) {{
  const int size = static_cast<int>(values.size());
  for (int i = 1, j = 0; i < size; ++i) {{
    int bit = size >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) std::swap(values[i], values[j]);
  }}
  for (int length = 2; length <= size; length <<= 1) {{
    u32 step = power(ROOT, N / length);
    if (inverse) step = power(step, P - 2);
    for (int start = 0; start < size; start += length) {{
      u32 omega = 1;
      for (int offset = 0; offset < length / 2; ++offset) {{
        u32 even = values[start + offset];
        u32 odd = multiply(values[start + offset + length / 2], omega);
        values[start + offset] = add(even, odd);
        values[start + offset + length / 2] = subtract(even, odd);
        omega = multiply(omega, step);
      }}
    }}
  }}
  if (inverse) {{
    u32 inverse_size = power(static_cast<u32>(size), P - 2);
    for (u32& value : values) value = multiply(value, inverse_size);
  }}
}}

u32 determinant(std::array<std::array<u32, D>, D> matrix) {{
  u32 output = 1;
  for (int column = 0; column < D; ++column) {{
    int pivot = column;
    while (pivot < D && matrix[pivot][column] == 0) ++pivot;
    if (pivot == D) return 0;
    if (pivot != column) {{
      std::swap(matrix[pivot], matrix[column]);
      if (output != 0) output = P - output;
    }}
    u32 pivot_value = matrix[column][column];
    output = multiply(output, pivot_value);
    u32 inverse_pivot = power(pivot_value, P - 2);
    for (int row = column + 1; row < D; ++row) {{
      if (matrix[row][column] == 0) continue;
      u32 factor = multiply(matrix[row][column], inverse_pivot);
      for (int index = column; index < D; ++index) {{
        matrix[row][index] = subtract(
            matrix[row][index], multiply(factor, matrix[column][index]));
      }}
    }}
  }}
  return output;
}}

u32 evaluate(const std::vector<u32>& coefficients, u32 point) {{
  u32 output = 0;
  for (auto iterator = coefficients.rbegin(); iterator != coefficients.rend();
       ++iterator) output = add(multiply(output, point), *iterator);
  return output;
}}

u32 direct_matrix_determinant(u32 point) {{
  std::array<std::array<u32, D>, D> matrix{{}};
  for (int row = 0; row < D; ++row)
    for (int column = 0; column < D; ++column)
      matrix[row][column] = evaluate(COEFFICIENTS[row * D + column], point);
  return determinant(matrix);
}}

int main() {{
  assert(COEFFICIENTS.size() == D * D);
  assert(power(ROOT, N) == 1);
  assert(power(ROOT, N / 2) == P - 1);
  std::vector<std::vector<u32>> evaluations(D * D, std::vector<u32>(N, 0));
#pragma omp parallel for schedule(dynamic)
  for (int index = 0; index < D * D; ++index) {{
    std::copy(COEFFICIENTS[index].begin(), COEFFICIENTS[index].end(),
              evaluations[index].begin());
    ntt(evaluations[index], false);
  }}
  std::vector<u32> determinant_values(N, 0);
#pragma omp parallel for schedule(static)
  for (int point = 0; point < N; ++point) {{
    std::array<std::array<u32, D>, D> matrix{{}};
    for (int row = 0; row < D; ++row)
      for (int column = 0; column < D; ++column)
        matrix[row][column] = evaluations[row * D + column][point];
    determinant_values[point] = determinant(matrix);
  }}
  ntt(determinant_values, true);
  for (int degree = DEGREE_BOUND + 1; degree < N; ++degree)
    assert(determinant_values[degree] == 0);
  int degree = DEGREE_BOUND;
  while (degree > 0 && determinant_values[degree] == 0) --degree;
  assert(determinant_values[degree] != 0);
  int terms = 0;
  for (int index = 0; index <= degree; ++index)
    if (determinant_values[index] != 0) ++terms;
  u32 witness_direct = direct_matrix_determinant({WITNESS_T});
  u32 witness_polynomial = evaluate(determinant_values, {WITNESS_T});
  assert(witness_direct == {WITNESS_DETERMINANT}u);
  assert(witness_polynomial == witness_direct);
  u32 holdout_direct = direct_matrix_determinant({HOLDOUT_T});
  u32 holdout_polynomial = evaluate(determinant_values, {HOLDOUT_T});
  assert(holdout_polynomial == holdout_direct);
  std::cout << "NTT_PROFILE " << N << " " << ROOT << " "
            << DEGREE_BOUND << " " << omp_get_max_threads() << "\\n";
  std::cout << "WITNESS_COMPLETE {WITNESS_T} " << witness_direct << " "
            << "{HOLDOUT_T} " << holdout_direct << "\\n";
  std::cout << "DETERMINANT_COMPLETE " << degree << " " << terms << "\\n";
  std::ofstream output("/tmp/fff_r76_ntt_determinant.txt");
  for (int index = 0; index <= degree; ++index) {{
    if (index) output << ',';
    output << determinant_values[index];
  }}
  output << "\\n";
  output.close();
  std::cout << "R76_NTT_DETERMINANT_CERTIFIED\\n";
  return 0;
}}
"""
    return {
        "program": program,
        "relation": "exact NTT determinant of column-cleared FFF R76 matrix",
        "engine": "C++17 NTT plus finite-field Gaussian elimination",
        "coefficient_ring": f"GF({PRIME})[t]",
        "dimension": DIMENSION,
        "ntt_size": NTT_SIZE,
        "primitive_root": PRIMITIVE_ROOT,
        "ntt_root": NTT_ROOT,
        "degree_bound": DEGREE_BOUND,
        "source_column_lcms_sha256": row["column_lcms_sha256"],
        "source_matrix_entries_sha256": row["matrix_entries_sha256"],
        "witness_t": WITNESS_T,
        "expected_witness_determinant": WITNESS_DETERMINANT,
        "holdout_t": HOLDOUT_T,
        "roots_open": True,
    }


if __name__ == "__main__":
    require(PRIME - 1 == 127 * 2**24, "field smoothness")
    require(pow(PRIMITIVE_ROOT, (PRIME - 1) // 2, PRIME) != 1 and
            pow(PRIMITIVE_ROOT, (PRIME - 1) // 127, PRIME) != 1,
            "primitive root")
    require(pow(NTT_ROOT, NTT_SIZE, PRIME) == 1 and
            pow(NTT_ROOT, NTT_SIZE // 2, PRIME) == PRIME - 1,
            "NTT root")
    require(DEGREE_BOUND < NTT_SIZE, "reconstruction bound")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_NTT_DETERMINANT_"
          "PROGRAM_PASS ntt=32768 degree_bound=22208")
