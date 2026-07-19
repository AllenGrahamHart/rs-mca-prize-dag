#!/usr/bin/env python3
"""Verify the active-partition incidence reconstruction packet."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction"
HERE = ROOT / "background" / "nodes" / NODE


def propagate(rows, cols, theta, p):
    """Recover theta[x,g]=b[x]/a[g], or reject an inconsistent cycle."""
    a = {cols[0]: 1}
    b = {}
    changed = True
    while changed:
        changed = False
        for (x, g), value in theta.items():
            if g in a and x not in b:
                b[x] = value * a[g] % p
                changed = True
            if x in b and g not in a:
                a[g] = b[x] * pow(value, -1, p) % p
                changed = True
            if g in a and x in b and value * a[g] % p != b[x]:
                return None
    if len(a) != len(cols) or len(b) != len(rows):
        return None
    return a, b


def affine_degree_one(values, p):
    items = sorted(values.items())
    x0, y0 = items[0]
    x1, y1 = items[1]
    slope = (y1 - y0) * pow(x1 - x0, -1, p) % p
    intercept = (y0 - slope * x0) % p
    return all((slope * x + intercept) % p == y for x, y in items)


def matrix_rank(matrix, p):
    work = [row[:] for row in matrix]
    rank = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, p)
        work[rank] = [v * inv % p for v in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][col]:
                factor = work[i][col]
                work[i] = [
                    (u - factor * v) % p for u, v in zip(work[i], work[rank])
                ]
        rank += 1
    return rank


def toy_reconstruction():
    # Q(t,X)=X-t on five rows/slopes. Its nonincidence graph is K_5 minus
    # the diagonal, F_t=X-t, G_x=t-x, and theta=-1.
    p = 101
    rows = list(range(5))
    cols = list(range(5))
    theta = {(x, g): p - 1 for x in rows for g in cols if x != g}
    potentials = propagate(rows, cols, theta, p)
    assert potentials is not None
    a, b = potentials
    assert len(set(a.values())) == 1
    assert len(set(b.values())) == 1
    assert next(iter(b.values())) == (p - next(iter(a.values()))) % p

    coeff_x = {g: a[g] for g in cols}
    coeff_0 = {g: (-a[g] * g) % p for g in cols}
    assert affine_degree_one(coeff_x, p)
    assert affine_degree_one(coeff_0, p)

    clean_coeffs = [[(-g) % p, 1] for g in cols]
    saturated_coeffs = [[x, p - 1] for x in rows]
    values = [[(x - g) % p for g in cols] for x in rows]
    assert matrix_rank(clean_coeffs, p) == 2
    assert matrix_rank(saturated_coeffs, p) == 2
    assert matrix_rank(values, p) == 2

    broken = dict(theta)
    broken[(0, 1)] = 2 * broken[(0, 1)] % p
    assert propagate(rows, cols, broken, p) is None

    bad_coeff = dict(coeff_0)
    bad_coeff[4] = (bad_coeff[4] + 1) % p
    assert not affine_degree_one(bad_coeff, p)


def main():
    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    contract = (HERE / "claim_contract.md").read_text()
    for needle in (
        "n_Z>2e_*",
        "n_X>2r",
        "theta_(x,gamma)=b_x/a_gamma",
        "lies in RS[Z_cl,e_*+1]",
        "rank C_cl=rank C_sat=rank W_sat,cl=sr(Q)",
        "rank W_sat,cl>=ceil((e+1)/(b+1))>=5",
        "impose the Hankel chain",
    ):
        assert needle in statement
    for needle in (
        "n_Z-2e_*=2e+2b+1-D_*>0",
        "n_X-2r=4e+4b+5-c",
        "spanning-tree propagation",
        "at all `n_Z>e_*` clean slopes",
        "Evaluation on `X_sat`",
    ):
        assert needle in proof
    assert "cycle consistency alone is not sufficient" in contract

    profiles = 0
    for e in range(3, 128):
        for b in range((e - 1) // 5 + 1):
            e_star = e - b
            r = 2 * e_star + 1
            for d_star in (0, 1):
                c_max = e - 5 * b - 1 + d_star
                if c_max < 1:
                    continue
                n_z = 4 * e + 1 - d_star
                for c in range(1, c_max + 1):
                    n_x = 8 * e + 7 - c
                    assert n_z > 2 * e_star
                    assert n_x > 2 * r
                    profiles += 1

    toy_reconstruction()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_ACTIVE_PARTITION_"
        f"INCIDENCE_RECONSTRUCTION_PASS profiles={profiles} toy=1 mutations=2"
    )


if __name__ == "__main__":
    main()
