#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COLS 8
#define MAX_ROWS 10

static int prime;
static int inverse_table[256];

static int mod_i64(int64_t value) {
    value %= prime;
    if (value < 0) value += prime;
    return (int)value;
}

static int mul(int left, int right) {
    return mod_i64((int64_t)left * right);
}

static int power(int value, int exponent) {
    int result = 1;
    while (exponent) {
        if (exponent & 1) result = mul(result, value);
        value = mul(value, value);
        exponent >>= 1;
    }
    return result;
}

static int rref(int rows, int matrix[MAX_ROWS][COLS], int pivots[COLS]) {
    int pivot_row = 0;
    memset(pivots, 0, COLS * sizeof(int));
    for (int column = 0; column < COLS && pivot_row < rows; ++column) {
        int selected = -1;
        for (int row = pivot_row; row < rows; ++row) {
            if (matrix[row][column] != 0) {
                selected = row;
                break;
            }
        }
        if (selected < 0) continue;
        if (selected != pivot_row) {
            for (int entry = 0; entry < COLS; ++entry) {
                int temporary = matrix[pivot_row][entry];
                matrix[pivot_row][entry] = matrix[selected][entry];
                matrix[selected][entry] = temporary;
            }
        }
        int scale = inverse_table[matrix[pivot_row][column]];
        for (int entry = column; entry < COLS; ++entry) {
            matrix[pivot_row][entry] = mul(matrix[pivot_row][entry], scale);
        }
        for (int row = 0; row < rows; ++row) {
            if (row == pivot_row || matrix[row][column] == 0) continue;
            scale = matrix[row][column];
            for (int entry = column; entry < COLS; ++entry) {
                matrix[row][entry] = mod_i64(
                    matrix[row][entry] - (int64_t)scale * matrix[pivot_row][entry]
                );
            }
        }
        pivots[column] = 1;
        ++pivot_row;
    }
    return pivot_row;
}

static int matrix_rank(int rows, const int input[MAX_ROWS][COLS]) {
    int matrix[MAX_ROWS][COLS];
    int pivots[COLS];
    memcpy(matrix, input, sizeof(matrix));
    return rref(rows, matrix, pivots);
}

static int leading_support_exists(
    int rows,
    const int input[MAX_ROWS][COLS],
    const int labels[5]
) {
    int matrix[MAX_ROWS][COLS];
    int pivots[COLS];
    int pivot_column_for_row[COLS];
    memcpy(matrix, input, sizeof(matrix));
    int rank = rref(rows, matrix, pivots);
    if (rank == COLS) return 0;

    int pivot_row = 0;
    for (int column = 0; column < COLS; ++column) {
        if (pivots[column]) pivot_column_for_row[pivot_row++] = column;
    }
    for (int label_index = 0; label_index < 5; ++label_index) {
        int label = labels[label_index];
        int label2 = mul(label, label);
        int functional_nonzero = 0;
        for (int free_column = 0; free_column < COLS; ++free_column) {
            if (pivots[free_column]) continue;
            int vector[COLS] = {0};
            vector[free_column] = 1;
            for (int row = 0; row < rank; ++row) {
                vector[pivot_column_for_row[row]] =
                    mod_i64(-matrix[row][free_column]);
            }
            int value = mod_i64(
                vector[0] + (int64_t)vector[1] * label
                + (int64_t)vector[2] * label2
            );
            if (value != 0) {
                functional_nonzero = 1;
                break;
            }
        }
        if (!functional_nonzero) return 0;
    }
    /* At most five proper hyperplanes cannot cover a vector space over p>5. */
    return 1;
}

static int unique_kernel_vector(
    int rows,
    const int input[MAX_ROWS][COLS],
    int vector[COLS]
) {
    int matrix[MAX_ROWS][COLS];
    int pivots[COLS];
    int pivot_column_for_row[COLS];
    memcpy(matrix, input, sizeof(matrix));
    int rank = rref(rows, matrix, pivots);
    if (rank != COLS - 1) return 0;
    int pivot_row = 0, free_column = -1;
    for (int column = 0; column < COLS; ++column) {
        if (pivots[column]) {
            pivot_column_for_row[pivot_row++] = column;
        } else {
            free_column = column;
        }
    }
    memset(vector, 0, COLS * sizeof(int));
    vector[free_column] = 1;
    for (int row = 0; row < rank; ++row) {
        vector[pivot_column_for_row[row]] = mod_i64(-matrix[row][free_column]);
    }
    return 1;
}

