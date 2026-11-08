# Kense

**AI OS.** One API key for heterogeneous compute, models, agents, apps and data capabilities.

Kense is an operating plane, not an AI application framework. It owns placement, isolation, routing, metering, audit and release; inference stays in the engines and workloads stay in their sandboxes.

## Architecture

![AI OS layered architecture — one key through the unified gateway into nine services, five cross-cutting planes, and the heterogeneous resource pool](docs/ai-os-architecture.png)

[Vector source](docs/ai-os-architecture.svg)

The supply side feeds the product side: `IaaS → MaaS → TaaS → PaaS / AaaS → SaaS`. Actions, Packages and Releases cut across every layer and ship changes through one primitive — **immutable version → alias → traffic weight** — so rollout and rollback work the same way everywhere.

One credential, one chain. The primary key is presented once at the gateway and exchanged for a short-lived scoped credential; downstream services never see it and sandboxes hold none. Capabilities register as URNs before exposure, and every request emits one metered event, so identity, quota, budget, audit and billing share a single chain.

## What each layer owns

| Layer | Owns |
| --- | --- |
| IaaS | Accelerator inventory, quotas, node agents, leases |
| MaaS | Model catalog, artifact distribution, placement, OpenAI-compatible inference |
| TaaS | Training jobs, datasets, adapters, production traces back to training |
| PaaS | Builds, immutable releases, rollout and rollback |
| AaaS | Agent runtime, sessions, tool calls, zero-credential sandboxes |
| SaaS | Product surfaces built on the layers above |
| Gateway | Model, API and MCP routing; auth, rate limits, per-request policy |
| Control plane | Tenancy, service catalog, metering, append-only audit, secrets |
| Actions / Packages / Releases | Build, store and ship immutable versions across the supply chain |

## Start here

- **Get a build** — product distributions ship from [Releases](https://github.com/kense-labs/kense/releases/latest).
- **Find the source** — public repositories are listed below; this repository contains documentation only.
- **Read the contract** — the architecture diagram above is the canonical shape of the system.

## Repositories

| Repository | What it is |
| --- | --- |
| [ksandbox](https://github.com/kense-labs/ksandbox) | Rust-native, fail-closed process sandbox for agent tool calls |
| [dsh-acp](https://github.com/kense-labs/dsh-acp) | ACP-only DeepSeek Harness distribution; public container image |
| [dsh-gpui](https://github.com/kense-labs/dsh-gpui) | Desktop GPUI client for DeepSeek Harness |
| [KUI](https://github.com/kense-labs/KUI) | Rust UI kit for GPUI, native desktop and WASM web |
| [kense-labs.github.io](https://github.com/kense-labs/kense-labs.github.io) | Organization website |

## Boundaries

No prompt registry, hosted vector store, standalone LLMOps product, visual orchestrator or marketplace. Those are applications, not operating-system primitives.

## License

[MIT](LICENSE). Each component repository carries its own license.
