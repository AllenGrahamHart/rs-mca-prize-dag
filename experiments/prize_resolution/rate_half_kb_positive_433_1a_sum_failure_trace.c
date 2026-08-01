#define main positive_433_1a_original_main
#include "rate_half_kb_positive_433_1a_common_chart_probe.c"
#undef main

typedef struct {
    uint64_t assignment_histogram[7];
    uint64_t assignment_count;
    int best;
    int best_mask;
    int best_sources[7];
} SumTrace;

static int type_a_sum_cut(
    const int kernel[COLS],
    int xi_label,
    int label
) {
    int opposite = mod_i64(-label);
    int dw = evaluate_quadratic(kernel, label);
    int nw = evaluate_quadratic(kernel + 3, label);
    int dm = evaluate_quadratic(kernel, opposite);
    int nm = evaluate_quadratic(kernel + 3, opposite);
    int dx = evaluate_quadratic(kernel, xi_label);
    int nx = evaluate_quadratic(kernel + 3, xi_label);
    if (!dw || !dm || !dx || !nw || !nm || !nx) return -1;
    int bw = mod_i64(kernel[6] + (int64_t)kernel[7] * label);
    int cross = mod_i64((int64_t)nm * dx - (int64_t)nx * dm);
    int first = mul(label, mul(mul(bw, bw), mul(mul(nx, nm), mul(dx, dm))));
    int second = mul(mul(nw, dw), mul(cross, cross));
    return mod_i64(first + second);
}

static void trace_pair_sums(
    const int *values,
    const int *sums,
    const int *record_ids,
    int count,
    uint64_t used_source_pairs,
    const uint64_t *pair_masks,
    const int kernel[COLS],
    int pass_mask,
    int sources[7],
    SumTrace *trace
) {
    if (count == 0) {
        int passed = __builtin_popcount((unsigned int)pass_mask);
        ++trace->assignment_count;
        ++trace->assignment_histogram[passed];
        if (passed > trace->best) {
            trace->best = passed;
            trace->best_mask = pass_mask;
            memcpy(trace->best_sources, sources, sizeof(trace->best_sources));
        }
        return;
    }
    int remaining_values[6], remaining_sums[6], remaining_ids[6];
    for (int partner = 1; partner < count; ++partner) {
        uint64_t available = pair_masks[values[0] * prime + values[partner]]
                             & ~used_source_pairs;
        if (!available) continue;
        int used = 0;
        for (int index = 1; index < count; ++index) {
            if (index == partner) continue;
            remaining_values[used] = values[index];
            remaining_sums[used] = sums[index];
            remaining_ids[used++] = record_ids[index];
        }
        while (available) {
            uint64_t bit = available & (~available + 1);
            int point = __builtin_ctzll(bit) + 1;
            int opposite = mod_i64(-point);
            int left_product = product_at_source(kernel, point);
            int right_product = product_at_source(kernel, opposite);
            int point_denominator = evaluate_quadratic(kernel, point);
            int opposite_denominator = evaluate_quadratic(kernel, opposite);
            int orientation[2][2] = {
                {0, partner}, {partner, 0}
            };
            for (int direction = 0; direction < 2; ++direction) {
                int left = orientation[direction][0];
                int right = orientation[direction][1];
                if (left_product != values[left]
                    || right_product != values[right]) continue;
                sources[record_ids[left]] = point;
                sources[record_ids[right]] = opposite;
                int next_mask = pass_mask;
                if (source_sum_squared_passes(
                        kernel, point, point_denominator, sums[left])) {
                    next_mask |= 1 << record_ids[left];
                }
                if (source_sum_squared_passes(
                        kernel, opposite, opposite_denominator, sums[right])) {
                    next_mask |= 1 << record_ids[right];
                }
                trace_pair_sums(
                    remaining_values, remaining_sums, remaining_ids, count - 2,
                    used_source_pairs | bit, pair_masks, kernel, next_mask,
                    sources, trace
                );
            }
            available ^= bit;
        }
    }
}