static int evaluate_quadratic(const int coefficients[3], int point) {
    return mod_i64(coefficients[0] + (int64_t)coefficients[1] * point
                   + (int64_t)coefficients[2] * mul(point, point));
}

static int same_antipodal_pair(int left, int right) {
    return left == right || left == mod_i64(-right);
}

static void build_product_pair_masks(
    const int kernel[COLS],
    const int common_labels[5],
    uint64_t *pair_masks
) {
    memset(pair_masks, 0, (size_t)prime * prime * sizeof(uint64_t));
    const int *denominator = kernel;
    const int *numerator = kernel + 3;
    int half = (prime - 1) / 2;
    for (int point = 1; point <= half; ++point) {
        int used = 0;
        for (int index = 0; index < 5; ++index) {
            if (same_antipodal_pair(point, common_labels[index])) {
                used = 1;
                break;
            }
        }
        if (used) continue;
        int opposite = mod_i64(-point);
        int denominator_left = evaluate_quadratic(denominator, point);
        int denominator_right = evaluate_quadratic(denominator, opposite);
        if (!denominator_left || !denominator_right) continue;
        int left = mul(evaluate_quadratic(numerator, point),
                       inverse_table[denominator_left]);
        int right = mul(evaluate_quadratic(numerator, opposite),
                        inverse_table[denominator_right]);
        uint64_t bit = UINT64_C(1) << (point - 1);
        pair_masks[left * prime + right] |= bit;
        pair_masks[right * prime + left] |= bit;
    }
}

static int pair_records_recursive(
    const int *values,
    int count,
    uint64_t used_source_pairs,
    const uint64_t *pair_masks
) {
    if (count == 0) return 1;
    int remaining[6];
    for (int partner = 1; partner < count; ++partner) {
        uint64_t available = pair_masks[values[0] * prime + values[partner]]
                             & ~used_source_pairs;
        if (!available) continue;
        int used = 0;
        for (int index = 1; index < count; ++index) {
            if (index != partner) remaining[used++] = values[index];
        }
        while (available) {
            uint64_t bit = available & (~available + 1);
            if (pair_records_recursive(remaining, count - 2,
                                       used_source_pairs | bit, pair_masks)) {
                return 1;
            }
            available ^= bit;
        }
    }
    return 0;
}

static int internal_sum_squared(
    int d,
    int e,
    int f,
    int cycle_sign,
    int eta_index
) {
    int sum;
    switch (eta_index) {
        case 0: sum = mod_i64(d + e); break;
        case 1: sum = mod_i64(d - e); break;
        case 2: sum = mod_i64(d + f); break;
        case 3: sum = mod_i64(d - f); break;
        default: sum = mod_i64(e + (int64_t)cycle_sign * f); break;
    }
    return mul(sum, sum);
}

static int missing_mate_sum_passes(
    const int kernel[COLS],
    int eta_label,
    int eta_denominator,
    int sum_squared
) {
    int b1 = mod_i64(kernel[6] + (int64_t)kernel[7] * eta_label);
    int left = mul(eta_label, mul(b1, b1));
    int right = mul(sum_squared, mul(eta_denominator, eta_denominator));
    return left == right;
}

