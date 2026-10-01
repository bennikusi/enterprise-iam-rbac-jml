# Access Request & Approval Workflow

## 1. Purpose

This document defines the access request and approval process used in the Apex Technology Solutions IAM lab.

The workflow is designed to ensure that access is:

- Business justified
- Approved by an appropriate business owner
- Validated against the user's job role
- Granted according to least privilege
- Documented for audit purposes

## 2. Business Scenario

Sarah Johnson is an HR Specialist at Apex Technology Solutions.

Sarah requires access to the organization's HR application to perform her assigned responsibilities.

Requested access:

- Security Group: SG-HR-App
- Access Type: HR Application
- Business Owner: HR Department
- Requestor: Sarah Johnson
- Business Justification: Access required to perform HR-related responsibilities

## 3. Access Request Workflow

The standard workflow is:

1. User or manager submits an access request.
2. The request includes a business justification.
3. The user's manager reviews the request.
4. The manager approves or denies the request.
5. IAM validates the requested access against the user's job role.
6. If approved, IAM assigns the appropriate security group.
7. IAM verifies that the intended access was granted.
8. The request and resulting access change are documented for audit purposes.

## 4. Approval Criteria

Before access is granted, the following questions should be evaluated:

- Does the user require this access for their current job?
- Is the requested access appropriate for the user's department?
- Is there a less-privileged alternative?
- Has the appropriate manager or resource owner approved the request?
- Does the request create a separation-of-duties concern?
- Is the requested access consistent with the user's assigned RBAC role?

## 5. IAM Validation

The IAM administrator validates the request before provisioning access.

For Sarah Johnson, the requested HR application access is consistent with her HR Specialist role.

The appropriate access group is:

`SG-HR-App`

The user should not receive:

`SG-HR-Managers`

unless her job role changes and the appropriate approval is obtained.

## 6. Provisioning Action

After approval, the IAM administrator adds the user to the appropriate security group.

Example:

Sarah Johnson
→ SG-HR-App

Group membership provides a controlled method for managing access to the HR resource.

## 7. Verification

After provisioning, IAM verifies:

- The user is a member of the correct group.
- The user does not have unnecessary privileged groups.
- The requested access matches the approved request.
- The access change is documented.

## 8. Denied Requests

If a request is denied, the administrator documents:

- Requestor
- Requested resource
- Date
- Approver
- Decision
- Reason for denial

Denied requests must not result in access being provisioned.

## 9. Least Privilege

Access is granted according to the minimum permissions required to perform the user's job responsibilities.

For example, an HR Specialist may require:

- SG-HR-App
- SG-M365-Users
- SG-VPN-Users

An HR Specialist should not automatically receive:

- SG-HR-Managers
- Administrative roles
- Privileged directory permissions

Additional access requires a documented business need and appropriate approval.

## 10. Audit Evidence

The following evidence should be retained:

- Access request
- Business justification
- Approval decision
- IAM provisioning action
- Group membership evidence
- Date/time of access change
- Any subsequent access review

## 11. Project Implementation Notes

This project uses Microsoft Entra ID security groups to demonstrate the technical access-control portion of the workflow.

The approval process is documented as an IAM governance workflow rather than represented as a production Entra Governance approval workflow.

Advanced automated approval workflows such as Microsoft Entra entitlement management or Privileged Identity Management require additional licensing and are therefore outside the scope of this Free-tier lab.

## 12. Security Principles Demonstrated

This workflow demonstrates:

- Least privilege
- Role-based access control
- Separation of duties
- Business justification
- Manager approval
- Controlled provisioning
- Access verification
- Auditability
