# Tegrastats-Exporter
This program simply parses a log of tegrastats output, and provides a CSV with human readable names.

# Dependencies
This program aims to use base python libraries, but for the sake of completeness, here's the full list of dependencies (you should NOT need to install anything)

- abc
- argparse
- csv
- re
- typing

# Supported Versions
## Tegrastats
Unfortunately, tegrasats does not provide a version number that I can find anywhere (at least for the builds I'm using).

As a intermediate step, known working SHA-1 hashes of the binary are listed below by architecture

### aarch64
- 07544736a44228416de7023ebd8441c3252cd33c

## Python
- 3.10.11
- 3.9.16