static uint64_t outside_product_completions(
    int b,
    int c,
    int cycle_sign,
    int singleton_label,
    const int kernel[COLS],
    const int common_labels[5],
    uint64_t *pair_masks,
    uint64_t *sum_completions,
    int example[8],
    int sum_example[8]
) {
    const int *denominator = kernel;
    const int *numerator = kernel + 3;
    int eta_label = mod_i64(-singleton_label);
    int eta_denominator = evaluate_quadratic(denominator, eta_label);
    *sum_completions = 0;
    if (!eta_denominator) return 0;
    int mate = mul(evaluate_quadratic(numerator, eta_label),
                   inverse_table[eta_denominator]);
    build_product_pair_masks(kernel, common_labels, pair_masks);

    uint64_t completions = 0;
    for (int d = 1; d < prime; ++d) {
        if (same_antipodal_pair(d, 1) || same_antipodal_pair(d, b)
            || same_antipodal_pair(d, c)) continue;
        for (int e = 1; e < prime; ++e) {
            if (same_antipodal_pair(e, 1) || same_antipodal_pair(e, b)
                || same_antipodal_pair(e, c) || same_antipodal_pair(e, d)) continue;
            for (int f = 1; f < prime; ++f) {
                if (same_antipodal_pair(f, 1) || same_antipodal_pair(f, b)
                    || same_antipodal_pair(f, c) || same_antipodal_pair(f, d)
                    || same_antipodal_pair(f, e)) continue;
                int internal[5] = {
                    mul(d, e), mod_i64(-(int64_t)d * e),
                    mul(d, f), mod_i64(-(int64_t)d * f),
                    mod_i64((int64_t)cycle_sign * e * f),
                };
                int colored[2] = {mul(b, e), mul(c, f)};
                int passes = 0, passes_sum = 0;
                for (int eta_index = 0; eta_index < 5 && !passes_sum; ++eta_index) {
                    if (internal[eta_index] != mate) continue;
                    int records[6], used = 0;
                    for (int index = 0; index < 5; ++index) {
                        if (index != eta_index) records[used++] = internal[index];
                    }
                    records[used++] = colored[0];
                    records[used++] = colored[1];
                    if (pair_records_recursive(records, 6, 0, pair_masks)) {
                        passes = 1;
                        if (example[0] < 0) {
                            example[0] = b;
                            example[1] = c;
                            example[2] = d;
                            example[3] = e;
                            example[4] = f;
                            example[5] = mate;
                            example[6] = eta_index;
                            example[7] = cycle_sign;
                        }
                        if (missing_mate_sum_passes(
                                kernel, eta_label, eta_denominator,
                                internal_sum_squared(
                                    d, e, f, cycle_sign, eta_index))) {
                            passes_sum = 1;
                            if (sum_example[0] < 0) {
                                sum_example[0] = b;
                                sum_example[1] = c;
                                sum_example[2] = d;
                                sum_example[3] = e;
                                sum_example[4] = f;
                                sum_example[5] = mate;
                                sum_example[6] = eta_index;
                                sum_example[7] = cycle_sign;
                            }
                        }
                    }
                }
                if (passes) ++completions;
                if (passes_sum) ++*sum_completions;
            }
        }
    }
    return completions;
}

static void build_cells(int cells[15][5]) {
    int index = 0;
    for (int singleton = 0; singleton < 5; ++singleton) {
        int rest[4], used = 0;
        for (int value = 0; value < 5; ++value) {
            if (value != singleton) rest[used++] = value;
        }
        for (int partner = 1; partner < 4; ++partner) {
            int tail[2], tail_used = 0;
            for (int position = 1; position < 4; ++position) {
                if (position != partner) tail[tail_used++] = rest[position];
            }
            cells[index][0] = singleton;
            cells[index][1] = rest[0];
            cells[index][2] = rest[partner];
            cells[index][3] = tail[0];
            cells[index][4] = tail[1];
            ++index;
        }
    }
}

static int distinct_labels(const int labels[5]) {
    for (int left = 0; left < 5; ++left) {
        for (int right = left + 1; right < 5; ++right) {
            if (labels[left] == labels[right]) return 0;
        }
    }
    return 1;
}

static void product_row(int row[COLS], int label, int product) {
    int label2 = mul(label, label);
    row[0] = mod_i64(-product);
    row[1] = mod_i64(-(int64_t)product * label);
    row[2] = mod_i64(-(int64_t)product * label2);
    row[3] = 1;
    row[4] = label;
    row[5] = label2;
    row[6] = 0;
    row[7] = 0;
}

static void sum_row(int row[COLS], int label, int q_value) {
    int label2 = mul(label, label);
    row[0] = q_value;
    row[1] = mul(q_value, label);
    row[2] = mul(q_value, label2);
    row[3] = 0;
    row[4] = 0;
    row[5] = 0;
    row[6] = label;
    row[7] = label2;
}

