# Audit

1. The upstream Python verifier was rerun at the exact commit and passed all
   29 semantic mutations; optimized execution failed closed as required.
2. Seven direct cells, transport, import, and both standalone parity
   derivations were rerun under Sage 10.9. These prove ten cells separately.
3. `M01-R11` reached external Singular `slimgb` completion but failed while
   Sage converted the returned large polynomial basis. The same exception
   occurred under conda Sage 10.7, conda Sage 10.9, and official Sage 10.9.
4. Replacing only the two external backend selectors by the mathematically
   equivalent in-process `libsingular:slimgb` avoided the conversion failure
   but exceeded the bounded 1740-second subprocess cap.
5. No result from a failed or timed-out run is promoted. The residual gate is
   exactly `M01-R11` and its already checked `M02-R11` literal transport.
6. The claim is cell-local and moves no owner, charge, row, or Prize bound.
7. A direct standalone Singular bridge avoids the Sage conversion entirely.
   Its 1740-second staged replay closes `w=0`, obtains q-slice basis size 168
   and `J` basis size 174, then times out at the `J`-localizer square. A lean
   replay reaches the same two bases and times out reducing `I`.
8. A 3540-second replay splits `I` into 148 deterministic 1024-term blocks.
   It again reaches the same q-slice and `J` metrics but prints fewer than
   eight completed blocks. This is a scaling fence, not proof evidence.
