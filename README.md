# Terraform GCP Example

This repository contains Terraform configuration for a small Google Cloud setup. It demonstrates a remote backend using Google Cloud Storage and a sample billing budget configuration.

## Files

- `backend.tf` – configures a GCS backend for storing Terraform state.
- `versions.tf` – sets the required Terraform and provider versions.
- `variables.tf` – declares input variables such as project ID, region and billing configuration.
- `main.tf` – configures the Google provider and creates a `google_billing_budget` resource.
- `Código com versionamento e backend remoto` – an extended example with additional resources (VPC, instances and billing notifications).

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

This structure follows the [Cloud Foundation Fabric](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric) style by separating version constraints, backend configuration and variable definitions.
