# Marketplace and Commerce Domain Specification

## 1. Overview

The Marketplace and Commerce domain is a core pillar of the Artist Arena platform. It enables creators to monetize their work, services, and audience access, while providing buyers, fans, and sponsors with a secure, transparent, and regulated environment to transact.

In accordance with Owner Directive 0001, all commerce capabilities—including the native blockchain ledger, credits, cash-in/cash-out, paid entry, wagers, subscriptions, digital products, services, commissions, licenses, and revenue splits—are mandatory V1 architecture, implementation, integration, and test scope. Production activation may be gated by jurisdiction, identity verification, and provider approval, but the complete capability must be built and verifiable.

## 2. Domain Boundaries

The Marketplace and Commerce domain manages creator storefronts, product catalogs, service offerings, and licensing options. It is responsible for processing purchases, subscriptions, and one-off payments using credits or fiat through external adapters. The domain grants, revokes, and verifies user access to digital goods, gated content, and services by managing entitlements. It maintains accurate records of user credit balances, holds, and transaction history within a secure ledger. Furthermore, it calculates earnings, applies the 1% platform fee, distributes splits, and processes cash-outs, while also handling chargebacks, refunds, and user disputes. It provides necessary admin tooling for financial compliance, tax reporting, and fraud management.

This domain interacts heavily with the Identity and Access domain for user verification, KYC/AML checks, and role-based access control. It integrates with the Competition Engine to manage entry fees, prize pools, and wagers. The Media and Content domain is utilized for delivering digital products and gated media. Finally, it integrates with the Blockchain infrastructure for anchoring high-value transactions, licenses, and revenue splits on-chain.

## 3. Core Entities

| Entity | Description |
| :--- | :--- |
| **Listing** | A digital product, service, commission slot, or license offered by a creator. |
| **SubscriptionTier** | A recurring access level defined by a creator, granting specific benefits or content. |
| **Order** | A record of a user's intent to purchase one or more listings, tracking the fulfillment status. |
| **Transaction** | A finalized movement of value, either in credits or fiat, between accounts or external providers. |
| **Entitlement** | A cryptographic or database record granting a user verified access to a specific resource or capability. |
| **SplitTemplate** | A predefined allocation of revenue among multiple creators, stakeholders, or the platform. |
| **Dispute** | A formalized claim regarding a transaction, requiring resolution through moderation or automated rules. |
| **LedgerEntry** | An immutable record of a financial event, such as a credit, debit, hold, or release, ensuring auditability. |

## 4. Product Rules & Policies

A configuration-driven 1% fee is applied to credit-to-cash and cash-to-credit conversions. This is the founder default and must be explicitly accounted for in all relevant transactions. Creators have the autonomy to set their own prices for products, services, and subscriptions, subject to platform minimums and maximums which are configurable per region.

The primary internal unit of account is the "Credit". Fiat values are converted to and from Credits at the time of transaction based on current exchange rates and the application of the 1% platform fee. For commissions and services, funds are held in escrow until deliverables are accepted by the buyer or the designated dispute window expires.

Revenue splits are calculated after platform fees and payment processing costs are deducted. Splits must be executed atomically where possible to ensure all parties receive their correct allocation simultaneously. Digital products are generally non-refundable once accessed, unless proven defective or fraudulent. Services and commissions follow specific milestone-based refund policies agreed upon at the time of the order. High-value licenses, permanent digital product ownership, and complex revenue splits must be anchored to the native blockchain or app-chain for verifiable provenance.

## 5. User Workflows

### 5.1 Creator Storefront Setup

The creator navigates to their Studio dashboard and selects the Storefront configuration section. They must define their default currency and payout preferences, which requires completing the necessary KYC verification steps. Once verified, the creator can create Listings for digital products, services, commissions, or licenses. They configure pricing, inventory limits, and attach SplitTemplates if collaborating with other creators. Finally, the creator publishes the storefront, making the listings available to users.

### 5.2 Purchasing a Digital Product

A buyer views a Listing on a creator's profile or within the global Marketplace. The buyer initiates the checkout process. The system checks the buyer's credit balance; if insufficient, the buyer is prompted to complete a top-up transaction. The buyer confirms the purchase, and the system deducts the required credits, creating an Order and a corresponding Transaction record. The system generates an Entitlement granting the buyer access to the digital product. Simultaneously, the system credits the creator's pending balance, subject to the standard clearing period, and the buyer can immediately access the digital product.

### 5.3 Commissioning a Service

A buyer requests a Commission from a creator, providing a detailed brief of the required work. The creator reviews the brief, negotiates terms if necessary, and accepts the request. The buyer funds the Commission, and the required credits are held securely in escrow. The creator completes and delivers the work. The buyer reviews the deliverables and either accepts them or initiates a dispute. Upon acceptance, the escrowed funds are released to the creator's account.

## 6. State Machines

### 6.1 Order State

