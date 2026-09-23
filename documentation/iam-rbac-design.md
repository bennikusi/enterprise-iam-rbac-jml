# IAM & RBAC Design

## Project Overview

This project simulates an enterprise Identity and Access Management (IAM) environment for Apex Technology Solutions, a fictional organization with approximately 250 employees.

The lab demonstrates how identity and access can be managed using Microsoft Entra ID through centralized user provisioning, role-based access control (RBAC), security groups, least-privilege access, and identity lifecycle management.

## Environment

**Identity Platform:** Microsoft Entra ID  
**Organization:** Apex Technology Solutions  
**Environment Type:** Simulated enterprise IAM laboratory  
**Primary IAM Model:** Group-based RBAC  
**Security Model:** Least privilege

## RBAC Strategy

Access is assigned through security groups rather than directly assigning permissions to individual users.

| Security Group | Purpose |
|---|---|
| SG-M365-Users | Standard Microsoft 365 access |
| SG-HR-App | Human Resources application access |
| SG-VPN-Users | Remote VPN access |
| SG-HR-Managers | Elevated access for HR management |

This approach allows access to be managed consistently as employees join the organization, change roles, or leave.

## Example User

**Employee:** Sarah Johnson  
**Initial Role:** HR Specialist  
**Department:** Human Resources  
**Office:** New York

### Initial Access

Sarah was assigned:

- SG-M365-Users
- SG-HR-App
- SG-VPN-Users

She was not assigned:

- SG-HR-Managers

This demonstrates role-based access based on the employee's job responsibilities.

## Least Privilege

The lab applies the principle of least privilege by granting users only the access required for their current responsibilities.

For example, Sarah initially received standard HR access but did not receive HR management privileges.

When her responsibilities changed, her access was modified rather than simply accumulating additional permissions.

## Role Change

Sarah was promoted from **HR Specialist** to **HR Manager**.

The access model was updated by:

1. Removing `SG-HR-App`
2. Adding `SG-HR-Managers`
3. Retaining `SG-M365-Users`
4. Retaining `SG-VPN-Users`

This demonstrates a controlled access change during the employee lifecycle.

## Access Governance

Using security groups for access assignment provides several benefits:

- Consistent access provisioning
- Easier access reviews
- Reduced direct permission assignments
- Simplified onboarding and offboarding
- Improved auditability
- Easier enforcement of least privilege

## Evidence

The implementation is supported by screenshots in the `/screenshots` directory.

Relevant evidence includes:

- Entra tenant configuration
- User provisioning
- Security group configuration
- User-to-group access assignments
- JML mover scenario
- Account disabling
- Access removal
- MFA security configuration

## Skills Demonstrated

- Microsoft Entra ID
- Identity and Access Management (IAM)
- Role-Based Access Control (RBAC)
- Least Privilege
- Security Groups
- User Provisioning
- Access Management
- Identity Lifecycle Management
- Access Governance
- MFA Security Controls
