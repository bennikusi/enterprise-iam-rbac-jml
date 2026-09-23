# Joiner-Mover-Leaver (JML) Workflow

## Overview

The Joiner-Mover-Leaver (JML) model provides a structured approach to managing employee identities throughout the employment lifecycle.

This lab demonstrates all three lifecycle stages using Microsoft Entra ID:

- Joiner — onboarding a new employee
- Mover — changing access when an employee changes roles
- Leaver — disabling the account and removing access when employment ends

The workflow is designed around least privilege and controlled access changes.

## 1. Joiner — Employee Onboarding

### Scenario

Sarah Johnson joins Apex Technology Solutions as an HR Specialist.

**Employee information:**

- Name: Sarah Johnson
- Job Title: HR Specialist
- Department: Human Resources
- Office: New York
- Hire Date: 08/18/2026

### Provisioning Process

A user account was created in Microsoft Entra ID and configured with the employee's organizational information.

Sarah was then assigned access through security groups based on her role.

### Initial Access

| Access Group | Assigned |
|---|---|
| SG-M365-Users | Yes |
| SG-HR-App | Yes |
| SG-VPN-Users | Yes |
| SG-HR-Managers | No |

The employee received the access required for the HR Specialist role while management-level access remained restricted.

### Evidence

`02-user-provisioning-sarah.png`

`04-sarah-rbac-access.png`

---

## 2. Mover — Role Change

### Scenario

Sarah is promoted from HR Specialist to HR Manager.

A role change requires access to be reviewed and adjusted so that the employee receives the permissions required for the new position without retaining unnecessary previous access.

### Access Changes

The following changes were made:

**Removed:**

- SG-HR-App

**Added:**

- SG-HR-Managers

**Retained:**

- SG-M365-Users
- SG-VPN-Users

### Result

Sarah's identity remained active, but her access profile was changed to reflect her new responsibilities.

This demonstrates the principle of modifying access during a role transition rather than continuously accumulating permissions.

### Evidence

`06-jml-mover-hr-manager.png`

---

## 3. Leaver — Employee Offboarding

### Scenario

Sarah leaves Apex Technology Solutions.

The account must no longer provide access to organizational resources.

### Offboarding Process

The following actions were performed:

1. Disabled Sarah's Microsoft Entra ID account.
2. Removed SG-M365-Users.
3. Removed SG-VPN-Users.
4. Removed SG-HR-Managers.
5. Verified that the user no longer retained the previously assigned group access.

### Result

The account was disabled and the user's previously assigned access groups were removed.

This demonstrates a controlled offboarding process designed to reduce the possibility of continued access after an employee leaves.

### Evidence

`07-jml-leaver-account-disabled.png`

`08-jml-leaver-access-removed.png`

---

## JML Control Objectives

| Lifecycle Stage | Primary Objective | Control |
|---|---|---|
| Joiner | Provide required access | User provisioning + RBAC groups |
| Mover | Align access with new responsibilities | Remove/add appropriate groups |
| Leaver | End organizational access | Disable account + remove group memberships |

## Security Principles

### Least Privilege

Users receive access appropriate to their current responsibilities.

### Access Modification

Role changes trigger an access review rather than allowing previous permissions to remain indefinitely.

### Timely Deprovisioning

When an employee leaves, the identity is disabled and access memberships are removed.

### Auditability

Each lifecycle action can be documented and supported with implementation evidence.

## Manual Lab vs. Automated Enterprise Workflow

This project manually demonstrates the JML controls in a Microsoft Entra ID laboratory environment.

In a production environment, organizations can automate JML processes using Microsoft Entra ID Governance Lifecycle Workflows. Microsoft provides workflow templates and tasks for onboarding, role changes, disabling users, and removing group memberships.

This lab focuses on demonstrating the underlying IAM control process rather than claiming that automated Lifecycle Workflows were deployed.

## Skills Demonstrated

- Joiner-Mover-Leaver (JML)
- User Provisioning
- User Deprovisioning
- RBAC
- Least Privilege
- Group-Based Access Control
- Account Lifecycle Management
- Access Removal
- Microsoft Entra ID
- Identity Governance Concepts
- IAM Documentation
