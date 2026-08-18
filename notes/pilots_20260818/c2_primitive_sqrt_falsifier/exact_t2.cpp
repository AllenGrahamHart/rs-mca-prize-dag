#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;

static std::uint64_t mod_pow(std::uint64_t a, std::uint64_t e,
                             std::uint64_t mod) {
  std::uint64_t out = 1;
  while (e) {
    if (e & 1) out = static_cast<__uint128_t>(out) * a % mod;
    a = static_cast<__uint128_t>(a) * a % mod;
    e >>= 1;
  }
  return out;
}

static std::vector<std::uint64_t> prime_factors(std::uint64_t value) {
  std::vector<std::uint64_t> out;
  for (std::uint64_t p = 2; p * p <= value; ++p) {
    if (value % p) continue;
    out.push_back(p);
    while (value % p == 0) value /= p;
  }
  if (value > 1) out.push_back(value);
  return out;
}

static std::uint64_t primitive_root(std::uint64_t q) {
  const auto factors = prime_factors(q - 1);
  for (std::uint64_t g = 2; g < q; ++g) {
    bool ok = true;
    for (auto p : factors) {
      if (mod_pow(g, (q - 1) / p, q) == 1) {
        ok = false;
        break;
      }
    }
    if (ok) return g;
  }
  throw std::runtime_error("primitive root missing");
}

static cpp_int subset_one(const std::vector<std::uint64_t>& roots,
                          std::uint64_t q) {
  std::vector<cpp_int> dp(q), next(q);
  dp[0] = 1;
  for (auto root : roots) {
#pragma omp parallel for schedule(static)
    for (std::int64_t a = 0; a < static_cast<std::int64_t>(q); ++a) {
      const auto prev = (a + q - root) % q;
      next[a] = dp[a] + dp[prev];
    }
    dp.swap(next);
  }
  return dp[0];
}

static cpp_int level_one(const std::vector<std::uint64_t>& roots,
                         std::uint64_t q) {
  std::vector<cpp_int> dp(q), next(q);
  dp[0] = 1;
  for (auto root : roots) {
#pragma omp parallel for schedule(static)
    for (std::int64_t a = 0; a < static_cast<std::int64_t>(q); ++a) {
      const auto prev1 = (a + q - root) % q;
      const auto prev2 = (a + q - (2 * root) % q) % q;
      next[a] = dp[a] + 2 * dp[prev1] + dp[prev2];
    }
    dp.swap(next);
  }
  return dp[0];
}

static cpp_int block_zero(const std::vector<std::uint64_t>& roots,
                          std::uint64_t q) {
  std::vector<cpp_int> dp(q), next(q);
  dp[0] = 1;
  for (auto root : roots) {
#pragma omp parallel for schedule(static)
    for (std::int64_t a = 0; a < static_cast<std::int64_t>(q); ++a) {
      const auto minus = (a + q - root) % q;
      const auto plus = (a + root) % q;
      next[a] = dp[minus] + 2 * dp[a] + dp[plus];
    }
    dp.swap(next);
  }
  return dp[0];
}

static cpp_int subset_two(const std::vector<std::pair<std::uint64_t,
                                                       std::uint64_t>>& vecs,
                          std::uint64_t q) {
  const std::uint64_t size = q * q;
  std::vector<cpp_int> dp(size), next(size);
  dp[0] = 1;
  for (const auto& [x, y] : vecs) {
#pragma omp parallel for schedule(static)
    for (std::int64_t index = 0; index < static_cast<std::int64_t>(size);
         ++index) {
      const std::uint64_t a = index / q;
      const std::uint64_t b = index % q;
      const std::uint64_t prev_a = (a + q - x) % q;
      const std::uint64_t prev_b = (b + q - y) % q;
      next[index] = dp[index] + dp[prev_a * q + prev_b];
    }
    dp.swap(next);
  }
  return dp[0];
}

int main(int argc, char** argv) {
  if (argc != 3) return 2;
  const std::uint64_t n = std::stoull(argv[1]);
  const std::uint64_t q = std::stoull(argv[2]);
  if ((q - 1) % n != 0 || n % 2 != 0) return 3;

  const auto g = primitive_root(q);
  const auto zeta = mod_pow(g, (q - 1) / n, q);
  if (mod_pow(zeta, n, q) != 1 || mod_pow(zeta, n / 2, q) == 1) return 4;

  std::vector<std::pair<std::uint64_t, std::uint64_t>> vectors;
  vectors.reserve(n);
  std::uint64_t root = 1;
  for (std::uint64_t i = 0; i < n; ++i) {
    vectors.push_back({root, static_cast<__uint128_t>(root) * root % q});
    root = static_cast<__uint128_t>(root) * zeta % q;
  }
  const cpp_int z0 = subset_two(vectors, q);

  const std::uint64_t half = n / 2;
  const auto eta = static_cast<__uint128_t>(zeta) * zeta % q;
  std::vector<std::uint64_t> even_roots, odd_roots;
  even_roots.reserve(half);
  odd_roots.reserve(half);
  std::uint64_t even = 1, odd = 1;
  for (std::uint64_t i = 0; i < half; ++i) {
    even_roots.push_back(even);
    odd_roots.push_back(odd);
    even = static_cast<__uint128_t>(even) * eta % q;
    odd = static_cast<__uint128_t>(odd) * zeta % q;
  }

  const cpp_int c1 = subset_one(even_roots, q);
  const cpp_int z1 = level_one(even_roots, q);
  const cpp_int b0 = block_zero(odd_roots, q);
  const cpp_int primitive = z0 - c1;
  const cpp_int numerator = primitive << n;
  const cpp_int denominator = z1 * b0;
  const bool fires = numerator * numerator > cpp_int(2 * n) * denominator * denominator;

  std::cout << "n=" << n << "\nq=" << q << "\nz0=" << z0
            << "\nc1=" << c1 << "\nz1=" << z1 << "\nb0=" << b0
            << "\nprimitive=" << primitive << "\nnumerator=" << numerator
            << "\ndenominator=" << denominator << "\nfires="
            << (fires ? 1 : 0) << "\n";
  return 0;
}
