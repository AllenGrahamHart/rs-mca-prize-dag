#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef int64_t i64;

static const int CELLS[15][5] = {
    {0,1,2,3,4}, {0,1,3,2,4}, {0,1,4,2,3},
    {1,0,2,3,4}, {1,0,3,2,4}, {1,0,4,2,3},
    {2,0,1,3,4}, {2,0,3,1,4}, {2,0,4,1,3},
    {3,0,1,2,4}, {3,0,2,1,4}, {3,0,4,1,2},
    {4,0,1,2,3}, {4,0,2,1,3}, {4,0,3,1,2},
};

static i64 mod(i64 value, i64 prime) {
    value %= prime;
    return value < 0 ? value + prime : value;
}

static i64 det3(i64 matrix[3][3], i64 prime) {
    i64 value =
        matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        - matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
        + matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]);
    return mod(value, prime);
}

static void kernel3x4(i64 rows[5][4], i64 kernel[4], i64 prime) {
    for (int omitted = 0; omitted < 4; ++omitted) {
        i64 minor[3][3];
        for (int row = 0; row < 3; ++row) {
            int target = 0;
            for (int column = 0; column < 4; ++column) {
                if (column != omitted) {
                    minor[row][target++] = rows[row][column];
                }
            }
        }
        kernel[omitted] = det3(minor, prime);
        if (omitted & 1) {
            kernel[omitted] = mod(-kernel[omitted], prime);
        }
    }
}

static i64 dot4(const i64 left[4], const i64 right[4], i64 prime) {
    i64 value = 0;
    for (int index = 0; index < 4; ++index) {
        value = mod(value + left[index]*right[index], prime);
    }
    return value;
}

static int distinct5(const i64 values[5]) {
    for (int left = 0; left < 5; ++left) {
        for (int right = left+1; right < 5; ++right) {
            if (values[left] == values[right]) {
                return 0;
            }
        }
    }
    return 1;
}

static int survives(int cell, int epsilon1, int epsilon2,
                    i64 b, i64 c, i64 r, i64 t, i64 iota, i64 prime) {
    i64 products[5] = {b, mod(-b,prime), c, mod(-c,prime), mod(b*c,prime)};
    if (!distinct5(products)) {
        return 0;
    }
    i64 sums[5] = {
        mod(1+b,prime), mod(1-b,prime), mod(1+c,prime),
        mod(1-c,prime), mod(b+c,prime)
    };
    for (int index = 0; index < 5; ++index) {
        if (!sums[index]) {
            return 0;
        }
    }

    const int *description = CELLS[cell];
    i64 roots[5] = {0,0,0,0,0};
    roots[description[1]] = 1;
    roots[description[2]] = mod(epsilon1*iota, prime);
    roots[description[3]] = r;
    roots[description[4]] = mod(epsilon2*iota*r, prime);
    roots[description[0]] = t;
    i64 labels[5], qvalues[5];
    for (int index = 0; index < 5; ++index) {
        labels[index] = mod(roots[index]*roots[index], prime);
        qvalues[index] = mod(roots[index]*sums[index], prime);
    }
    if (!distinct5(labels)) {
        return 0;
    }

    i64 product_rows[5][4];
    for (int index = 0; index < 5; ++index) {
        product_rows[index][0] = mod(-products[index], prime);
        product_rows[index][1] = mod(-products[index]*labels[index], prime);
        product_rows[index][2] = 1;
        product_rows[index][3] = labels[index];
    }
    i64 kernel[4];
    kernel3x4(product_rows, kernel, prime);
    if ((!kernel[0] && !kernel[1]) ||
        dot4(product_rows[3], kernel, prime) ||
        dot4(product_rows[4], kernel, prime)) {
        return 0;
    }

    i64 q_rows[5][4];
    for (int index = 0; index < 5; ++index) {
        i64 denominator = mod(kernel[0] + kernel[1]*labels[index], prime);
        if (!denominator) {
            return 0;
        }
        q_rows[index][0] = 1;
        q_rows[index][1] = labels[index];
        q_rows[index][2] = mod(labels[index]*labels[index], prime);
        q_rows[index][3] = mod(qvalues[index]*denominator, prime);
    }
    i64 q_kernel[4];
    kernel3x4(q_rows, q_kernel, prime);
    return !dot4(q_rows[3], q_kernel, prime) &&
           !dot4(q_rows[4], q_kernel, prime);
}

int main(int argc, char **argv) {
    i64 prime = argc == 2 ? strtoll(argv[1], NULL, 10) : 29;
    i64 iota = 0;
    for (i64 value = 1; value < prime; ++value) {
        if (mod(value*value, prime) == prime-1) {
            iota = value;
            break;
        }
    }
    if (!iota) {
        fprintf(stderr, "prime must contain a square root of -1\n");
        return 2;
    }
    for (int cell = 0; cell < 15; ++cell) {
        for (int epsilon1 = -1; epsilon1 <= 1; epsilon1 += 2) {
            for (int epsilon2 = -1; epsilon2 <= 1; epsilon2 += 2) {
                i64 count = 0, witness[4] = {0,0,0,0};
                for (i64 b = 1; b < prime; ++b) {
                    for (i64 c = 1; c < prime; ++c) {
                        for (i64 r = 1; r < prime; ++r) {
                            for (i64 t = 1; t < prime; ++t) {
                                if (survives(cell, epsilon1, epsilon2,
                                             b,c,r,t,iota,prime)) {
                                    if (!count) {
                                        witness[0]=b; witness[1]=c;
                                        witness[2]=r; witness[3]=t;
                                    }
                                    ++count;
                                }
                            }
                        }
                    }
                }
                printf("prime=%lld cell=%d eps=%d,%d count=%lld",
                       (long long)prime, cell, epsilon1, epsilon2,
                       (long long)count);
                if (count) {
                    printf(" witness=%lld,%lld,%lld,%lld",
                           (long long)witness[0], (long long)witness[1],
                           (long long)witness[2], (long long)witness[3]);
                }
                putchar('\n');
            }
        }
    }
    return 0;
}
