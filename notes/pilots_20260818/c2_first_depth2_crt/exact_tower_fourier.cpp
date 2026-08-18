#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

#include <omp.h>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static u64 mul_mod(u64 a, u64 b, u64 mod) {
  return static_cast<u64>(static_cast<u128>(a) * b % mod);
}

static u64 add_mod(u64 a, u64 b, u64 mod) {
  return static_cast<u64>((static_cast<u128>(a) + b) % mod);
}

static u64 pow_mod(u64 a, u64 e, u64 mod) {
  u64 out = 1;
  while (e) {
    if (e & 1) out = mul_mod(out, a, mod);
    a = mul_mod(a, a, mod);
    e >>= 1;
  }
  return out;
}

static std::vector<u64> factors(u64 value) {
  std::vector<u64> out;
  for (u64 p = 2; p * p <= value; ++p) {
    if (value % p) continue;
    out.push_back(p);
    while (value % p == 0) value /= p;
  }
  if (value > 1) out.push_back(value);
  return out;
}

static u64 primitive_root(u64 q) {
  const auto primes = factors(q - 1);
  for (u64 g = 2; g < q; ++g) {
    bool good = true;
    for (u64 p : primes) {
      if (pow_mod(g, (q - 1) / p, q) == 1) {
        good = false;
        break;
      }
    }
    if (good) return g;
  }
  throw std::runtime_error("primitive root missing");
}

static std::vector<u64> coset_representatives(u64 multiplier, u64 q) {
  std::vector<std::uint8_t> seen(q, 0);
  std::vector<u64> reps;
  for (u64 value = 1; value < q; ++value) {
    if (seen[value]) continue;
    u64 current = value;
    u64 least = value;
    do {
      seen[current] = 1;
      least = std::min(least, current);
      current = current * multiplier % q;
    } while (current != value);
    reps.push_back(least);
  }
  std::sort(reps.begin(), reps.end());
  return reps;
}

struct Context {
  u64 n;
  u64 t;
  u64 q;
  u64 mod;
  u64 zeta;
  u64 inv_q;
  std::vector<u64> character;
};

static u64 inverse_power_q(const Context& ctx, u64 dimension) {
  return pow_mod(ctx.inv_q, dimension, ctx.mod);
}

static u64 level_zero_orbit_count(const Context& ctx) {
  const u64 n = ctx.n;
  const u64 T = ctx.t;
  if (T == 0 || T > 4) throw std::runtime_error("unsupported level-zero dimension");

  std::array<std::vector<std::vector<std::uint16_t>>, 4> contribution;
  std::array<u64, 4> multiplier{};
  for (u64 r = 1; r <= T; ++r) {
    multiplier[r - 1] = pow_mod(ctx.zeta, r, ctx.q);
    contribution[r - 1].assign(n, std::vector<std::uint16_t>(ctx.q));
    u64 root = 1;
    const u64 step = multiplier[r - 1];
    for (u64 i = 0; i < n; ++i) {
      for (u64 a = 0; a < ctx.q; ++a) {
        contribution[r - 1][i][a] = static_cast<std::uint16_t>(a * root % ctx.q);
      }
      root = root * step % ctx.q;
    }
  }
  std::vector<u64> factor(ctx.q);
  for (u64 phase = 0; phase < ctx.q; ++phase) {
    factor[phase] = add_mod(1, ctx.character[phase], ctx.mod);
  }

  u64 fourier = pow_mod(2, n, ctx.mod);  // zero dual tuple
  for (u64 first = 1; first <= T; ++first) {
    const auto reps = coset_representatives(multiplier[first - 1], ctx.q);
    u64 tail_size = 1;
    for (u64 r = first + 1; r <= T; ++r) tail_size *= ctx.q;
    const u64 total = reps.size() * tail_size;
    const u64 orbit_weight = n / std::gcd(n, first);
    u64 case_sum = 0;

#pragma omp parallel
    {
      u64 local = 0;
#pragma omp for schedule(static)
      for (std::int64_t flat = 0; flat < static_cast<std::int64_t>(total); ++flat) {
        std::array<u64, 4> coefficient{};
        u64 encoded = static_cast<u64>(flat);
        const u64 rep_index = encoded / tail_size;
        encoded %= tail_size;
        coefficient[first - 1] = reps[rep_index];
        for (u64 r = T; r > first; --r) {
          coefficient[r - 1] = encoded % ctx.q;
          encoded /= ctx.q;
        }

        u64 product_value = 1;
        for (u64 i = 0; i < n; ++i) {
          u64 phase = 0;
          for (u64 r = first; r <= T; ++r) {
            phase += contribution[r - 1][i][coefficient[r - 1]];
          }
          phase %= ctx.q;
          product_value = mul_mod(product_value, factor[phase], ctx.mod);
        }
        local = add_mod(local, mul_mod(orbit_weight, product_value, ctx.mod), ctx.mod);
      }
#pragma omp critical
      case_sum = add_mod(case_sum, local, ctx.mod);
    }
    fourier = add_mod(fourier, case_sum, ctx.mod);
  }
  return mul_mod(fourier, inverse_power_q(ctx, T), ctx.mod);
}

