# Audit

- Checked the sign normalization: `A=H+S_Phi`, `B=-S_Phi`, and
  `E_d(S_Phi)=Phi+d`.
- Checked that the full gcd is exactly `D`, including cases where `D` shares
  a root with one same-side factor; coprimality of `U,V` is the only required
  cancellation input.
- Kept base-field splitting separate from fourth-power reconstruction, and
  kept the harmonic deleted-root matching separate from both.
- Kept exact degree `deg Phi=d-4`; it forces the lower quotient to have the
  required degree `4r-4`.
- The official implementation warning is load-bearing: use a symbolic
  recurrence or succinct cover representation, never a dense length-`d`
  vector.
- No Modal or other remote computation was used.
