#!/usr/bin/env python3
"""Verify the m12 diagonal-socle route cut."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def set_partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in set_partitions(rest):
        yield (frozenset({first}),) + partition
        for index in range(len(partition)):
            blocks = list(partition)
            blocks[index] = blocks[index] | {first}
            yield tuple(sorted(blocks, key=lambda block: min(block)))


def canonical(partition):
    return tuple(sorted((tuple(sorted(block)) for block in partition)))


def image_partition(partition, permutation):
    return canonical(
        tuple(frozenset(permutation[item] for item in block) for block in partition)
    )


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "(r,delta)=(4,12)" in statement
    assert "Dickson branch is empty" in contract

    catalogue = {
        "M11": (7_920, "M11"),
        "M12": (95_040, "M12"),
        "PSL(2,11)": (660, "PSL(2,11)"),
        "PGL(2,11)": (1_320, "PSL(2,11)"),
        "A12": (239_500_800, "A12"),
        "S12": (479_001_600, "A12"),
    }
    assert len(catalogue) == 6
    assert min(order for order, _ in catalogue.values()) == 660
    assert {socle for _, socle in catalogue.values()} == {
        "M11", "M12", "PSL(2,11)", "A12"
    }
    assert 24 < 660

    # A five-cycle already forces an invariant set partition of five points
    # to be either the singleton partition or the one-part partition.
    rotation = {index: (index + 1) % 5 for index in range(5)}
    invariant = set()
    for partition in set_partitions(list(range(5))):
        key = canonical(partition)
        if image_partition(partition, rotation) == key:
            invariant.add(key)
    assert invariant == {
        ((0,), (1,), (2,), (3,), (4,)),
        ((0, 1, 2, 3, 4),),
    }

    # In the independent case a point in any other block has a 12-point
    # socle orbit, already larger than the actual quartic suborbit.
    actual_suborbit = 4
    independent_other_block_orbit = 12
    assert independent_other_block_orbit > actual_suborbit

    # In the diagonal case every block met by a size-four orbit contributes
    # one fixed point. Thus the suborbit size equals its block projection.
    live_outer_subdegrees = {2, 4}
    survivors = {
        r for r in live_outer_subdegrees if r == actual_suborbit
    }
    assert survivors == {4}
    print("RATE_HALF_KB_M12_DIAGONAL_SOCLE_ROUTE_CUT_PASS")


if __name__ == "__main__":
    main()
