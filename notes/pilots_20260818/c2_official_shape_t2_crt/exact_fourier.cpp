#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static u64 mul_mod(u64 a, u64 b, u64 mod) {
  return static_cast<u64>(static_cast<u128>(a) * b % mod);
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

static u64 add_mod(u64 a, u64 b, u64 mod) {
  return static_cast<u64>((static_cast<u128>(a) + b) % mod);
}

int main(int argc, char** argv) {
  if (argc != 4) return 2;
  const u64 n = std::stoull(argv[1]);
  const u64 q = std::stoull(argv[2]);
  const u64 mod = std::stoull(argv[3]);
  if (n % 2 || (q - 1) % n || (mod - 1) % q) return 3;

  const u64 gq = primitive_root(q);
  const u64 zeta = pow_mod(gq, (q - 1) / n, q);
  if (pow_mod(zeta, n, q) != 1 || pow_mod(zeta, n / 2, q) == 1) return 4;
  const u64 zeta2 = mul_mod(zeta, zeta, q);

  u64 omega = 1;
  for (u64 base = 2; omega == 1; ++base) {
    omega = pow_mod(base, (mod - 1) / q, mod);
  }
  if (pow_mod(omega, q, mod) != 1 || omega == 1) return 5;

  std::vector<u64> character(q);
  character[0] = 1;
  for (u64 value = 1; value < q; ++value) {
    character[value] = mul_mod(character[value - 1], omega, mod);
  }

  std::vector<u64> root1(n), root2(n);
  root1[0] = root2[0] = 1;
  for (u64 i = 1; i < n; ++i) {
    root1[i] = mul_mod(root1[i - 1], zeta, q);
    root2[i] = mul_mod(root2[i - 1], zeta2, q);
  }

  const u64 plane = q * q;
  std::vector<std::uint8_t> visited(plane, 0);
  u64 fourier2 = 0;
  u64 orbit_count = 0;
  for (u64 a0 = 0; a0 < q; ++a0) {
    for (u64 b0 = 0; b0 < q; ++b0) {
      const u64 index = a0 * q + b0;
      if (visited[index]) continue;
      ++orbit_count;

      u64 a = a0, b = b0, orbit = 0;
      do {
        visited[a * q + b] = 1;
        ++orbit;
        a = mul_mod(a, zeta, q);
        b = mul_mod(b, zeta2, q);
      } while (a != a0 || b != b0);

      u64 term_product = 1;
      for (u64 i = 0; i < n; ++i) {
        const u64 phase = static_cast<u64>(
            (static_cast<u128>(a0) * root1[i] +
             static_cast<u128>(b0) * root2[i]) % q);
        const u64 term = add_mod(1, character[phase], mod);
        term_product = mul_mod(term_product, term, mod);
      }
      fourier2 = add_mod(fourier2, mul_mod(orbit % mod, term_product, mod), mod);
    }
  }
  const u64 inv_q = pow_mod(q % mod, mod - 2, mod);
  const u64 z0 = mul_mod(fourier2, mul_mod(inv_q, inv_q, mod), mod);

  const u64 h = n / 2;
  u64 c1_sum = 0, z1_sum = 0, b0_sum = 0;
  for (u64 dual = 0; dual < q; ++dual) {
    u64 c1_product = 1, z1_product = 1, b0_product = 1;
    for (u64 i = 0; i < h; ++i) {
      const u64 even_phase = mul_mod(dual, root2[i], q);
      const u64 even_term = add_mod(1, character[even_phase], mod);
      c1_product = mul_mod(c1_product, even_term, mod);
      z1_product = mul_mod(z1_product, mul_mod(even_term, even_term, mod), mod);

      const u64 odd_phase = mul_mod(dual, root1[i], q);
      const u64 negative = odd_phase == 0 ? 0 : q - odd_phase;
      u64 odd_term = add_mod(2, character[odd_phase], mod);
      odd_term = add_mod(odd_term, character[negative], mod);
      b0_product = mul_mod(b0_product, odd_term, mod);
    }
    c1_sum = add_mod(c1_sum, c1_product, mod);
    z1_sum = add_mod(z1_sum, z1_product, mod);
    b0_sum = add_mod(b0_sum, b0_product, mod);
  }
  const u64 c1 = mul_mod(c1_sum, inv_q, mod);
  const u64 z1 = mul_mod(z1_sum, inv_q, mod);
  const u64 b0 = mul_mod(b0_sum, inv_q, mod);

  std::cout << "n=" << n << "\nq=" << q << "\nmodulus=" << mod
            << "\norbits=" << orbit_count << "\nz0=" << z0
            << "\nc1=" << c1 << "\nz1=" << z1 << "\nb0=" << b0
            << "\n";
  return 0;
}
