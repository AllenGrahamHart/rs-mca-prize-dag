#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>

namespace {

constexpr std::uint64_t P = 2130706433ULL;
constexpr std::uint64_t N = 1ULL << 21;
constexpr std::uint64_t INDEX = 1016;
constexpr std::uint64_t GENERATOR = 3;
constexpr int RANDOM_PARAMETERS = 32;
constexpr int TOTAL_PARAMETERS = 64;

struct Parameter {
    std::uint64_t kappa;
    const char* kind;
};

std::uint64_t multiply(std::uint64_t left, std::uint64_t right) {
    return (left * right) % P;
}

std::uint64_t power(std::uint64_t base, std::uint64_t exponent) {
    std::uint64_t result = 1;
    while (exponent != 0) {
        if (exponent & 1ULL) result = multiply(result, base);
        base = multiply(base, base);
        exponent >>= 1;
    }
    return result;
}

std::uint64_t splitmix64(std::uint64_t& state) {
    std::uint64_t value = (state += 0x9e3779b97f4a7c15ULL);
    value = (value ^ (value >> 30)) * 0xbf58476d1ce4e5b9ULL;
    value = (value ^ (value >> 27)) * 0x94d049bb133111ebULL;
    return value ^ (value >> 31);
}

void set_bit(std::vector<std::uint64_t>& bits, std::uint64_t value) {
    bits[value >> 6] |= 1ULL << (value & 63ULL);
}

bool get_bit(const std::vector<std::uint64_t>& bits, std::uint64_t value) {
    return ((bits[value >> 6] >> (value & 63ULL)) & 1ULL) != 0;
}

bool exponent_member(std::uint64_t value) {
    if (value == 0) return false;
    for (int step = 0; step < 21; ++step) value = multiply(value, value);
    return value == 1;
}

}  // namespace

int main(int argc, char** argv) {
    if (argc != 2) throw std::runtime_error("usage: probe TAU_INDEX");
    const int tau_index = std::stoi(argv[1]);
    if (tau_index < 0 || tau_index >= static_cast<int>(INDEX)) {
        throw std::runtime_error("invalid tau index");
    }
    if (power(GENERATOR, (P - 1) / 2) == 1 ||
        power(GENERATOR, (P - 1) / 127) == 1) {
        throw std::runtime_error("generator is not primitive");
    }

    const std::uint64_t h = power(GENERATOR, INDEX);
    if (power(h, N) != 1 || power(h, N / 2) == 1) {
        throw std::runtime_error("subgroup generator order");
    }
    const std::uint64_t tau = power(GENERATOR, tau_index);

    std::vector<std::uint64_t> bits((P + 63) / 64, 0);
    std::vector<std::uint32_t> points(N);
    std::uint64_t x = 1;
    for (std::uint64_t index = 0; index < N; ++index) {
        if (get_bit(bits, x)) throw std::runtime_error("early subgroup repeat");
        points[index] = static_cast<std::uint32_t>(x);
        set_bit(bits, x);
        x = multiply(x, h);
    }
    if (x != 1) throw std::runtime_error("subgroup closure");

    std::vector<std::uint64_t> prefix(N);
    std::vector<std::uint32_t> inverses(N);
    std::uint64_t product = 1;
    for (std::uint64_t index = 0; index < N; ++index) {
        prefix[index] = product;
        const std::uint64_t denominator = (points[index] + tau) % P;
        if (denominator != 0) product = multiply(product, denominator);
    }
    std::uint64_t inverse_product = power(product, P - 2);
    for (std::uint64_t index = N; index-- > 0;) {
        const std::uint64_t denominator = (points[index] + tau) % P;
        if (denominator == 0) {
            inverses[index] = 0;
        } else {
            inverses[index] = static_cast<std::uint32_t>(multiply(inverse_product, prefix[index]));
            inverse_product = multiply(inverse_product, denominator);
        }
    }
    if (inverse_product != 1) throw std::runtime_error("batch inverse audit");

    std::uint64_t state = 0x72616e6b31317370ULL ^ static_cast<std::uint64_t>(tau_index);
    std::unordered_set<std::uint64_t> seen;
    std::vector<Parameter> parameters;
    while (static_cast<int>(parameters.size()) < RANDOM_PARAMETERS) {
        const std::uint64_t kappa = 1 + splitmix64(state) % (P - 1);
        if (seen.insert(kappa).second) parameters.push_back({kappa, "random"});
    }
    while (static_cast<int>(parameters.size()) < TOTAL_PARAMETERS) {
        const std::uint64_t left_index = splitmix64(state) % N;
        std::uint64_t right_index = splitmix64(state) % N;
        if (right_index == left_index) right_index = (right_index + 1) % N;
        const std::uint64_t left = (points[left_index] + tau) % P;
        const std::uint64_t right = (points[right_index] + tau) % P;
        if (left == 0 || right == 0) continue;
        const std::uint64_t kappa = multiply(left, right);
        if (kappa != 0 && seen.insert(kappa).second) {
            parameters.push_back({kappa, "planted"});
        }
    }

    std::uint64_t maximum = 0;
    std::uint64_t maximizing_kappa = 0;
    for (int parameter_index = 0; parameter_index < TOTAL_PARAMETERS; ++parameter_index) {
        const Parameter& parameter = parameters[parameter_index];
        std::uint64_t total = 0;
        std::uint64_t fixed = 0;
        for (std::uint64_t index = 0; index < N; ++index) {
            if (inverses[index] == 0) continue;
            const std::uint64_t shifted = multiply(parameter.kappa, inverses[index]);
            const std::uint64_t image = shifted >= tau ? shifted - tau : P + shifted - tau;
            if (get_bit(bits, image)) {
                ++total;
                fixed += image == points[index];
            }
        }
        const std::uint64_t nonfixed = total - fixed;
        if (fixed > 2 || (nonfixed & 1ULL)) throw std::runtime_error("involution orbit audit");
        std::cout << tau_index << '\t' << tau << '\t' << parameter_index << '\t'
                  << parameter.kind << '\t' << parameter.kappa << '\t' << total << '\t'
                  << fixed << '\t' << nonfixed << '\n';
        if (nonfixed > maximum) {
            maximum = nonfixed;
            maximizing_kappa = parameter.kappa;
        }
    }

    std::uint64_t audit_total = 0;
    std::uint64_t audit_fixed = 0;
    for (std::uint64_t index = N; index-- > 0;) {
        if (inverses[index] == 0) continue;
        const std::uint64_t shifted = multiply(maximizing_kappa, inverses[index]);
        const std::uint64_t image = shifted >= tau ? shifted - tau : P + shifted - tau;
        if (exponent_member(image)) {
            ++audit_total;
            audit_fixed += image == points[index];
        }
    }
    if (audit_total - audit_fixed != maximum) {
        throw std::runtime_error("maximum implementation disagreement");
    }
    return 0;
}
