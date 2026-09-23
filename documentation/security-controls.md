# IAM Security Controls

## Overview

This project implements foundational Identity and Access Management (IAM) security controls using Microsoft Entra ID.

The controls focus on authentication security, least privilege, role-based access, account lifecycle management, and access removal.

## 1. Multifactor Authentication

Microsoft Entra Security Defaults were verified and enabled as part of the lab's baseline identity security configuration.

Security Defaults provide baseline protections including:

- Multifactor authentication (MFA) registration
- MFA requirements for administrators
- Blocking legacy authentication
- Blocking device code flow
- Protection for privileged Azure management activities

Security Defaults are available with Microsoft Entra ID Free and provide a baseline security configuration without requiring Conditional Access licensing.

## Evidence

`09-entra-security-defaults-mfa.png`

## 2. Least Privilege

The project applies least privilege by assigning access according to job responsibilities.

Sarah Johnson initially received access appropriate for an HR Specialist and was not assigned the HR Manager group.

When her role changed, access was modified to reflect her new responsibilities.

This prevents unnecessary accumulation of permissions.

## 3. Role-Based Access Control

Access is managed through security groups representing business roles and access requirements.

### Implemented Groups

| Group | Purpose |
|---|---|
| SG-M365-Users | Standard Microsoft 365 access |
| SG-HR-App | HR application access |
| SG-VPN-Users | Remote VPN access |
| SG-HR-Managers | HR management access |

Group-based access provides a scalable way to manage permissions across an organization.

## 4. Identity Lifecycle Management

The project demonstrates the three major identity lifecycle stages:

### Joiner

A new employee account is created and assigned appropriate access.

### Mover

An employee's access is reviewed and modified when their job responsibilities change.

### Leaver

The employee account is disabled and organizational access is removed.

This reduces the risk of stale accounts and unnecessary permissions.

## 5. Account Disablement

During the leaver scenario, Sarah's Microsoft Entra account was disabled.

Disabling the account prevents the identity from continuing normal authentication activity.

## Evidence

`07-jml-leaver-account-disabled.png`

## 6. Access Removal

After the account was disabled, Sarah's organizational security group memberships were removed.

Removed groups included:

- SG-M365-Users
- SG-VPN-Users
- SG-HR-Managers

This provides a second layer of access control beyond simply disabling the account.

## Evidence

`08-jml-leaver-access-removed.png`

## 7. Group-Based Access Governance

Using security groups rather than individually assigning access helps create a more consistent access management model.

Benefits include:

- Standardized access
- Easier access reviews
- Reduced manual permission assignments
- Improved auditability
- Easier onboarding and offboarding
- Better alignment with RBAC

## 8. Administrative Privilege

The lab was administered using a Global Administrator account because the personal Microsoft Entra laboratory environment required elevated administrative permissions for tenant configuration.

In a production environment, administrative privileges should follow the principle of least privilege and be separated according to administrative responsibilities.

The project does not claim that a production privileged-access-management (PAM) solution was implemented.

## 9. Security Control Limitations

This laboratory intentionally uses Microsoft Entra ID capabilities available in the personal lab environment.

The project does not claim implementation of:

- Microsoft Entra ID Governance Lifecycle Workflows
- Conditional Access policies requiring Entra ID P1/P2
- Privileged Identity Management (PIM)
- Production SIEM integration
- Automated provisioning
- Production ServiceNow integration
- Production SailPoint integration

These technologies represent potential next steps for expanding the lab into a more advanced enterprise IAM architecture.

## Control Summary

| Control | Implementation |
|---|---|
| MFA | Microsoft Entra Security Defaults |
| RBAC | Security groups |
| Least Privilege | Role-based group assignments |
| Joiner | User provisioning |
| Mover | Access modification |
| Leaver | Account disablement |
| Access Removal | Security group removal |
| Authentication Protection | Security Defaults |
| Administrative Security | Privilege limitation documented |

## Skills Demonstrated

- Microsoft Entra ID
- IAM Security Controls
- Multifactor Authentication
- RBAC
- Least Privilege
- Identity Lifecycle Management
- User Provisioning
- User Deprovisioning
- Access Governance
- Authentication Security
- Security Documentation
