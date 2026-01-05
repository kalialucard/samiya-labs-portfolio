---
title: "Example Test: Login Flow"
date: "2026-01-05"
category: "testing"
enrich: true
image: "assets/test-thumb.png"
tags: "qa, security"
description: "Security assessment of the new login flow."
---

# Test Log: Login Flow

> **Scope**: Auth Service
> **Date**: 2026-01-05

## Findings
### [Low] Missing Rate Limiting
The login endpoint allows unlimited attempts.

**Recommendation**:
Implement exponential backoff.
