provider "google" {
  credentials = file("${path.module}/credentials/credentials.json")
  project     = var.gcp_project
}
