#!/usr/bin/env python3
"""Exact checker for E1 N'=256 box-witness campaign results."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_RESULT = ROOT / "experiments/prize_resolution/e1_n256_box_witness_result.json"

P = 904625697166646869347790708689937759412227977745095982970820953353127723009
RHO = 368095729527972287347366462180303065908636718991804826343652948937354262881
N = 128
SEEDS = {1729, 2718, 31415, 65537}


def check_vector(vector):
    if not isinstance(vector, list) or len(vector) != N:
        raise ValueError("vector must have length 128")
    if any(not isinstance(value, int) for value in vector):
        raise ValueError("vector entries must be integers")
    if not any(vector):
        raise ValueError("zero vector is not a falsifier")
    if max(abs(value) for value in vector) > 2:
        raise ValueError("vector leaves the coefficient box")
    residue = sum(
        value * pow(RHO, index, P) for index, value in enumerate(vector)
    ) % P
    if residue:
        raise ValueError(f"nonzero folded-kernel residue {residue}")
    return {
        "support": sum(value != 0 for value in vector),
        "norm2": sum(value * value for value in vector),
        "inf_norm": max(abs(value) for value in vector),
    }


def check_campaign(data):
    if data.get("schema") != "e1-n256-box-falsifier-campaign-v1":
        raise ValueError("campaign schema mismatch")
    workers = data.get("workers")
    if not isinstance(workers, list) or not workers:
        raise ValueError("missing worker records")
    witnesses = []
    seen_seeds = set()
    for worker in workers:
        if worker.get("schema") != "e1-n256-box-falsifier-v1":
            raise ValueError("worker schema mismatch")
        status = worker.get("status")
        seed = worker.get("seed")
        if seed in seen_seeds or seed not in SEEDS:
            raise ValueError("worker seed coverage mismatch")
        seen_seeds.add(seed)
        if status != "ERROR_OR_TIMEOUT":
            if worker.get("p") != str(P) or worker.get("rho_256") != str(RHO):
                raise ValueError("worker field/root mismatch")
            if worker.get("dimension") != N:
                raise ValueError("worker dimension mismatch")
            elapsed = worker.get("elapsed_seconds")
            if not isinstance(elapsed, (int, float)) or not 0 <= elapsed <= 240:
                raise ValueError("worker elapsed-time contract mismatch")
            stages = worker.get("stages")
            if not isinstance(stages, list) or not stages:
                raise ValueError("worker stage summaries missing")
            for stage in stages:
                if stage.get("label") not in {"LLL", "BKZ-28", "BKZ-36", "BKZ-42"}:
                    raise ValueError("unknown worker stage")
                if not all(key in stage for key in ("best_norm2", "best_inf", "best_pair_inf")):
                    raise ValueError("incomplete worker stage summary")
        if status == "WITNESS":
            summary = check_vector(worker.get("vector"))
            for key, value in summary.items():
                if worker.get(key) != value:
                    raise ValueError(f"worker {key} mismatch")
            witnesses.append((worker.get("seed"), summary))
        elif status not in {"NO_WITNESS_WITHIN_SEARCH_BUDGET", "ERROR_OR_TIMEOUT"}:
            raise ValueError(f"unknown worker status {status!r}")
    if seen_seeds != SEEDS:
        raise ValueError("campaign did not cover every pinned seed")
    return witnesses, len(workers)


def self_test():
    rejected = 0
    mutations = [
        [0] * N,
        [3] + [0] * (N - 1),
        [1] + [0] * (N - 1),
        [0] * (N - 1),
    ]
    for mutation in mutations:
        try:
            check_vector(mutation)
        except ValueError:
            rejected += 1
    if rejected != len(mutations):
        raise RuntimeError("self-test accepted a hostile mutation")
    base_worker = {
        "schema": "e1-n256-box-falsifier-v1",
        "status": "NO_WITNESS_WITHIN_SEARCH_BUDGET",
        "p": str(P),
        "rho_256": str(RHO),
        "dimension": N,
        "elapsed_seconds": 1.0,
        "stages": [
            {"label": "LLL", "best_norm2": 1000, "best_inf": 10, "best_pair_inf": 8}
        ],
    }
    valid = {
        "schema": "e1-n256-box-falsifier-campaign-v1",
        "workers": [dict(base_worker, seed=seed) for seed in sorted(SEEDS)],
    }
    check_campaign(valid)
    campaign_mutations = []
    for change in ("schema", "duplicate", "prime", "status"):
        mutated = json.loads(json.dumps(valid))
        if change == "schema":
            mutated["schema"] = "wrong"
        elif change == "duplicate":
            mutated["workers"][1]["seed"] = mutated["workers"][0]["seed"]
        elif change == "prime":
            mutated["workers"][0]["p"] = str(P + 1)
        else:
            mutated["workers"][0]["status"] = "CERTIFIED"
        campaign_mutations.append(mutated)
    campaign_rejected = 0
    for mutation in campaign_mutations:
        try:
            check_campaign(mutation)
        except ValueError:
            campaign_rejected += 1
    if campaign_rejected != len(campaign_mutations):
        raise RuntimeError("campaign self-test accepted a hostile mutation")
    print(
        "E1_N256_BOX_CHECK_SELFTEST_PASS "
        f"vector_mutations={rejected} campaign_mutations={campaign_rejected}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("result", nargs="?", type=Path, default=DEFAULT_RESULT)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    data = json.loads(args.result.read_text(encoding="utf-8"))
    witnesses, workers = check_campaign(data)
    status = "FALSIFIED" if witnesses else "INCOMPLETE"
    print(
        f"E1_N256_BOX_CAMPAIGN_AUDIT status={status} "
        f"workers={workers} witnesses={len(witnesses)}"
    )
    for seed, summary in witnesses:
        print(f"witness seed={seed} {summary}")


if __name__ == "__main__":
    main()
