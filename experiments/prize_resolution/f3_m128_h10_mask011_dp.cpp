#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <map>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct State {
  int plus;
  int minus;
  int odd;
  int delta0;
  int delta1;
  int total;
};

struct Energy {
  int plus;
  int minus;
  int odd;
  int delta0;
  int delta1;
};

static std::uint64_t pack_state(const State& state) {
  std::uint64_t key = static_cast<std::uint64_t>(state.plus);
  key = (key << 5) | state.minus;
  key = (key << 10) | state.odd;
  key = (key << 10) | state.delta0;
  key = (key << 10) | state.delta1;
  key = (key << 6) | (state.total + 16);
  return key;
}

static State unpack_state(std::uint64_t key) {
  State state{};
  state.total = static_cast<int>(key & 63) - 16;
  key >>= 6;
  state.delta1 = key & 1023;
  key >>= 10;
  state.delta0 = key & 1023;
  key >>= 10;
  state.odd = key & 1023;
  key >>= 10;
  state.minus = key & 31;
  key >>= 5;
  state.plus = key & 31;
  return state;
}

static std::vector<State> combine_level(const std::vector<State>& left,
                                        const std::vector<State>& right,
                                        int level) {
  std::unordered_set<std::uint64_t> seen;
  for (const State& a : left) {
    for (const State& b : right) {
      if (a.plus + b.plus > 10 || a.minus + b.minus > 10) continue;
      State out{a.plus + b.plus,
                a.minus + b.minus,
                a.odd + b.odd,
                a.delta0 + b.delta0,
                a.delta1 + b.delta1,
                a.total + b.total};
      const int square = (a.total - b.total) * (a.total - b.total);
      if (level == 0) out.delta0 += square;
      if (level == 1) out.delta1 += square;
      seen.insert(pack_state(out));
    }
  }
  std::vector<State> result;
  result.reserve(seen.size());
  for (std::uint64_t key : seen) result.push_back(unpack_state(key));
  return result;
}

static std::vector<Energy> pareto(std::vector<Energy> states) {
  std::map<std::pair<int, int>, std::vector<Energy>> buckets;
  for (const Energy& state : states) {
    buckets[{state.plus, state.minus}].push_back(state);
  }

  std::vector<Energy> result;
  for (auto& [counts, bucket] : buckets) {
    std::sort(bucket.begin(), bucket.end(), [](const Energy& a, const Energy& b) {
      return std::tie(a.odd, a.delta0, a.delta1) >
             std::tie(b.odd, b.delta0, b.delta1);
    });
    int max_delta0 = 0;
    for (const Energy& state : bucket) max_delta0 = std::max(max_delta0, state.delta0);
    std::vector<int> suffix_best(max_delta0 + 2, -1);
    for (const Energy& state : bucket) {
      int best = -1;
      for (int delta0 = state.delta0; delta0 <= max_delta0; ++delta0) {
        best = std::max(best, suffix_best[delta0]);
      }
      if (best >= state.delta1) continue;
      result.push_back(state);
      suffix_best[state.delta0] = std::max(suffix_best[state.delta0], state.delta1);
    }
  }
  return result;
}

int main() {
  std::vector<State> leaves;
  for (int a = -1; a <= 1; ++a) {
    for (int b = -1; b <= 1; ++b) {
      leaves.push_back(State{static_cast<int>(a == 1) + static_cast<int>(b == 1),
                             static_cast<int>(a == -1) + static_cast<int>(b == -1),
                             (a - b) * (a - b), 0, 0, a + b});
    }
  }

  const std::vector<State> level0 = combine_level(leaves, leaves, 0);
  const std::vector<State> level1 = combine_level(level0, level0, 1);

  std::map<int, std::vector<State>> by_total;
  for (const State& state : level1) by_total[state.total].push_back(state);
  std::vector<Energy> group_candidates;
  for (const auto& [total, bucket] : by_total) {
    for (const State& a : bucket) {
      for (const State& b : bucket) {
        if (a.plus + b.plus > 10 || a.minus + b.minus > 10) continue;
        group_candidates.push_back(
            Energy{a.plus + b.plus, a.minus + b.minus, a.odd + b.odd,
                   a.delta0 + b.delta0, a.delta1 + b.delta1});
      }
    }
  }
  std::vector<Energy> groups = pareto(std::move(group_candidates));
  std::cerr << "local level0=" << level0.size() << " level1=" << level1.size()
            << " pareto_groups=" << groups.size() << std::endl;

  std::vector<Energy> global{{0, 0, 0, 0, 0}};
  for (int group_index = 0; group_index < 8; ++group_index) {
    std::vector<Energy> candidates;
    for (const Energy& left : global) {
      for (const Energy& right : groups) {
        if (left.plus + right.plus > 10 || left.minus + right.minus > 10) continue;
        candidates.push_back(Energy{left.plus + right.plus,
                                    left.minus + right.minus,
                                    left.odd + right.odd,
                                    left.delta0 + right.delta0,
                                    left.delta1 + right.delta1});
      }
    }
    global = pareto(std::move(candidates));
    std::cerr << "groups=" << group_index + 1 << " frontier=" << global.size()
              << std::endl;
  }

  long double maximum_log = -INFINITY;
  Energy witness{};
  std::size_t endpoint_states = 0;
  for (const Energy& state : global) {
    if (state.plus != 10 || state.minus != 10 || state.odd == 0 ||
        state.delta0 == 0 || state.delta1 == 0) {
      continue;
    }
    const long double value_log =
        32 * std::log2(static_cast<long double>(state.odd)) +
        16 * std::log2(static_cast<long double>(state.delta0)) +
        8 * std::log2(static_cast<long double>(state.delta1));
    if (value_log > maximum_log) {
      maximum_log = value_log;
      witness = state;
    }
    ++endpoint_states;
  }

  const bool closes = maximum_log < 235;
  std::cout << "F3_M128_H10_MASK011_DP_"
            << (closes ? "ROUTE_CLOSES" : "ROUTE_FALSIFIED")
            << " endpoint_states=" << endpoint_states
            << " max_energies=" << witness.odd << ',' << witness.delta0 << ','
            << witness.delta1 << " log2_max=" << static_cast<double>(maximum_log)
            << " margin_bits=" << static_cast<double>(235.0L - maximum_log)
            << std::endl;
  return 0;
}
