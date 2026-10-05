"""
AI-Assisted IAM Access Review Engine

Purpose:
    Analyze an access request and provide an IAM risk recommendation.

The engine is designed as a decision-support tool.
It does NOT automatically provision or remove access.
Final decisions remain with an authorized IAM reviewer.
"""


# Role-to-access baseline
ROLE_ACCESS = {
    "Sales Representative": {
        "department": "Sales",
        "allowed_groups": {
            "SG-M365-Users",
            "SG-VPN-Users",
            "SG-Sales-App"
        }
    },

    "Finance Analyst": {
        "department": "Finance",
        "allowed_groups": {
            "SG-M365-Users",
            "SG-VPN-Users",
            "SG-Finance-App"
        }
    },

    "HR Specialist": {
        "department": "HR",
        "allowed_groups": {
            "SG-M365-Users",
            "SG-VPN-Users",
            "SG-HR-App"
        }
    }
}


def analyze_access_request(
    user_name,
    job_title,
    department,
    requested_group,
    business_justification
):
    """
    Analyze an IAM access request and return a recommendation.
    """

    role = ROLE_ACCESS.get(job_title)

    if not role:
        return {
            "user": user_name,
            "risk": "MEDIUM",
            "recommendation": "REVIEW",
            "reason": "No defined role baseline exists for this job title.",
            "human_review_required": True
        }

    risk = "LOW"
    recommendation = "APPROVE"
    reasons = []

    # Check department alignment
    if department != role["department"]:
        risk = "HIGH"
        recommendation = "REVIEW"
        reasons.append(
            "User department does not match the defined role baseline."
        )

    # Check requested access
    if requested_group not in role["allowed_groups"]:
        risk = "MEDIUM"
        recommendation = "REVIEW"
        reasons.append(
            f"{requested_group} is not part of the normal access baseline "
            f"for {job_title}."
        )

    # Check business justification
    if not business_justification.strip():
        risk = "MEDIUM"
        recommendation = "REVIEW"
        reasons.append(
            "A business justification was not provided."
        )

    if not reasons:
        reasons.append(
            "Requested access aligns with the user's role and department."
        )

    return {
        "user": user_name,
        "risk": risk,
        "recommendation": recommendation,
        "reasons": reasons,
        "human_review_required": recommendation != "APPROVE"
    }


# Test scenario: Sales employee requesting Finance access
result = analyze_access_request(
    user_name="Emily Davis",
    job_title="Sales Representative",
    department="Sales",
    requested_group="SG-Finance-App",
    business_justification=(
        "Emily needs access to financial information "
        "to support sales reporting."
    )
)

print("\n=== AI-ASSISTED IAM ACCESS REVIEW ===")
print(f"User: {result['user']}")
print(f"Risk Level: {result['risk']}")
print(f"Recommendation: {result['recommendation']}")

print("\nReason(s):")
for reason in result["reasons"]:
    print(f"- {reason}")

print(
    f"\nHuman IAM Review Required: "
    f"{result['human_review_required']}"
)
