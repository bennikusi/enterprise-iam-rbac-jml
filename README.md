# Enterprise IAM, RBAC & JML Lifecycle Management

![Microsoft Entra ID](https://img.shields.io/badge/Microsoft%20Entra%20ID-IAM-blue)
![IAM](https://img.shields.io/badge/Domain-Identity%20%26%20Access%20Management-purple)
![RBAC](https://img.shields.io/badge/Access%20Control-RBAC-green)
![JML](https://img.shields.io/badge/Lifecycle-JML-orange)

## Project Overview

This project is a hands-on enterprise Identity and Access Management (IAM) laboratory built using Microsoft Entra ID.

The environment simulates identity management for **Apex Technology Solutions**, a fictional organization with approximately 250 employees.

The project demonstrates how an IAM analyst can manage employee identities and access throughout the Joiner-Mover-Leaver (JML) lifecycle while applying Role-Based Access Control (RBAC), least privilege, group-based access management, MFA security controls, and account deprovisioning.

---

## Business Scenario

Apex Technology Solutions requires a centralized identity and access management process for its workforce.

The IAM environment must support:

- New employee onboarding
- Role-based access assignment
- Employee role changes
- Access modification during transfers and promotions
- Employee offboarding
- Access removal
- Authentication security
- Least-privilege access

Microsoft Entra ID was used as the identity platform for this laboratory implementation.

---

## Architecture

```text
                    Apex Technology Solutions
                              |
                              v
                    Microsoft Entra ID
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
        User Identity    Security Groups   Authentication
              |               |               |
              |               |               +--> Security Defaults
              |               |
              |               +--> SG-M365-Users
              |               +--> SG-HR-App
              |               +--> SG-VPN-Users
              |               +--> SG-HR-Managers
              |
              v
       JML Lifecycle Management
              |
      +-------+-------+
      |       |       |
      v       v       v
    Joiner  Mover   Leaver
