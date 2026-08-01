#!/usr/bin/env python3
"""Exact full-row replay for the DLI C1 L=1 block-owner ledger."""

from fractions import Fraction


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def prime_factors(value):
    output = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            output.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        output.append(value)
    return output


def primitive_root(prime):
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1
               for factor in factors):
            return candidate
    raise AssertionError("no primitive root")


def main():
    prime, length = 7681, 256
    generator = primitive_root(prime)
    omega = pow(generator, (prime - 1) // 512, prime)
    require(pow(omega, 256, prime) == prime - 1, "omega order")
    coefficients = [pow(omega, index, prime) for index in range(length)]

    counts = [0] * prime
    counts[0] = 1
    z_values = [Fraction(1)]
    for index, coefficient in enumerate(coefficients, 1):
        updated = counts.copy()
        for residue, count in enumerate(counts):
            if count:
                updated[(residue + coefficient) % prime] += count
        counts = updated
        if index % 4 == 0:
            collision = Fraction(
                sum(count * count for count in counts), 2 ** (2 * index)
            )
            z_values.append(2**index * collision)

    require(len(z_values) == 65, "checkpoint count")
    require(sum(counts) == 2**length, "Boolean mass")

    for block_index in range(64):
        block = coefficients[4*block_index:4*block_index+4]
        kappa = {0: Fraction(1)}
        for coefficient in block:
            updated = {}
            for residue, weight in kappa.items():
                for digit, factor in (
                    (0, Fraction(1)),
                    (1, Fraction(1, 2)),
                    (-1, Fraction(1, 2)),
                ):
                    target = (residue + digit*coefficient) % prime
                    updated[target] = updated.get(target, Fraction(0)) \
                        + weight*factor
            kappa = updated
        require(sum(kappa.values()) == 16,
                f"kappa mass block {block_index}")
        require(kappa[0] == 1,
                f"kappa(0) block {block_index}")

    owner_sum = Fraction(0)
    for block_index in range(64):
        actual = z_values[block_index + 1] - z_values[block_index]
        haar = Fraction(15 * 2 ** (4 * block_index), prime)
        owner_sum += actual - haar
    terminal = z_values[-1] - Fraction(2**256, prime)
    require(
        terminal == Fraction(1) - Fraction(1, prime) + owner_sum,
        "telescoping identity",
    )
    print(
        "DLI_C1_L1_BLOCK_OWNER_LEDGER_PASS",
        f"q={prime} blocks=64 terminal_minus_haar={float(terminal):.6f}",
    )


if __name__ == "__main__":
    main()
