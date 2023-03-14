terraform {
  backend "gcs" {
    bucket = "gpt-terraform-backend"
    prefix = "terraform/state"
  }
}