int main(int argc, char **argv) {
    if (argc != 5 && argc != 6) {
        fprintf(stderr, "usage: %s PRIME CELL EPSILON1 EPSILON2 [CYCLE_SIGN]\n", argv[0]);
        return 2;
    }
    prime = atoi(argv[1]);
    int cell_index = atoi(argv[2]);
    int epsilon1 = atoi(argv[3]);
    int epsilon2 = atoi(argv[4]);
    int outside_mode = argc == 6;
    int cycle_sign = outside_mode ? atoi(argv[5]) : 0;
    if (prime >= 256 || prime <= 5 || (prime - 1) / 2 > 64
        || cell_index < 0 || cell_index >= 15) return 2;
    for (int value = 1; value < prime; ++value) {
        inverse_table[value] = power(value, prime - 2);
    }
    int iota = 0;
    for (int value = 1; value < prime; ++value) {
        if (mul(value, value) == prime - 1) {
            iota = value;
            break;
        }
    }
    if (!iota) {
        fprintf(stderr, "-1 is not a square\n");
        return 2;
    }

    int cells[15][5];
    build_cells(cells);
    uint64_t admissible = 0, base_rank_six = 0, rank_survivors = 0;
    uint64_t support_survivors = 0, zero_branch = 0;
    uint64_t pivot_counts[4] = {0, 0, 0, 0};
    uint64_t rank_histogram[9] = {0};
    uint64_t outside_nonunique_kernel = 0;
    uint64_t common_points_with_outside = 0;
    uint64_t outside_target_completions = 0;
    uint64_t common_points_with_mate_sum = 0;
    uint64_t outside_mate_sum_target_completions = 0;
    int outside_example[8] = {-1, -1, -1, -1, -1, -1, -1, -1};
    int mate_sum_example[8] = {-1, -1, -1, -1, -1, -1, -1, -1};
    uint64_t *pair_masks = outside_mode
        ? calloc((size_t)prime * prime, sizeof(uint64_t)) : NULL;
    if (outside_mode && !pair_masks) return 3;

    for (int b = 1; b < prime; ++b) {
        if (b == 1 || b == prime - 1) continue;
        for (int c = 1; c < prime; ++c) {
            if (c == 1 || c == prime - 1 || c == b || c == prime - b) continue;
            for (int r = 1; r < prime; ++r) {
                for (int t = 1; t < prime; ++t) {
                    int roots[5] = {0};
                    roots[cells[cell_index][1]] = 1;
                    roots[cells[cell_index][2]] = mod_i64((int64_t)epsilon1 * iota);
                    roots[cells[cell_index][3]] = r;
                    roots[cells[cell_index][4]] = mod_i64((int64_t)epsilon2 * iota * r);
                    roots[cells[cell_index][0]] = t;
                    int labels[5];
                    for (int role = 0; role < 5; ++role) labels[role] = mul(roots[role], roots[role]);
                    if (!distinct_labels(labels)) continue;
                    ++admissible;

                    int products[5] = {
                        mod_i64(-(int64_t)c * c), b, b, prime - b, c
                    };
                    int sums[5] = {
                        0, mod_i64(1 + b), mod_i64(1 + b),
                        mod_i64(1 - b), mod_i64(1 + c)
                    };
                    int matrix[MAX_ROWS][COLS] = {{0}};
                    for (int role = 0; role < 5; ++role) {
                        product_row(matrix[role], labels[role], products[role]);
                        int q_value = mul(roots[role], sums[role]);
                        sum_row(matrix[5 + role], labels[role], q_value);
                    }
                    int base[MAX_ROWS][COLS] = {{0}};
                    for (int role = 0; role < 5; ++role) {
                        memcpy(base[role], matrix[role], COLS * sizeof(int));
                    }
                    memcpy(base[5], matrix[5], COLS * sizeof(int));
                    if (matrix_rank(6, base) != 6) continue;
                    ++base_rank_six;
                    int full_rank = matrix_rank(10, matrix);
                    if (full_rank >= 0 && full_rank <= 8) ++rank_histogram[full_rank];
                    if (full_rank > 7) continue;
                    ++rank_survivors;
                    if (!leading_support_exists(10, matrix, labels)) continue;
                    ++support_survivors;

                    int pivot_mask = 0;
                    for (int role = 1; role < 5; ++role) {
                        int augmented[MAX_ROWS][COLS] = {{0}};
                        for (int row = 0; row < 6; ++row) {
                            memcpy(augmented[row], base[row], COLS * sizeof(int));
                        }
                        memcpy(augmented[6], matrix[5 + role], COLS * sizeof(int));
                        if (matrix_rank(7, augmented) == 7) {
                            ++pivot_counts[role - 1];
                            pivot_mask |= 1 << (role - 1);
                        }
                    }
                    if (!pivot_mask) ++zero_branch;
                    if (outside_mode) {
                        int kernel[COLS];
                        if (!unique_kernel_vector(10, matrix, kernel)) {
                            ++outside_nonunique_kernel;
                        } else {
                            uint64_t sum_completions = 0;
                            uint64_t completions = outside_product_completions(
                                b, c, cycle_sign,
                                labels[cells[cell_index][0]],
                                kernel, labels, pair_masks, &sum_completions,
                                outside_example, mate_sum_example
                            );
                            outside_target_completions += completions;
                            if (completions) ++common_points_with_outside;
                            outside_mate_sum_target_completions += sum_completions;
                            if (sum_completions) ++common_points_with_mate_sum;
                        }
                    }
                }
            }
        }
    }

    printf(
        "{\"prime\":%d,\"cell\":%d,\"epsilon\":[%d,%d],"
        "\"iota\":%d,\"admissible\":%llu,\"base_rank_six\":%llu,"
        "\"rank_survivors\":%llu,\"support_survivors\":%llu,"
        "\"zero_branch\":%llu,\"pivot_counts\":[%llu,%llu,%llu,%llu],"
        "\"outside_mode\":%d,\"cycle_sign\":%d,"
        "\"outside_nonunique_kernel\":%llu,"
        "\"common_points_with_outside\":%llu,"
        "\"outside_target_completions\":%llu,"
        "\"outside_example\":[%d,%d,%d,%d,%d,%d,%d,%d],"
        "\"common_points_with_mate_sum\":%llu,"
        "\"outside_mate_sum_target_completions\":%llu,"
        "\"mate_sum_example\":[%d,%d,%d,%d,%d,%d,%d,%d],"
        "\"rank_histogram\":[%llu,%llu,%llu,%llu,%llu,%llu,%llu,%llu,%llu]}\n",
        prime, cell_index, epsilon1, epsilon2, iota,
        (unsigned long long)admissible,
        (unsigned long long)base_rank_six,
        (unsigned long long)rank_survivors,
        (unsigned long long)support_survivors,
        (unsigned long long)zero_branch,
        (unsigned long long)pivot_counts[0],
        (unsigned long long)pivot_counts[1],
        (unsigned long long)pivot_counts[2],
        (unsigned long long)pivot_counts[3],
        outside_mode,
        cycle_sign,
        (unsigned long long)outside_nonunique_kernel,
        (unsigned long long)common_points_with_outside,
        (unsigned long long)outside_target_completions,
        outside_example[0], outside_example[1], outside_example[2],
        outside_example[3], outside_example[4], outside_example[5],
        outside_example[6], outside_example[7],
        (unsigned long long)common_points_with_mate_sum,
        (unsigned long long)outside_mate_sum_target_completions,
        mate_sum_example[0], mate_sum_example[1], mate_sum_example[2],
        mate_sum_example[3], mate_sum_example[4], mate_sum_example[5],
        mate_sum_example[6], mate_sum_example[7],
        (unsigned long long)rank_histogram[0],
        (unsigned long long)rank_histogram[1],
        (unsigned long long)rank_histogram[2],
        (unsigned long long)rank_histogram[3],
        (unsigned long long)rank_histogram[4],
        (unsigned long long)rank_histogram[5],
        (unsigned long long)rank_histogram[6],
        (unsigned long long)rank_histogram[7],
        (unsigned long long)rank_histogram[8]
    );
    free(pair_masks);
    return 0;
}
