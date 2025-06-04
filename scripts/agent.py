import json
import os

QUESTIONS = {
    "credentials_file": {
        "prompt": "Path to service account credentials JSON",
        "help": (
            "Provide the path to a Google Cloud service account key file. Terraform uses this file to authenticate. "
            "See https://cloud.google.com/docs/authentication/getting-started for instructions on obtaining a key."
        ),
    },
    "project_id": {
        "prompt": "Google Cloud project ID",
        "help": (
            "The unique ID of your project as shown in the Google Cloud console. "
            "It will be used for all resources created by Terraform."
        ),
    },
    "region": {
        "prompt": "Deployment region",
        "help": (
            "Specify the GCP region for resources, e.g. us-central1. "
            "See https://cloud.google.com/about/locations for available regions."
        ),
    },
    "backend_bucket": {
        "prompt": "GCS bucket for Terraform state",
        "help": (
            "Name of an existing Google Cloud Storage bucket where Terraform state will be stored. "
            "Terraform must have permission to read and write in this bucket."
        ),
    },
    "user_email": {
        "prompt": "User email for budget alerts",
        "help": (
            "Individual email address that will receive billing budget notifications."
        ),
    },
    "group_email": {
        "prompt": "Group email for budget alerts",
        "help": (
            "Group email address to receive billing budget notifications."
        ),
    },
    "billing_account_id": {
        "prompt": "Billing account ID",
        "help": (
            "Identifier of the billing account in the form XXXXXX-XXXXXX-XXXXXX. "
            "Find it in the Google Cloud console under Billing."
        ),
    },
    "budget_amount_currency_code": {
        "prompt": "Budget currency code [USD]",
        "help": "Currency to use for the billing budget amount.",
        "default": "USD",
    },
    "budget_amount_units": {
        "prompt": "Budget amount [100]",
        "help": "Numeric amount for the budget limit.",
        "default": "100",
    },
    "budget_threshold_percent": {
        "prompt": "Alert threshold percent [50]",
        "help": "Percentage of the budget that triggers an alert.",
        "default": "50",
    },
}


def ask(key, info):
    prompt = info["prompt"]
    default = info.get("default")
    while True:
        ans = input(f"{prompt}: ").strip()
        if ans.lower() in {"?", "help", "h"}:
            print(info["help"])
            continue
        if not ans and default is not None:
            return default
        if ans:
            return ans
        print("Please provide a value or type '?' for help.")


def main():
    print("Terraform configuration helper. Type '?' for help on any field.\n")
    answers = {}
    for key, info in QUESTIONS.items():
        answers[key] = ask(key, info)

    with open("terraform.auto.tfvars.json", "w") as f:
        json.dump(answers, f, indent=2)
    print("\nVariables written to terraform.auto.tfvars.json")

    gen = input("Generate GitHub Actions workflow? [y/N]: ").strip().lower()
    if gen == "y" or gen == "yes":
        write_workflow()
        print("Workflow saved to .github/workflows/terraform.yml")


def write_workflow():
    workflow = """
name: Terraform
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: hashicorp/setup-terraform@v2
      - run: terraform init
      - run: terraform fmt -check
      - run: terraform validate
      - run: terraform plan -input=false
"""
    os.makedirs(".github/workflows", exist_ok=True)
    with open(".github/workflows/terraform.yml", "w") as f:
        f.write(workflow)


if __name__ == "__main__":
    main()
