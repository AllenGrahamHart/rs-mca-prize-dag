"""Bounded Modal falsifier for the E1 N'=256 zero-vector claim."""

import json

import modal


IMAGE = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("libgmp-dev", "libmpfr-dev", "libqd-dev", "pkg-config")
    .pip_install("cython", "cysignals")
    .pip_install("fpylll", "numpy")
)
APP = modal.App("rs-mca-e1-n256-box-falsifier")

P = 904625697166646869347790708689937759412227977745095982970820953353127723009
RHO = 368095729527972287347366462180303065908636718991804826343652948937354262881
N = 128


def _negacyclic_shift(vector, amount):
    out = [0] * N
    for index, value in enumerate(vector):
        target = index + amount
        if target >= N:
            out[target - N] = -value
        else:
            out[target] = value
    return out


def _is_witness(vector):
    return (
        len(vector) == N
        and any(vector)
        and max(abs(value) for value in vector) <= 2
        and sum(value * pow(RHO, index, P) for index, value in enumerate(vector)) % P == 0
    )


@APP.function(image=IMAGE, cpu=8.0, memory=16384, timeout=240)
def search(seed):
    import random
    import time

    import numpy as np
    from fpylll import BKZ, FPLLL, IntegerMatrix, LLL

    started = time.monotonic()
    soft_deadline = 210.0
    rng = random.Random(seed)
    FPLLL.set_random_seed(seed)

    powers = [pow(RHO, index, P) for index in range(N)]
    basis = IntegerMatrix(N, N)
    basis[0, 0] = P
    for index in range(1, N):
        basis[index, index] = 1
        basis[index, 0] = (-powers[index]) % P

    # Deterministic unimodular row mixing gives the seeds genuinely different
    # reduction trajectories without changing the lattice.
    for _ in range(2 * N):
        left = rng.randrange(N)
        right = rng.randrange(N - 1)
        if right >= left:
            right += 1
        sign = -1 if rng.randrange(2) else 1
        for column in range(N):
            basis[left, column] = int(basis[left, column]) + sign * int(
                basis[right, column]
            )

    stages = []

    def inspect(label):
        rows = [[int(basis[row, column]) for column in range(N)] for row in range(N)]
        rows.sort(key=lambda row: (sum(value * value for value in row), max(abs(v) for v in row)))
        best = rows[0]
        record = {
            "label": label,
            "elapsed_seconds": round(time.monotonic() - started, 6),
            "best_norm2": sum(value * value for value in best),
            "best_inf": max(abs(value) for value in best),
        }
        for row in rows[:16]:
            if _is_witness(row):
                record["search"] = "basis-row"
                stages.append(record)
                return row

        # Multiplication by rho is a negacyclic coordinate shift, so every
        # shifted row remains an exact lattice vector. Search signed sums of
        # shifts from the eight shortest rows.
        pool = []
        for row in rows[:8]:
            for amount in range(N):
                shifted = _negacyclic_shift(row, amount)
                pool.append(shifted)
                pool.append([-value for value in shifted])
        array = np.asarray(pool, dtype=np.int64)
        record["pool_size"] = int(array.shape[0])

        best_pair_inf = None
        near_pairs = {}
        for index in range(array.shape[0]):
            sums = array + array[index]
            infs = np.max(np.abs(sums), axis=1)
            nonzero = np.any(sums != 0, axis=1)
            hits = np.flatnonzero((infs <= 2) & nonzero)
            if hits.size:
                vector = [int(value) for value in sums[int(hits[0])]]
                if _is_witness(vector):
                    record["search"] = "signed-shift-pair"
                    record["pair_indices"] = [index, int(hits[0])]
                    stages.append(record)
                    return vector
            local = int(np.min(infs[nonzero])) if np.any(nonzero) else None
            if local is not None:
                best_pair_inf = local if best_pair_inf is None else min(best_pair_inf, local)
            # Retain a bounded exact near-pair frontier for a third summand.
            for hit in np.flatnonzero((infs <= 5) & nonzero)[:8]:
                vector = tuple(int(value) for value in sums[int(hit)])
                near_pairs.setdefault(vector, int(infs[int(hit)]))
            if len(near_pairs) >= 1200 or time.monotonic() - started > soft_deadline:
                break

        record["best_pair_inf"] = best_pair_inf
        record["near_pair_count"] = len(near_pairs)
        near = sorted(
            near_pairs,
            key=lambda vector: (max(abs(value) for value in vector), sum(v * v for v in vector)),
        )[:600]
        for pair_index, pair in enumerate(near):
            sums = array + np.asarray(pair, dtype=np.int64)
            infs = np.max(np.abs(sums), axis=1)
            nonzero = np.any(sums != 0, axis=1)
            hits = np.flatnonzero((infs <= 2) & nonzero)
            if hits.size:
                vector = [int(value) for value in sums[int(hits[0])]]
                if _is_witness(vector):
                    record["search"] = "signed-shift-triple"
                    record["triple_indices"] = [pair_index, int(hits[0])]
                    stages.append(record)
                    return vector
            if time.monotonic() - started > soft_deadline:
                break
        stages.append(record)
        print(json.dumps({"seed": seed, "stage": record}), flush=True)
        return None

    LLL.reduction(basis, delta=0.99)
    witness = inspect("LLL")
    if witness is None and time.monotonic() - started < 150:
        BKZ.reduction(basis, BKZ.Param(block_size=28, max_loops=2))
        witness = inspect("BKZ-28")
    if witness is None and time.monotonic() - started < 175:
        BKZ.reduction(basis, BKZ.Param(block_size=36, max_loops=1))
        witness = inspect("BKZ-36")
    if witness is None and time.monotonic() - started < 195:
        BKZ.reduction(basis, BKZ.Param(block_size=42, max_loops=1))
        witness = inspect("BKZ-42")

    status = "WITNESS" if witness is not None else "NO_WITNESS_WITHIN_SEARCH_BUDGET"
    result = {
        "schema": "e1-n256-box-falsifier-v1",
        "status": status,
        "seed": seed,
        "p": str(P),
        "rho_256": str(RHO),
        "dimension": N,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "stages": stages,
    }
    if witness is not None:
        assert _is_witness(witness)
        result["vector"] = witness
        result["support"] = sum(value != 0 for value in witness)
        result["norm2"] = sum(value * value for value in witness)
        result["inf_norm"] = max(abs(value) for value in witness)
    return result


@APP.local_entrypoint()
def main():
    calls = [search.spawn(seed) for seed in (1729, 2718, 31415, 65537)]
    workers = []
    for seed, call in zip((1729, 2718, 31415, 65537), calls):
        try:
            workers.append(call.get())
        except Exception as error:
            workers.append(
                {
                    "schema": "e1-n256-box-falsifier-v1",
                    "status": "ERROR_OR_TIMEOUT",
                    "seed": seed,
                    "error": str(error)[:500],
                }
            )
    aggregate = {
        "schema": "e1-n256-box-falsifier-campaign-v1",
        "workers": workers,
    }
    print("E1_N256_BOX_RESULTS_START")
    print(json.dumps(aggregate, sort_keys=True))
    print("E1_N256_BOX_RESULTS_END")