static void trace_outside(
    int b,
    int c,
    int cycle_sign,
    int alignment,
    int singleton_label,
    const int kernel[COLS],
    const int common_labels[5],
    uint64_t *pair_masks,
    uint64_t target_best_histogram[7],
    uint64_t *target_triples,
    uint64_t assignment_histogram[7],
    uint64_t *assignment_count,
    int example[12],
    int example_outside[7],
    int example_sums[7],
    int example_sources[7],
    int example_residuals[7],
    int *global_best
) {
    int xi_label = mod_i64(-singleton_label);
    int xi_denominator = evaluate_quadratic(kernel, xi_label);
    if (!xi_denominator) return;
    int mate = product_at_source(kernel, xi_label);
    build_product_pair_masks(kernel, common_labels, pair_masks);

    for (int d = 1; d < prime; ++d) {
        if (same_antipodal_pair(d, 1) || same_antipodal_pair(d, b)
            || same_antipodal_pair(d, c)) continue;
        for (int e = 1; e < prime; ++e) {
            if (same_antipodal_pair(e, 1) || same_antipodal_pair(e, b)
                || same_antipodal_pair(e, c)
                || same_antipodal_pair(e, d)) continue;
            for (int f = 1; f < prime; ++f) {
                if (same_antipodal_pair(f, 1)
                    || same_antipodal_pair(f, b)
                    || same_antipodal_pair(f, c)
                    || same_antipodal_pair(f, d)
                    || same_antipodal_pair(f, e)) continue;
                int outside[7] = {
                    mul(d, e), mod_i64(-(int64_t)d * e),
                    mul(d, f), mod_i64(-(int64_t)d * f),
                    mod_i64((int64_t)cycle_sign * e * f),
                    mul(b, e), mul(c, f),
                };
                int sum_squared[7] = {
                    internal_sum_squared(d, e, f, cycle_sign, 0),
                    internal_sum_squared(d, e, f, cycle_sign, 1),
                    internal_sum_squared(d, e, f, cycle_sign, 2),
                    internal_sum_squared(d, e, f, cycle_sign, 3),
                    internal_sum_squared(d, e, f, cycle_sign, 4),
                    mul(mod_i64(b + e), mod_i64(b + e)),
                    mul(mod_i64(c + f), mod_i64(c + f)),
                };
                int triple_best = -1;
                int triple_xi = -1;
                int triple_sources[7] = {0};
                for (int xi_index = 0; xi_index < 7; ++xi_index) {
                    if (outside[xi_index] != mate) continue;
                    if (alignment == 0 && xi_index >= 5) continue;
                    if (!source_sum_squared_passes(
                            kernel, xi_label, xi_denominator,
                            sum_squared[xi_index])) continue;
                    int records[6], sums[6], ids[6], used = 0;
                    for (int index = 0; index < 7; ++index) {
                        if (index == xi_index) continue;
                        records[used] = outside[index];
                        sums[used] = sum_squared[index];
                        ids[used++] = index;
                    }
                    if (!pair_records_recursive(records, 6, 0, pair_masks)) {
                        continue;
                    }
                    SumTrace trace = {{0}, 0, -1, 0, {0}};
                    int sources[7] = {0};
                    trace_pair_sums(
                        records, sums, ids, 6, 0, pair_masks, kernel, 0,
                        sources, &trace
                    );
                    for (int passed = 0; passed <= 6; ++passed) {
                        assignment_histogram[passed]
                            += trace.assignment_histogram[passed];
                    }
                    *assignment_count += trace.assignment_count;
                    if (trace.best > triple_best) {
                        triple_best = trace.best;
                        triple_xi = xi_index;
                        memcpy(triple_sources, trace.best_sources,
                               sizeof(triple_sources));
                        triple_sources[xi_index] = xi_label;
                    }
                    if (trace.best > *global_best) {
                        *global_best = trace.best;
                        int eta_index = alignment == 0
                            ? xi_index : (xi_index == 0 ? 1 : 0);
                        int values[12] = {
                            b, c, d, e, f, mate, eta_index, xi_index,
                            cycle_sign, alignment, trace.best, trace.best_mask,
                        };
                        memcpy(example, values, sizeof(values));
                        memcpy(example_outside, outside, 7 * sizeof(int));
                        memcpy(example_sums, sum_squared, 7 * sizeof(int));
                        memcpy(example_sources, trace.best_sources,
                               7 * sizeof(int));
                        example_sources[xi_index] = xi_label;
                        for (int index = 0; index < 7; ++index) {
                            int label = example_sources[index];
                            int denominator = evaluate_quadratic(kernel, label);
                            int b1 = mod_i64(kernel[6]
                                           + (int64_t)kernel[7] * label);
                            example_residuals[index] = mod_i64(
                                (int64_t)label * mul(b1, b1)
                                - (int64_t)sum_squared[index]
                                  * mul(denominator, denominator)
                            );
                        }
                    }
                }
                if (triple_best >= 0) {
                    ++*target_triples;
                    ++target_best_histogram[triple_best];
                    fprintf(stderr,
                            "TRACE b=%d c=%d d=%d e=%d f=%d mate=%d xi=%d "
                            "best=%d sources=%d,%d,%d,%d,%d,%d,%d\n",
                            b, c, d, e, f, mate, triple_xi, triple_best,
                            triple_sources[0], triple_sources[1],
                            triple_sources[2], triple_sources[3],
                            triple_sources[4], triple_sources[5],
                            triple_sources[6]);
                }
            }
        }
    }
}

