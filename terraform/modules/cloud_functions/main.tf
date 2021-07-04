# ------------------------------------------------
# Google Cloud Pub/Sub

resource "google_pubsub_topic" "topic_twice_a_day" {
  name    = var.cloud_pubsub_topic_name
  project = var.gcp_project
}

# ------------------------------------------------
# Google Cloud Storage

resource "google_storage_bucket" "bucket" {
  name          = "bucket-${var.cloud_functions_function_name}"
  location      = var.region
  project       = var.gcp_project
  storage_class = "NEARLINE"
}

resource "google_storage_bucket_object" "object" {
  name   = "functions.zip"
  bucket = google_storage_bucket.bucket.name
  source = "../.out/functions.zip"
}

# ------------------------------------------------
# Google Cloud Functions

resource "google_cloudfunctions_function" "function" {
  name    = var.cloud_functions_function_name
  runtime = var.cloud_functions_runtime

  project               = var.gcp_project
  region                = var.region
  entry_point           = var.cloud_functions_entry_point
  available_memory_mb   = var.cloud_functions_available_memory_mb
  timeout               = var.cloud_functions_timeout
  service_account_email = var.cloud_functions_service_account_email
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.object.name
  environment_variables = var.cloud_functions_environment_variables

  event_trigger {
    event_type = "providers/cloud.pubsub/eventTypes/topic.publish"
    resource   = google_pubsub_topic.topic_twice_a_day.id
  }
}
