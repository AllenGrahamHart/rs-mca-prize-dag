#include <stdio.h>

#ifndef P
#define P 29
#endif
#ifndef IOTA
#define IOTA 12
#endif

static int mod(long long value) {
    value %= P;
    return value < 0 ? (int)(value + P) : (int)value;
}

static int determinant4(int matrix[4][4]) {
    int total = 0;
    for (int a = 0; a < 4; ++a) {
        for (int b = 0; b < 4; ++b) {
            if (b == a) continue;
            for (int c = 0; c < 4; ++c) {
                if (c == a || c == b) continue;
                int d = 6-a-b-c;
                int permutation[4] = {a, b, c, d};
                int inversions = 0;
                for (int left = 0; left < 4; ++left)
                    for (int right = left+1; right < 4; ++right)
                        inversions += permutation[left] > permutation[right];
                long long term = 1;
                for (int row = 0; row < 4; ++row)
                    term = term*matrix[row][permutation[row]] % P;
                total = mod(total + (inversions % 2 ? -term : term));
            }
        }
    }
    return total;
}

static int distinct5(const int values[5]) {
    for (int left = 0; left < 5; ++left) {
        if (values[left] == 0) return 0;
        for (int right = left+1; right < 5; ++right)
            if (values[left] == values[right]) return 0;
    }
    return 1;
}

static int weld(
    const int labels[5], const int products[5], const int q_values[5],
    int third
) {
    int left = 1, right = 2;
    int dl = mod(products[0]-products[left]);
    int dr = mod(products[0]-products[right]);
    int dk = mod(products[0]-products[third]);
    long long value =
        (long long)q_values[left]*dr*dk*mod(labels[third]-labels[right])
        +(long long)q_values[right]*dl*dk*mod(labels[left]-labels[third])
        +(long long)q_values[third]*dl*dr*mod(labels[right]-labels[left]);
    return mod(value);
}

static int equation_rows(
    const int labels[5], const int products[5], int fourth
) {
    int indices[4] = {0, 1, 2, fourth};
    int matrix[4][4];
    for (int row = 0; row < 4; ++row) {
        int index = indices[row];
        matrix[row][0] = mod(-products[index]);
        matrix[row][1] = mod(-products[index]*labels[index]);
        matrix[row][2] = 1;
        matrix[row][3] = labels[index];
    }
    return determinant4(matrix);
}

static void cell_data(int cell, int *singleton, int matching[2][2]) {
    int rest[4], cursor = 0;
    *singleton = cell/3;
    int local = cell%3;
    for (int role = 0; role < 5; ++role)
        if (role != *singleton) rest[cursor++] = role;
    if (local == 0) {
        matching[0][0] = rest[0]; matching[0][1] = rest[1];
        matching[1][0] = rest[2]; matching[1][1] = rest[3];
    } else if (local == 1) {
        matching[0][0] = rest[0]; matching[0][1] = rest[2];
        matching[1][0] = rest[1]; matching[1][1] = rest[3];
    } else {
        matching[0][0] = rest[0]; matching[0][1] = rest[3];
        matching[1][0] = rest[1]; matching[1][1] = rest[2];
    }
}

int main(void) {
    if (mod(IOTA*IOTA) != P-1) return 2;
    for (int cell = 0; cell < 15; ++cell) {
        int singleton, matching[2][2];
        cell_data(cell, &singleton, matching);
        for (int epsilon_1 = -1; epsilon_1 <= 1; epsilon_1 += 2) {
            for (int epsilon_2 = -1; epsilon_2 <= 1; epsilon_2 += 2) {
                long long count = 0;
                int witness[4] = {0, 0, 0, 0};
                for (int b = 1; b < P; ++b) {
                    for (int c = 1; c < P; ++c) {
                        int products[5] = {
                            P-1, b, c, mod(b*c), mod(-b*c)
                        };
                        if (!distinct5(products)) continue;
                        for (int r = 1; r < P; ++r) {
                            for (int t = 1; t < P; ++t) {
                                int roots[5] = {0, 0, 0, 0, 0};
                                roots[matching[0][0]] = 1;
                                roots[matching[0][1]] = mod(epsilon_1*IOTA);
                                roots[matching[1][0]] = r;
                                roots[matching[1][1]] = mod(epsilon_2*IOTA*r);
                                roots[singleton] = t;
                                int labels[5];
                                for (int role = 0; role < 5; ++role)
                                    labels[role] = mod(roots[role]*roots[role]);
                                if (!distinct5(labels)) continue;
                                int sums[5] = {
                                    0, mod(1+b), mod(1+c), mod(b+c), mod(b-c)
                                };
                                int q_values[5];
                                for (int role = 0; role < 5; ++role)
                                    q_values[role] = mod(roots[role]*sums[role]);
                                if (equation_rows(labels, products, 3)
                                    || equation_rows(labels, products, 4)
                                    || weld(labels, products, q_values, 3)
                                    || weld(labels, products, q_values, 4))
                                    continue;
                                if (count == 0) {
                                    witness[0] = b; witness[1] = c;
                                    witness[2] = r; witness[3] = t;
                                }
                                ++count;
                            }
                        }
                    }
                }
                printf(
                    "cell=%d eps=%d,%d survivors=%lld witness=%d,%d,%d,%d\n",
                    cell, epsilon_1, epsilon_2, count,
                    witness[0], witness[1], witness[2], witness[3]
                );
                fflush(stdout);
            }
        }
    }
    return 0;
}
