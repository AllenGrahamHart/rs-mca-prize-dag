#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

namespace {

constexpr std::uint64_t P = 2130706433ULL;
constexpr std::uint64_t N = 1ULL << 21;
constexpr std::uint64_t INDEX = 1016;
constexpr std::uint64_t GENERATOR = 3;

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

bool exponent_member(std::uint64_t value) {
    if (value == 0) return false;
    for (int step = 0; step < 21; ++step) value = multiply(value, value);
    return value == 1;
}

void set_bit(std::vector<std::uint64_t>& bits, std::uint64_t value) {
    bits[value >> 6] |= 1ULL << (value & 63ULL);
}

bool get_bit(const std::vector<std::uint64_t>& bits, std::uint64_t value) {
    return ((bits[value >> 6] >> (value & 63ULL)) & 1ULL) != 0;
}

}  // namespace

int main(int argc, char** argv) {
    if (argc != 3) throw std::runtime_error("usage: census LO HI");
    const int lo = std::stoi(argv[1]);
    const int hi = std::stoi(argv[2]);
    if (lo < 0 || lo >= hi || hi > static_cast<int>(INDEX)) {
        throw std::runtime_error("invalid shard");
    }
    if (power(GENERATOR, (P - 1) / 2) == 1 ||
        power(GENERATOR, (P - 1) / 127) == 1) {
        throw std::runtime_error("generator is not primitive");
    }

    const std::uint64_t h = power(GENERATOR, INDEX);
    const std::uint64_t h_inverse = power(h, P - 2);
    if (power(h, N) != 1 || power(h, N / 2) == 1) {
        throw std::runtime_error("subgroup generator order");
    }

    std::vector<std::uint64_t> bits((P + 63) / 64, 0);
    std::uint64_t x = 1;
    for (std::uint64_t i = 0; i < N; ++i) {
        if (get_bit(bits, x)) throw std::runtime_error("early subgroup repeat");
        set_bit(bits, x);
        x = multiply(x, h);
    }
    if (x != 1) throw std::runtime_error("subgroup closure");

    std::uint64_t c = power(GENERATOR, static_cast<std::uint64_t>(lo));
    for (int index = lo; index < hi; ++index) {
        std::uint64_t production = 0;
        x = 1;
        for (std::uint64_t i = 0; i < N; ++i) {
            const std::uint64_t y = c >= x ? c - x : P + c - x;
            production += y != 0 && get_bit(bits, y);
            x = multiply(x, h);
        }

        std::uint64_t audit = 0;
        x = 1;
        for (std::uint64_t i = 0; i < N; ++i) {
            const std::uint64_t y = c >= x ? c - x : P + c - x;
            audit += exponent_member(y);
            x = multiply(x, h_inverse);
        }
        if (production != audit) throw std::runtime_error("implementation disagreement");
        std::cout << index << '\t' << c << '\t' << production << '\t' << audit << '\n';
        c = multiply(c, GENERATOR);
    }
    return 0;
}
