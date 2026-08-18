#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <utility>
#include <vector>

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

static bool is_prime(std::uint64_t value) {
  if (value < 2) return false;
  if (value % 2 == 0) return value == 2;
  for (std::uint64_t p = 3; p * p <= value; p += 2) {
    if (value % p == 0) return false;
  }
  return true;
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
    bool good = true;
    for (const auto p : factors) {
      if (mod_pow(g, (q - 1) / p, q) == 1) {
        good = false;
        break;
      }
    }
    if (good) return g;
  }
  throw std::runtime_error("primitive root missing");
}

using Histogram = std::unordered_map<std::uint64_t, std::uint64_t>;

static Histogram pair_histogram(
    const std::vector<std::pair<std::uint64_t, std::uint64_t>>& values,
    std::uint64_t q) {
  const std::size_t count = std::size_t{1} << values.size();
  Histogram out;
  out.reserve(count * 2);
  std::uint64_t previous_gray = 0;
  std::uint64_t s1 = 0, s2 = 0;
  ++out[0];
  for (std::size_t step = 1; step < count; ++step) {
    const std::uint64_t gray = step ^ (step >> 1);
    const std::uint64_t changed = gray ^ previous_gray;
    const unsigned index = __builtin_ctzll(changed);
    const bool added = (gray & changed) != 0;
    const auto [a, b] = values[index];
    if (added) {
      s1 = (s1 + a) % q;
      s2 = (s2 + b) % q;
    } else {
      s1 = (s1 + q - a) % q;
      s2 = (s2 + q - b) % q;
    }
    ++out[s1 * q + s2];
    previous_gray = gray;
  }
  return out;
}

static std::uint64_t owner_count(const std::vector<std::uint64_t>& values,
                                 std::uint64_t q) {
  const std::size_t count = std::size_t{1} << values.size();
  std::uint64_t answer = 1;
  std::uint64_t previous_gray = 0;
  std::uint64_t sum = 0;
  for (std::size_t step = 1; step < count; ++step) {
    const std::uint64_t gray = step ^ (step >> 1);
    const std::uint64_t changed = gray ^ previous_gray;
    const unsigned index = __builtin_ctzll(changed);
    if (gray & changed) {
      sum = (sum + values[index]) % q;
    } else {
      sum = (sum + q - values[index]) % q;
    }
    answer += sum == 0;
    previous_gray = gray;
  }
  return answer;
}

static std::vector<std::uint64_t> scalar_histogram(
    const std::vector<std::uint64_t>& values, std::uint64_t q) {
  const std::size_t count = std::size_t{1} << values.size();
  std::vector<std::uint64_t> out(q);
  std::uint64_t previous_gray = 0;
  std::uint64_t sum = 0;
  ++out[0];
  for (std::size_t step = 1; step < count; ++step) {
    const std::uint64_t gray = step ^ (step >> 1);
    const std::uint64_t changed = gray ^ previous_gray;
    const unsigned index = __builtin_ctzll(changed);
    if (gray & changed) {
      sum = (sum + values[index]) % q;
    } else {
      sum = (sum + q - values[index]) % q;
    }
    ++out[sum];
    previous_gray = gray;
  }
  return out;
}

static void scan_row(std::uint64_t q) {
  constexpr std::uint64_t n = 32;
  const auto generator = primitive_root(q);
  const auto zeta = mod_pow(generator, (q - 1) / n, q);
  if (mod_pow(zeta, n, q) != 1 || mod_pow(zeta, n / 2, q) == 1) {
    throw std::runtime_error("bad order-32 root");
  }

  std::vector<std::pair<std::uint64_t, std::uint64_t>> left, right;
  std::vector<std::uint64_t> even_values, odd_values;
  std::uint64_t root = 1;
  for (std::uint64_t i = 0; i < n; ++i) {
    const auto square = static_cast<__uint128_t>(root) * root % q;
    (i < n / 2 ? left : right).push_back({root, square});
    if (i < n / 2) {
      even_values.push_back(square);
      odd_values.push_back(root);
    }
    root = static_cast<__uint128_t>(root) * zeta % q;
  }

  const auto first = pair_histogram(left, q);
  const auto second = pair_histogram(right, q);
  std::uint64_t z0 = 0;
  for (const auto& [key, multiplicity] : first) {
    const auto a = key / q;
    const auto b = key % q;
    const auto target = ((q - a) % q) * q + (q - b) % q;
    const auto found = second.find(target);
    if (found != second.end()) z0 += multiplicity * found->second;
  }
  const auto c1 = owner_count(even_values, q);
  if (z0 < c1) throw std::runtime_error("owner exceeds joint");
  const auto primitive = z0 - c1;

  const auto even_hist = scalar_histogram(even_values, q);
  const auto odd_hist = scalar_histogram(odd_values, q);
  std::uint64_t z1 = 0, b0 = 0;
  for (std::uint64_t value = 0; value < q; ++value) {
    z1 += even_hist[value] * even_hist[(q - value) % q];
    b0 += odd_hist[value] * odd_hist[value];
  }

  const __uint128_t scaled = static_cast<__uint128_t>(q) * q * primitive;
  const __uint128_t threshold = static_cast<__uint128_t>(8) << n;
  const bool fires = scaled > threshold;
  const __uint128_t j_left = static_cast<__uint128_t>(primitive) << n;
  const __uint128_t j_right = static_cast<__uint128_t>(8) * z1 * b0;
  const bool j_fires = j_left > j_right;
  std::cout << q << ',' << z0 << ',' << c1 << ',' << primitive << ','
            << (fires ? 1 : 0) << ',' << z1 << ',' << b0 << ','
            << (j_fires ? 1 : 0) << '\n' << std::flush;
}

int main(int argc, char** argv) {
  if (argc != 3) return 2;
  const std::uint64_t low = std::stoull(argv[1]);
  const std::uint64_t high = std::stoull(argv[2]);
  std::cout << "q,z0,c1,primitive,fires,z1,b0,j_fires\n" << std::flush;
  for (std::uint64_t q = low; q <= high; ++q) {
    if ((q - 1) % 32 == 0 && is_prime(q)) scan_row(q);
  }
  return 0;
}
