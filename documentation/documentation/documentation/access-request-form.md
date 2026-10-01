# Access Request Form

## Request Information

| Field                  | Details                                            |
| ---------------------- | -------------------------------------------------- |
| Requester              | Sarah Johnson                                      |
| Job Title              | HR Specialist                                      |
| Department             | Human Resources                                    |
| Manager                | Michael Brown                                      |
| Request Date           | 08/20/2026                                         |
| Requested Resource     | HR Application                                     |
| Requested Access Group | SG-HR-App                                          |
| Requested Access Level | Standard User                                      |
| Business Justification | Required to perform HR Specialist responsibilities |

---

## Current Access

| Access Group   | Status       |
| -------------- | ------------ |
| SG-M365-Users  | Assigned     |
| SG-VPN-Users   | Assigned     |
| SG-HR-App      | Not Assigned |
| SG-HR-Managers | Not Assigned |

---

## Business Justification

Sarah Johnson requires access to the HR Application to perform responsibilities associated with her HR Specialist position.

The requested access is limited to the standard HR application functionality required for her role.

No administrative or management-level access is requested.

---

## Manager Approval

**Decision:** Approved

**Approver:** Michael Brown

**Role:** HR Manager

**Approval Date:** 08/20/2026

**Approval Reason:** Access is required for the employee's assigned HR responsibilities.

---

## IAM Review

**IAM Reviewer:** IAM Administrator

### Validation

* Employee identity verified
* Department verified
* Job role verified
* Business justification reviewed
* Existing access reviewed
* Requested access aligned with job responsibilities
* Least privilege considered
* No elevated administrative access requested

### IAM Decision

**Approved for Provisioning**

### Provisioning Method

Microsoft Entra ID security group assignment:

`SG-HR-App`

---

## Provisioning

**User:** Sarah Johnson

**Group Added:** `SG-HR-App`

**Access Level:** Standard User

**Provisioning Status:** Completed

---

## Verification

The IAM administrator verified that:

* Sarah Johnson was added to `SG-HR-App`.
* The requested HR application access was provisioned.
* No unauthorized administrative groups were assigned.
* The provisioned access matched the approved request.

**Verification Status:** Passed

---

## Closure

**Request Status:** Closed

**Completion Date:** 08/20/2026

**IAM Control:** Access was requested, approved, reviewed, provisioned, and verified before closure.
