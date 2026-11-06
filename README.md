# kense

Kense Labs main repository. Product distributions are published as GitHub Releases.

## Current releases

- **kbox 3.2.7 — macOS (Apple Silicon)**: local Agent Runtime and OCI workload execution (MicroVM, Docker-compatible CLI). Download `kbox-3.2.7-macos-arm64.tar.gz` from the release page and run the bundled `install.sh`.

Related repositories:

- [kbox](https://github.com/kense-labs/kbox) — runtime source code
- [dsh-acp](https://github.com/kense-labs/dsh-acp) — ACP-only DeepSeek Harness distribution; public container image at `ghcr.io/kense-labs/dsh-acp:latest`

## Website

This repository publishes the [Kense organization website](https://kense-labs.github.io/kense/) with GitHub Pages. The site source, component documentation and release build live in [kense-labs/KUI](https://github.com/kense-labs/KUI).

The [publishing workflow](.github/workflows/publish.yml) checks for a new KUI release every five minutes and verifies its SHA-256 checksum before deploying it to GitHub Pages.
