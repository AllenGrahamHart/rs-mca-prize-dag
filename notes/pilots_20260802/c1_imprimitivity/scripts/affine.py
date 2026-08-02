#!/usr/bin/env python3
"""Support-orbit reduction for the ternary max-norm problem in R_N = Z[x]/(x^N+1).

THE REDUCTION (exact, proved here; validated exhaustively in calib.py)
----------------------------------------------------------------------
The norm-preserving, ternariness-preserving, weight-preserving group of the
prior pilot is  G = <U, Gal>  with

    U   = {+- x^c : 0 <= c < N}                 (order 2N)
    Gal = {x -> x^u : u in (Z/2N)^*}            (order phi(2N) = N)

Every element of G is a SIGNED PERMUTATION of the monomial basis
x^0, ..., x^(N-1).  Discard the signs and look only at the induced permutation
of the index set Z/N:

    x^c  :  i -> i + c            (mod N)   [x^i -> +-x^(i+c mod N)]
    x^u  :  i -> u * i            (mod N)   [x^i -> +-x^(u i mod N); u odd
                                             mod 2N, and u mod N is odd, and
                                             every odd residue mod N arises]

So the induced action on the SUPPORT of f is exactly the affine group

    Aff(N) = { i -> u i + c :  u in (Z/N)^*_odd,  c in Z/N },    |Aff| = N^2/2.

Consequence used everywhere below:

    max { Norm(f) : f ternary, weight w }
      = max { Norm(f) : supp(f) in R,  signs arbitrary with the sign at the
                        least support index pinned to +1 }

where R is ANY set of representatives for the Aff(N)-orbits of w-subsets of
Z/N.  (Given f, move supp(f) onto its representative by some g in G -- Norm and
weight are preserved and gf is still ternary -- then negate if needed.  Negation
lies in U and fixes the support.)

For N = 32 this is a factor  |Aff| * 2 = 512 * 2 = 1024  saving over the naive
3^N enumeration restricted to weight w, and a factor 16 over the prior pilot's
d_0 = +1 slice (which quotients only by U and only by a factor of 2N/w).

Counts at N = 32:                   naive C(32,w) 2^w      here
    w = 8      2 692 684 800                            ~2.6e6
    w = 9      7 180 492 800                            ~1.4e7
    w = 10    16 515 133 440                            ~6.5e7
"""

from __future__ import annotations

import numpy as np


# ------------------------------------------------------------ subset masks ---

def combo_masks(n: int, k: int, _memo=None) -> np.ndarray:
    """All k-subsets of {0,...,n-1} as bitmasks (uint64), ascending."""
    if _memo is None:
        _memo = {}
    key = (n, k)
    if key in _memo:
        return _memo[key]
    if k == 0:
        out = np.zeros(1, dtype=np.uint64)
    elif k > n:
        out = np.zeros(0, dtype=np.uint64)
    else:
        parts = [combo_masks(j, k - 1, _memo) | np.uint64(1) << np.uint64(j)
                 for j in range(k - 1, n)]
        out = np.concatenate(parts) if parts else np.zeros(0, dtype=np.uint64)
    _memo[key] = out
    return out


BLOCK = 1_000_000          # memory ceiling knob for combo_blocks / affine_reps


def combo_blocks(n: int, k: int, block: int = BLOCK):
    """Yield the k-subsets of {0,...,n-1} as bitmask arrays of size <= ~block.

    Recurses on the largest element until the remaining sub-problem fits, so
    peak memory is O(block) regardless of C(n,k).
    """
    from math import comb
    if k < 0 or k > n:
        return
    if comb(n, k) <= block:
        yield combo_masks(n, k)
        return
    for t in range(k - 1, n):
        bit = np.uint64(1) << np.uint64(t)
        for sub in combo_blocks(t, k - 1, block):
            yield sub | bit


