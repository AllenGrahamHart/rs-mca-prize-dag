# proof: m720_certificate_semantics

The MITM enumerator proof establishes the contract of `mitm_slice`:

```text
complete = (W == n) and not aborted.
```

It also proves that the enumerator covers exactly anchored trades whose
support lies inside the declared window `[0,W)`. Therefore:

- if `complete=true`, the window is the whole row and the run did not abort,
  so a zero active-core count is a complete-cell zero certificate;
- if `W<n`, the enumerator only covered a proper window, so a zero result is
  slice-local;
- if the run aborted, the enumerator did not finish even that declared
  window, so a zero result is not a complete certificate.

Thus incomplete n=1024 window slices can be used only as local evidence and
cannot be promoted to global zero certificates. This is exactly the
certificate-semantics rule required by the M720 calibration node.
