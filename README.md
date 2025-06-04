# Terraform GCP Example

This repository contains Terraform configuration for a small Google Cloud setup. It demonstrates a remote backend using Google Cloud Storage and a sample billing budget configuration.

## Files

- `backend.tf` – configures a GCS backend for storing Terraform state.
- `versions.tf` – sets the required Terraform and provider versions.
- `variables.tf` – declares input variables such as project ID, region and billing configuration.
- `main.tf` – configures the Google provider and creates a `google_billing_budget` resource.
- `Código com versionamento e backend remoto` – an extended example with additional resources (VPC, instances and billing notifications).
- `scripts/agent.py` – interactive helper that collects values for required variables and can create a GitHub Actions pipeline.

## Usage

1. Ensure you have Terraform installed (`>= 1.3`).
2. Initialize the working directory:
   ```sh
   terraform init
   ```
3. Review the execution plan:
   ```sh
   terraform plan
   ```
4. Apply the changes:
   ```sh
   terraform apply
   ```

### Interactive setup

Run `scripts/agent.py` to be guided through entering the required variables. The
script can also generate a basic GitHub Actions workflow for running Terraform
commands automatically.

### Fetching GCP information

The workflow `.github/workflows/gcp-info.yml` can query your Google Cloud
environment for available projects and billing accounts. It uses the helper
script `scripts/fetch_gcp_info.sh` which relies on the Google Cloud SDK.

1. Add `GCP_PROJECT_ID` and `GCP_SA_KEY` secrets to your repository. The latter
   should contain the JSON key for a service account with permission to list
   projects and billing accounts.
2. Trigger the **Fetch GCP Info** workflow from the GitHub Actions tab.
3. After the job completes, download the `gcp-info` artifact to review the
   generated `gcp-info.json` file.

This structure follows the [Cloud Foundation Fabric](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric) style by separating version constraints, backend configuration and variable definitions.
