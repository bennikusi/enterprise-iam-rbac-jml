# AI-Assisted Access Review

## Purpose

This project demonstrates how AI can assist Identity and Access Management (IAM) teams by analyzing access requests, identifying potential risks, and providing recommendations to human IAM reviewers.

AI is used as a decision-support tool. It does not independently approve or provision access.

## Access Request Scenario

**User:** Emily Davis
**Job Title:** Sales Representative
**Department:** Sales
**Requested Resource:** Finance Application
**Requested Group:** `SG-Finance-App`

### Current Access

Emily Davis currently has:

* `SG-M365-Users`
* `SG-VPN-Users`
* `SG-Sales-App`

### Business Justification

Emily requested access to the Finance Application to assist with reviewing sales-related financial information.

## AI Analysis

The AI evaluates the request using:

* User department
* User job title
* Existing group memberships
* Requested application
* Business justification
* Least-privilege principles
* Role-to-access alignment

### AI Risk Assessment

**Risk Level:** Medium

**Finding:** The requested `SG-Finance-App` access does not directly align with Emily Davis's current Sales Representative role.

The user already has access appropriate for the Sales department. Additional Finance application access may introduce unnecessary privileges unless a documented business requirement exists.

### AI Recommendation

**Flag for IAM Review — Do Not Automatically Approve**

The AI recommends that an IAM analyst verify:

1. Whether Emily's Sales responsibilities require Finance Application access.
2. Whether her manager has approved the request.
3. Whether a less-privileged alternative can satisfy the business requirement.
4. Whether the requested access should be temporary or permanent.

## Human IAM Decision

**Decision:** Pending IAM Review

The AI recommendation is advisory only. Final access approval remains with an authorized human IAM reviewer.

## Security Principle

This workflow follows a **human-in-the-loop** model:

```text
Access Request
      ↓
AI Analysis
      ↓
Risk / Recommendation
      ↓
Human IAM Review
      ↓
Approve or Deny
      ↓
Entra ID Provisioning
      ↓
Audit Log
```

## Expected Outcome

The AI should prevent inappropriate access from being automatically granted by identifying role-to-access mismatches before provisioning.

This demonstrates how AI can improve IAM review efficiency while maintaining human oversight and traditional access-control safeguards.

## Skills Demonstrated

* Identity and Access Management
* Microsoft Entra ID
* Role-Based Access Control (RBAC)
* Least Privilege
* Access Request Review
* AI-Assisted Security Analysis
* Human-in-the-Loop Security
* Access Governance
* Security Risk Assessment
* Auditability