static u64 direct_level_count(const Context& ctx, u64 cells, u64 dimension,
                              u64 alphabet_layers, u64 root) {
  u64 total_duals = 1;
  for (u64 r = 0; r < dimension; ++r) total_duals *= ctx.q;
  u64 sum = 0;
  for (u64 flat = 0; flat < total_duals; ++flat) {
    std::vector<u64> coefficient(dimension);
    u64 encoded = flat;
    for (u64 r = dimension; r > 0; --r) {
      coefficient[r - 1] = encoded % ctx.q;
      encoded /= ctx.q;
    }
    u64 product_value = 1;
    u64 point = 1;
    for (u64 i = 0; i < cells; ++i) {
      u64 phase = 0;
      u64 power = point;
      for (u64 r = 0; r < dimension; ++r) {
        phase = (phase + coefficient[r] * power) % ctx.q;
        power = power * point % ctx.q;
      }
      const u64 base = add_mod(1, ctx.character[phase], ctx.mod);
      product_value = mul_mod(product_value, pow_mod(base, alphabet_layers, ctx.mod), ctx.mod);
      point = point * root % ctx.q;
    }
    sum = add_mod(sum, product_value, ctx.mod);
  }
  return mul_mod(sum, inverse_power_q(ctx, dimension), ctx.mod);
}

static u64 direct_skew_count(const Context& ctx, u64 cells,
                             const std::vector<u64>& exponents,
                             u64 alphabet_layers, u64 root) {
  const u64 dimension = exponents.size();
  u64 total_duals = 1;
  for (u64 r = 0; r < dimension; ++r) total_duals *= ctx.q;
  u64 sum = 0;
  for (u64 flat = 0; flat < total_duals; ++flat) {
    std::vector<u64> coefficient(dimension);
    u64 encoded = flat;
    for (u64 r = dimension; r > 0; --r) {
      coefficient[r - 1] = encoded % ctx.q;
      encoded /= ctx.q;
    }
    u64 product_value = 1;
    u64 point = 1;
    for (u64 i = 0; i < cells; ++i) {
      u64 phase = 0;
      for (u64 r = 0; r < dimension; ++r) {
        phase = (phase + coefficient[r] * pow_mod(point, exponents[r], ctx.q)) % ctx.q;
      }
      const u64 base = add_mod(1, ctx.character[phase], ctx.mod);
      const u64 negative_shift = phase == 0
          ? 0
          : ctx.q - (alphabet_layers / 2 * phase) % ctx.q;
      u64 local = pow_mod(base, alphabet_layers, ctx.mod);
      local = mul_mod(local, ctx.character[negative_shift], ctx.mod);
      product_value = mul_mod(product_value, local, ctx.mod);
      point = point * root % ctx.q;
    }
    sum = add_mod(sum, product_value, ctx.mod);
  }
  return mul_mod(sum, inverse_power_q(ctx, dimension), ctx.mod);
}

int main(int argc, char** argv) {
  if (argc != 5) return 2;
  const u64 n = std::stoull(argv[1]);
  const u64 t = std::stoull(argv[2]);
  const u64 q = std::stoull(argv[3]);
  const u64 mod = std::stoull(argv[4]);
  if (n % 2 || t < 2 || (t & (t - 1)) || (q - 1) % n || (mod - 1) % q) return 3;
  const u64 m = static_cast<u64>(__builtin_ctzll(t));

  const u64 generator = primitive_root(q);
  const u64 zeta = pow_mod(generator, (q - 1) / n, q);
  if (pow_mod(zeta, n, q) != 1 || pow_mod(zeta, n / 2, q) == 1) return 4;
  u64 omega = 1;
  for (u64 base = 2; omega == 1; ++base) {
    omega = pow_mod(base, (mod - 1) / q, mod);
  }
  if (pow_mod(omega, q, mod) != 1 || omega == 1) return 5;

  Context ctx{n, t, q, mod, zeta, pow_mod(q % mod, mod - 2, mod), {}};
  ctx.character.resize(q);
  ctx.character[0] = 1;
  for (u64 value = 1; value < q; ++value) {
    ctx.character[value] = mul_mod(ctx.character[value - 1], omega, mod);
  }

  std::vector<u64> levels(m + 1), blocks(m);
  levels[0] = level_zero_orbit_count(ctx);
  for (u64 level = 1; level <= m; ++level) {
    const u64 scale = u64{1} << level;
    levels[level] = direct_level_count(
        ctx, n / scale, t / scale, scale, pow_mod(zeta, scale, q));
  }
  const u64 c1 = direct_level_count(ctx, n / 2, t / 2, 1, pow_mod(zeta, 2, q));
  for (u64 j = 0; j < m; ++j) {
    std::vector<u64> odd_exponents;
    for (u64 exponent = 1; exponent * (u64{1} << j) <= t; exponent += 2) {
      odd_exponents.push_back(exponent);
    }
    const u64 scale = u64{1} << j;
    blocks[j] = direct_skew_count(
        ctx, n / (2 * scale), odd_exponents, 2 * scale,
        pow_mod(zeta, scale, q));
  }

  std::cout << "n=" << n << "\nt=" << t << "\nq=" << q
            << "\nmodulus=" << mod << "\n";
  for (u64 level = 0; level <= m; ++level) {
    std::cout << "z" << level << "=" << levels[level] << "\n";
  }
  std::cout << "c1=" << c1 << "\n";
  for (u64 j = 0; j < m; ++j) {
    std::cout << "b" << j << "=" << blocks[j] << "\n";
  }
  return 0;
}