def masks_to_positions(masks: np.ndarray, N: int, w: int) -> np.ndarray:
    """(M,) masks -> (M, w) int64 sorted support positions."""
    bits = ((masks[:, None] >> np.arange(N, dtype=np.uint64)[None, :])
            & np.uint64(1)).astype(np.int8)
    assert (bits.sum(axis=1) == w).all()
    pos = np.argsort(-bits, axis=1, kind="stable")[:, :w]
    return np.sort(pos, axis=1)


# --------------------------------------------------------------- rotations ---

def _rotl(masks: np.ndarray, r: int, N: int) -> np.ndarray:
    full = (np.uint64(1) << np.uint64(N)) - np.uint64(1)
    r = r % N
    if r == 0:
        return masks
    return ((masks << np.uint64(r)) | (masks >> np.uint64(N - r))) & full


def canon_rot(masks: np.ndarray, N: int) -> np.ndarray:
    out = masks.copy()
    for r in range(1, N):
        np.minimum(out, _rotl(masks, r, N), out=out)
    return out


def _apply_perm(masks: np.ndarray, perm: list[int], N: int) -> np.ndarray:
    out = np.zeros_like(masks)
    one = np.uint64(1)
    for i in range(N):
        bit = (masks >> np.uint64(i)) & one
        out |= bit << np.uint64(perm[i])
    return out


def affine_reps(N: int, w: int) -> np.ndarray:
    """A COVERING set of representatives for the Aff(N)-orbits of w-subsets of
    Z/N (as bitmasks): every orbit contains at least one listed mask.

    Exactly-one-per-orbit is NOT claimed (and is not needed for maximisation);
    `validate_reps.py` checks the covering property against an independent
    brute-force enumeration of full affine orbits.

    Memory-safe: every rotation class has a member containing index 0, and the
    (w-1)-subsets of {1..N-1} are generated in chunks indexed by their largest
    element, each chunk rotation-canonicalised and merged.
    """
    if w == 0:
        return np.zeros(1, dtype=np.uint64)
    if w == 1:
        return np.ones(1, dtype=np.uint64)
    reps = np.zeros(0, dtype=np.uint64)
    pending = []
    npend = 0
    for sub in combo_blocks(N - 1, w - 1, BLOCK):   # (w-1)-subsets of {0..N-2}
        m = (sub << np.uint64(1)) | np.uint64(1)    # shift to {1..N-1}, add bit 0
        chunk = np.unique(canon_rot(m, N))
        del m
        pending.append(chunk)
        npend += chunk.size
        if npend >= BLOCK:
            reps = np.unique(np.concatenate([reps] + pending))
            pending = []; npend = 0
    if pending:
        reps = np.unique(np.concatenate([reps] + pending))
    del pending
    for u in range(3, N, 2):
        perm = [(u * i) % N for i in range(N)]
        cand = canon_rot(_apply_perm(reps, perm, N), N)
        np.minimum(reps, cand, out=reps)
    return np.unique(reps)


def sign_patterns(k: int) -> np.ndarray:
    """(2^k, k) int8 matrix of all +-1 patterns."""
    if k == 0:
        return np.zeros((1, 0), dtype=np.int8)
    idx = np.arange(1 << k, dtype=np.int64)
    bits = ((idx[:, None] >> np.arange(k)[None, :]) & 1).astype(np.int8)
    return (1 - 2 * bits).astype(np.int8)


def build_block(pos: np.ndarray, S: np.ndarray, N: int) -> np.ndarray:
    """pos (B, w) supports, S (T, w-1) signs -> (B*T, N) int8 ternary vectors.

    The sign at the least support index is pinned to +1 (global negation).
    """
    B, w = pos.shape
    T = S.shape[0]
    d = np.zeros((B, T, N), dtype=np.int8)
    rows = np.arange(B)[:, None, None]
    cols = np.arange(T)[None, :, None]
    d[rows, cols, pos[:, None, 0:1]] = np.int8(1)
    if w > 1:
        d[rows, cols, pos[:, None, 1:]] = S[None, :, :]
    return d.reshape(B * T, N)
