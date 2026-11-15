## Verification Results

Environment:
- Python 3.11.9
- pytest 9.2.0
- Hypothesis 6.170.15

Original application:
- 16 tests executed
- 12 failed
- 4 passed

Fixed application:
- 16 tests executed
- 16 passed
- 0 failed

The Hypothesis tests exposed input-validation weaknesses in
the original application. The fixed application passed all
16 tests.

## Evidence

- Original application fuzz-testing evidence PDF.
- Fixed application fuzz-testing evidence PDF.
- Original and fixed application demonstrations.

Note: Application demonstration pages reconstructed from
the supplied terminal output are labelled accordingly.