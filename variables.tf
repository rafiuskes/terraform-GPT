variable "project_id" {
  type    = string
  description = "The ID of the Google Cloud Platform project to use for this deployment."
}

variable "region" {
  type    = string
  description = "The region in which to deploy resources, e.g. 'us-central1'."
}

variable "backend_bucket" {
  type    = string
  description = "The name of the Google Cloud Storage bucket to use for the Terraform backend."
}

variable "user_email" {
  type    = string
  description = "The email address of the user to receive billing notifications."
}

variable "group_email" {
  type    = string
  description = "The email address of the group to receive billing notifications."
}

variable "billing_account_id" {
  type    = string
  description = "The ID of the billing account to associate with the project."
}

variable "budget_amount_currency_code" {
  type    = string
  description = "The currency code to use for the billing budget amount."
  default = "USD"
}

variable "budget_amount_units" {
  type    = number
  description = "The amount to use for the billing budget, in the specified currency."
  default = 100
}

variable "budget_threshold_percent" {
  type    = number
  description = "The threshold percentage for the billing budget, e.g. 50 for 50%."
  default = 50
}
