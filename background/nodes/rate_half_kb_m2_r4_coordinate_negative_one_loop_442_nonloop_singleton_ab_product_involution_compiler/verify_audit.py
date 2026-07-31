#!/usr/bin/env python3
"""Independent deployed-field audit of the cells [3,6] involution."""


PRIME = 2130706433
B_C_ROOTS = {
    1608564875: (181785890, PRIME-181785890),
    1587494773: (449324246, PRIME-449324246),
}


def main():
    checked = 0
    mates = set()
    for b, c_roots in B_C_ROOTS.items():
        if (2*b*b+3*b+2) % PRIME:
            raise RuntimeError("b equation")
        for c in c_roots:
            if (4*c*c-5*b-6) % PRIME:
                raise RuntimeError("c-square relation")
            gamma = b*(b+1) % PRIME
            alpha = -(b**3+c**2) % PRIME
            beta = -b*(b+1)*c**2 % PRIME

            def phi(left, right):
                return (
                    gamma*left*right-alpha*(left+right)-beta
                ) % PRIME

            if phi(-b*b, -b) or phi(c, -c):
                raise RuntimeError("common product pairs")
            determinant = (alpha*alpha+gamma*beta) % PRIME
            expected_determinant = (
                (b-c)*(b+c)*(b*b-c)*(b*b+c)
            ) % PRIME
            if determinant == 0 or determinant != expected_determinant:
                raise RuntimeError("determinant")
            denominator = (gamma*b-alpha) % PRIME
            if denominator == 0:
                raise RuntimeError("mate denominator")
            mate = (alpha*b+beta)*pow(denominator, -1, PRIME) % PRIME
            expected = (18-5*b)*pow(22, -1, PRIME) % PRIME
            if mate != expected or phi(b, mate):
                raise RuntimeError("forced mate")
            common = {-(b*b) % PRIME, -b % PRIME, c, -c % PRIME, b}
            if mate == 0 or mate in common:
                raise RuntimeError("mate guard")
            mates.add(mate)
            checked += 1
    if checked != 4 or len(mates) != 2:
        raise RuntimeError("audit census")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_INVOLUTION_AUDIT_PASS "
        "field=2130706433 common_packets=4 mates=2 determinant=guarded"
    )


if __name__ == "__main__":
    main()
