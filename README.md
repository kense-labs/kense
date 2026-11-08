# kense

**AI OS.** One API key for heterogeneous compute, models, agents, apps and data capabilities.

kense is a control plane, not an AI application framework. It owns placement, isolation, routing, metering, audit and release. Inference stays in the engines; workloads stay in their sandboxes.

## Architecture

![AI OS layered architecture — one key through the unified gateway into nine services, five cross-cutting planes, and the heterogeneous resource pool](docs/ai-os-architecture.png)

[Vector source](docs/ai-os-architecture.svg)

The supply side feeds the product side: `IaaS → MaaS → TaaS → PaaS / AaaS → SaaS`. Actions, Packages and Releases cut across every layer and ship changes as **immutable version → alias → traffic weight**, so rollout and rollback use one primitive everywhere.

Trust stops at the edge. The primary key is presented once at the gateway and exchanged for a short-lived scoped credential; downstream services never see it. Sandboxes hold no credentials — the egress gateway injects a secret reference on their behalf.

Capabilities register as URNs before they are exposed, declaring protocol, metering unit, quota dimension, scope and audit level. Every request emits one metered event, so identity, quota, budget, audit and billing form a single chain instead of five disconnected systems.

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

- **Get a build** — product distributions ship from [Releases](https://github.com/kense-labs/kense/releases/latest). This repository holds no binaries; use the latest release page rather than a pinned version, which goes stale.
- **Find the source** — the public repositories are listed below. Components that are still private are intentionally not linked here.
- **Read the design** — the diagram above is the contract. Code names describe responsibilities, not the product brand.

## Repositories

| Repository | What it is |
| --- | --- |
| [ksandbox](https://github.com/kense-labs/ksandbox) | Rust-native, fail-closed process sandbox for agent tool calls |
| [dsh-acp](https://github.com/kense-labs/dsh-acp) | ACP-only DeepSeek Harness distribution; public container image |
| [dsh-gpui](https://github.com/kense-labs/dsh-gpui) | Desktop GPUI client for DeepSeek Harness |
| [KUI](https://github.com/kense-labs/KUI) | Rust UI kit for GPUI, native desktop and WASM web |
| [kense-labs.github.io](https://github.com/kense-labs/kense-labs.github.io) | Organization website |

## Principles

- **One credential, one chain** — a single key carries identity, quota, budget, audit and billing across all services.
- **Brand-neutral code** — source names describe responsibilities; product identity lives in packaging, not in modules or wire values.
- **Facts before claims** — no version numbers, no private links, no capabilities that cannot be verified from a public artifact.
- **Explicit boundaries** — no prompt registry, hosted vector store, standalone LLMOps product, visual orchestrator or marketplace. Those are applications, not operating-system primitives.

## About this repository

This is the organization entry point: architecture, release index and source map. It contains no product code. Licensing is defined per repository in its own LICENSE file.