int main(int argc, char **argv) {
    if (argc != 7) {
        fprintf(stderr,
                "usage: %s PRIME CELL EPSILON1 EPSILON2 CYCLE_SIGN ALIGNMENT\n",
                argv[0]);
        return 2;
    }
    prime = atoi(argv[1]);
    int cell_index = atoi(argv[2]);
    int epsilon1 = atoi(argv[3]);
    int epsilon2 = atoi(argv[4]);
    int cycle_sign = atoi(argv[5]);
    int alignment = atoi(argv[6]);
    if (prime >= 256 || prime <= 5 || cell_index < 0 || cell_index >= 15
        || (alignment != 0 && alignment != 1)) return 2;
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
    if (!iota) return 2;

    int cells[15][5];
    build_cells(cells);
    uint64_t target_best_histogram[7] = {0};
    uint64_t assignment_histogram[7] = {0};
    uint64_t target_triples = 0, assignment_count = 0;
    uint64_t type_a_common_points = 0, type_a_roots = 0;
    int type_a_example[5] = {-1, -1, -1, -1, -1};
    int example[12];
    for (int index = 0; index < 12; ++index) example[index] = -1;
    int example_outside[7], example_sums[7], example_sources[7];
    int example_residuals[7];
    for (int index = 0; index < 7; ++index) {
        example_outside[index] = example_sums[index] = -1;
        example_sources[index] = example_residuals[index] = -1;
    }
    int global_best = -1;
    uint64_t *pair_masks = calloc((size_t)prime * prime, sizeof(uint64_t));
    if (!pair_masks) return 3;

    for (int b = 1; b < prime; ++b) {
        if (b == 1 || b == prime - 1) continue;
        for (int c = 1; c < prime; ++c) {
            if (c == 1 || c == prime - 1 || c == b || c == prime - b) continue;
            for (int r = 1; r < prime; ++r) {
                for (int t = 1; t < prime; ++t) {
                    int roots[5] = {0};
                    roots[cells[cell_index][1]] = 1;
                    roots[cells[cell_index][2]]
                        = mod_i64((int64_t)epsilon1 * iota);
                    roots[cells[cell_index][3]] = r;
                    roots[cells[cell_index][4]]
                        = mod_i64((int64_t)epsilon2 * iota * r);
                    roots[cells[cell_index][0]] = t;
                    int labels[5];
                    for (int role = 0; role < 5; ++role) {
                        labels[role] = mul(roots[role], roots[role]);
                    }
                    if (!distinct_labels(labels)) continue;
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
                        sum_row(matrix[5 + role], labels[role],
                                mul(roots[role], sums[role]));
                    }
                    if (matrix_rank(10, matrix) > 7
                        || !leading_support_exists(10, matrix, labels)) continue;
                    int kernel[COLS];
                    if (!unique_kernel_vector(10, matrix, kernel)) continue;
                    int point_has_type_a_root = 0;
                    int xi_label = mod_i64(-labels[cells[cell_index][0]]);
                    for (int label = 1; label < prime; ++label) {
                        int excluded = 0;
                        for (int role = 0; role < 5; ++role) {
                            if (same_antipodal_pair(label, labels[role])) {
                                excluded = 1;
                                break;
                            }
                        }
                        if (excluded) continue;
                        if (type_a_sum_cut(kernel, xi_label, label) == 0) {
                            ++type_a_roots;
                            point_has_type_a_root = 1;
                            if (type_a_example[0] < 0) {
                                type_a_example[0] = b;
                                type_a_example[1] = c;
                                type_a_example[2] = r;
                                type_a_example[3] = t;
                                type_a_example[4] = label;
                            }
                        }
                    }
                    if (point_has_type_a_root) ++type_a_common_points;
                    trace_outside(
                        b, c, cycle_sign, alignment,
                        labels[cells[cell_index][0]], kernel, labels,
                        pair_masks, target_best_histogram, &target_triples,
                        assignment_histogram, &assignment_count, example,
                        example_outside, example_sums, example_sources,
                        example_residuals, &global_best
                    );
                }
            }
        }
    }
    printf(
        "{\"prime\":%d,\"cell\":%d,\"epsilon\":[%d,%d],"
        "\"cycle_sign\":%d,\"alignment\":%d,"
        "\"target_triples\":%llu,"
        "\"target_best_histogram\":[%llu,%llu,%llu,%llu,%llu,%llu,%llu],"
        "\"assignment_count\":%llu,"
        "\"assignment_pass_histogram\":[%llu,%llu,%llu,%llu,%llu,%llu,%llu],"
        "\"global_best\":%d,"
        "\"type_a_common_points\":%llu,\"type_a_roots\":%llu,"
        "\"type_a_example\":[%d,%d,%d,%d,%d],"
        "\"example\":[%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d],"
        "\"outside\":[%d,%d,%d,%d,%d,%d,%d],"
        "\"sum_squared\":[%d,%d,%d,%d,%d,%d,%d],"
        "\"source_labels\":[%d,%d,%d,%d,%d,%d,%d],"
        "\"sum_residuals\":[%d,%d,%d,%d,%d,%d,%d]}\n",
        prime, cell_index, epsilon1, epsilon2, cycle_sign, alignment,
        (unsigned long long)target_triples,
        (unsigned long long)target_best_histogram[0],
        (unsigned long long)target_best_histogram[1],
        (unsigned long long)target_best_histogram[2],
        (unsigned long long)target_best_histogram[3],
        (unsigned long long)target_best_histogram[4],
        (unsigned long long)target_best_histogram[5],
        (unsigned long long)target_best_histogram[6],
        (unsigned long long)assignment_count,
        (unsigned long long)assignment_histogram[0],
        (unsigned long long)assignment_histogram[1],
        (unsigned long long)assignment_histogram[2],
        (unsigned long long)assignment_histogram[3],
        (unsigned long long)assignment_histogram[4],
        (unsigned long long)assignment_histogram[5],
        (unsigned long long)assignment_histogram[6],
        global_best,
        (unsigned long long)type_a_common_points,
        (unsigned long long)type_a_roots,
        type_a_example[0], type_a_example[1], type_a_example[2],
        type_a_example[3], type_a_example[4],
        example[0], example[1], example[2], example[3], example[4],
        example[5], example[6], example[7], example[8], example[9],
        example[10], example[11],
        example_outside[0], example_outside[1], example_outside[2],
        example_outside[3], example_outside[4], example_outside[5],
        example_outside[6],
        example_sums[0], example_sums[1], example_sums[2], example_sums[3],
        example_sums[4], example_sums[5], example_sums[6],
        example_sources[0], example_sources[1], example_sources[2],
        example_sources[3], example_sources[4], example_sources[5],
        example_sources[6],
        example_residuals[0], example_residuals[1], example_residuals[2],
        example_residuals[3], example_residuals[4], example_residuals[5],
        example_residuals[6]
    );
    free(pair_masks);
    return 0;
}
