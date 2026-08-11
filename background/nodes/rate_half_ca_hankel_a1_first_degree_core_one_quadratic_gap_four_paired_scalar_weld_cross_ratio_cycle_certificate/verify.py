#!/usr/bin/env python3
"""Exact finite-field replay of the cross-ratio cycle certificate."""

Q = 101


def inverse(value):
    return pow(value % Q, -1, Q)


def ratio(left, right):
    return left * inverse(right) % Q


def certificate(edges, labels, xset, zset):
    transitions = {}
    for first_index, first in enumerate(zset):
        for second in zset[first_index + 1 :]:
            common = [
                x for x in xset
                if (first, x) in edges and (second, x) in edges
            ]
            assert common
            values = {
                ratio(labels[first, x], labels[second, x])
                for x in common
            }
            if len(values) != 1:
                return False
            value = values.pop()
            transitions[first, second] = value
            transitions[second, first] = inverse(value)

    for first in zset:
        for second in zset:
            for third in zset:
                if len({first, second, third}) == 3:
                    if (
                        transitions[first, second]
                        * transitions[second, third]
                        * transitions[third, first]
                    ) % Q != 1:
                        return False
    return True


def main():
    xset = list(range(6))
    zset = list(range(4))
    omitted = {
        0: {0, 1},
        1: {1, 2},
        2: {2, 3},
        3: {3, 4},
    }
    edges = {
        (delta, x)
        for delta in zset
        for x in xset
        if x not in omitted[delta]
    }

    lambdas = [2, 3, 5, 7, 11, 13]
    zetas = [17, 19, 23, 29]
    labels = {
        (delta, x): zetas[delta] * inverse(lambdas[x]) % Q
        for delta, x in edges
    }
    assert certificate(edges, labels, xset, zset)

    tampered = labels.copy()
    tampered[0, 5] = tampered[0, 5] * 2 % Q
    assert not certificate(edges, tampered, xset, zset)
    print("PASS scalar-weld cross-ratio certificate tamper=1/1")


if __name__ == "__main__":
    main()
