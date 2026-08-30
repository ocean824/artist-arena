# Artist Arena Canonical Source and Directive Precedence

The file [`ARTIST-ARENA-V1-Master-Specification.md`](ARTIST-ARENA-V1-Master-Specification.md) is a byte-for-byte copy of the supplied `Pasted_content_01.txt`. It is preserved so that founder decisions, original wording, data models, routes, requirements, and historical scope labels remain inspectable.

Its expected SHA-256 digest is:

```text
6fe9ba6637165d43d3ab606e54aaed07104aff69e2b5717046ae26b4d4d18fa5
```

## Authority order

| Priority | Authority | Effect |
|---:|---|---|
| 1 | [`../owner-directives/0001-v1-build-complete.md`](../owner-directives/0001-v1-build-complete.md) | Governs present V1 scope and overrides source statements that postpone, exclude, or limit construction of described capabilities |
| 2 | Canonical master specification | Governs all product and architecture details not overridden by a later owner directive |
| 3 | Approved ADRs and RFCs | Resolve implementation decisions without weakening owner directives or product canon |
| 4 | Derived product, domain, API, schema, security, and roadmap documents | Operationalize the canon and decisions |
| 5 | Issues, pull requests, source code, tests, and deployment artifacts | Implement and prove the approved requirements |

The owner directive does not erase the original specification. It changes the interpretation of maturity and timing language. Blockchain, credit purchase, paid entry, one-to-one wagering, prize pools, cash conversion, payouts, marketplace commerce, and every other described later or gated capability are mandatory V1 build scope. Gates may restrict activation by environment, jurisdiction, identity status, assurance level, provider readiness, or value limit; they may not eliminate construction or end-to-end testing.

Do not edit the canonical file in place. A new source version must be created through an approved owner directive or change process, carry a new checksum, and document its relationship to prior source material.
