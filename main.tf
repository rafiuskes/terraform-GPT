provider "google" {
  credentials = file(var.credentials_file)
  project     = var.project_id
  region      = "us-central1"
}

resource "google_billing_budget" "budget" {
  display_name = "My budget"
  billing_account = var.billing_account_id

  budget_filter {
    projects = [var.project_id]
  }

  amount {
    specified_amount {
      currency_code = "USD"
      units         = 100
    }
    threshold_rules {
      threshold_percent = 0.5
      spend_basis = "CURRENT_SPEND"
    }
  }

  notifications {
    pubsub_topic = "projects/${var.project_id}/topics/billing-budget-alerts"

    email_notifications {
      enabled = true
      destinations = ["user:example@example.com"]
    }
  }
}