| State | Description |
| :--- | :--- |
| `PENDING` | The order is created and awaiting payment confirmation. |
| `PAID` | Payment is successful; the order is awaiting fulfillment (applicable for services or physical goods). |
| `FULFILLED` | The digital entitlement has been granted or the service is completed. |
| `CANCELLED` | The order was cancelled before payment was finalized. |
| `REFUNDED` | The payment has been returned to the buyer. |
| `DISPUTED` | The order is subject to an active dispute requiring resolution. |

### 6.2 Ledger Entry State

| State | Description |
| :--- | :--- |
| `PENDING` | The transaction is initiated and awaiting confirmation from an external provider. |
| `CLEARED` | The funds are confirmed and available for use or withdrawal. |
| `HELD` | The funds are locked, such as in escrow or pending a security review. |
| `REVERSED` | The transaction has been undone due to fraud, chargeback, or administrative action. |

## 7. API Implications

The Commerce API must provide robust, idempotent endpoints for all financial operations to prevent duplicate transactions.

*   `POST /v1/commerce/orders`: Create a new order with specified items and quantities.
*   `POST /v1/commerce/checkout/credits`: Pay for an existing order using the user's credit balance.
*   `POST /v1/commerce/checkout/fiat`: Initiate a fiat payment, returning the necessary provider intent for client-side processing.
*   `GET /v1/commerce/entitlements`: List all access rights currently held by the authenticated user.
*   `POST /v1/commerce/listings`: Create a new product or service listing within a creator's storefront.
*   `POST /v1/commerce/payouts`: Request a cash-out of cleared earnings to a verified external account.

## 8. Security, Privacy, and Compliance

The system must strictly adhere to PCI-DSS standards; it must not store raw Primary Account Number (PAN) data. All fiat processing must utilize tokenized flows via approved external providers, such as Stripe or PayPal. Cash-outs and high-volume transactions mandate robust identity verification. The system must integrate with a reputable KYC/AML provider and maintain comprehensive, tamper-evident audit logs of all verification events.

To prevent abuse, the system must implement velocity limits, anomaly detection algorithms analyzing purchasing patterns, and device fingerprinting to identify suspicious activity. For tax compliance, the system must collect necessary tax information (e.g., W-9/W-8BEN equivalents) from creators and generate required annual statements (e.g., 1099-K) for those exceeding regulatory thresholds.

## 9. Abuse and Failure Modes

A primary abuse vector is credit card fraud, where stolen cards are used to purchase credits, which are then tipped or spent on a colluding creator to cash out the illicit funds. This is mitigated by enforcing clearing periods on earnings, requiring strict KYC on cash-out requests, and implementing real-time fraud scoring on transactions.

Another failure mode is service non-delivery, where a creator accepts commission funds but fails to deliver the agreed-upon work. This risk is managed by holding funds in escrow, utilizing milestone-based payments for larger projects, and maintaining a robust, transparent dispute resolution process.

In the event of a provider outage, such as the primary payment gateway going offline, the system must degrade gracefully. It should queue pending transactions where appropriate, prevent new checkouts that rely on the downed service, and provide clear, reassuring messaging to the user regarding the temporary unavailability.

## 10. Observability and Analytics

The system must track key financial metrics including Gross Merchandise Value (GMV), conversion rates across different checkout flows, average order value, refund rates, and chargeback ratios. Alerting systems must be configured to trigger upon detecting a spike in failed transactions, a high volume of chargebacks, or abnormal patterns in cash-out requests. Crucially, every ledger mutation must be immutably linked to the initiating user, the specific action performed, and a precise timestamp to ensure a complete and reliable audit trail.

## 11. Acceptance Criteria & Definition of Done

The domain is considered complete for V1 when users can successfully purchase credits using a mock or test payment provider, and the 1% conversion fee is accurately calculated and recorded on all relevant conversions. Creators must be able to create and publish digital product listings, and users must be able to purchase these products using credits, subsequently receiving the correct entitlement.

Furthermore, revenue splits must be accurately calculated and distributed to multiple accounts as defined by SplitTemplates. The commission workflow, encompassing escrow, delivery, acceptance, and fund release, must function seamlessly end-to-end. Users must be able to request a cash-out, subject to simulated KYC checks and clearing holds. Administrators require functional tooling to view transaction history, process refunds, and manage disputes. Critical transactions, including licenses and splits, must be successfully anchored to the designated testnet blockchain. Finally, all API endpoints must be covered by comprehensive integration tests simulating edge cases such as insufficient funds and concurrent purchase attempts.

## 12. Unresolved ADRs

The selection of the primary fiat payment processor (e.g., Stripe, Adyen, PayPal) remains unresolved, pending final legal and regional operating review. The exact duration of the default clearing period for creator earnings is currently assumed to be 7-14 days but requires final confirmation. Additionally, the specific blockchain network or Layer 2 solution for anchoring transactions is pending a final decision from the Architecture team.
