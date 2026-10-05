# AI Access Review Engine

## Objective

The AI Access Review Engine evaluates IAM access requests and identifies potential risks before access is provisioned.

The engine considers:

* User role
* Department
* Existing access
* Requested access
* Business justification
* Least-privilege requirements

## Decision Model

The AI produces one of three recommendations:

| Recommendation | Meaning                                                   |
| -------------- | --------------------------------------------------------- |
| Approve        | Request appears consistent with the user's role           |
| Review         | Request may require additional validation                 |
| Deny           | Request presents a significant role or privilege mismatch |

### Example

**User:** Emily Davis
**Role:** Sales Representative
**Department:** Sales
**Requested Access:** `SG-Finance-App`

**AI Recommendation:** REVIEW

**Reason:** Finance application access does not directly align with the user's current Sales role and may introduce unnecessary privileges.

## Human-in-the-Loop Control

The AI recommendation does not directly modify Microsoft Entra ID.

The final decision must be made by an authorized IAM reviewer.

```text
Access Request
      ↓
AI Risk Analysis
      ↓
Recommendation
      ↓
Human IAM Review
      ↓
Approve / Deny
      ↓
Entra ID
      ↓
Audit Log
```

## Security Controls

The design follows:

* Least Privilege
* Role-Based Access Control (RBAC)
* Separation of Duties
* Human Approval
* Auditability
* Access Governance

## Future Automation

This prototype can be extended using:

* Microsoft Graph API
* PowerShell
* Python
* Microsoft Entra ID
* Azure Logic Apps
* Large Language Models (LLMs)

The future automation layer could retrieve access requests, analyze them, generate risk explanations, and route flagged requests to IAM personnel for approval.
