# ------------------------------------------------
# Google Cloud Scheduler

resource "google_cloud_scheduler_job" "scheduler_job" {
  name      = var.cloud_scheduler_job_name
  project   = var.gcp_project
  schedule  = var.cloud_scheduler_job_schedule
  time_zone = "Asia/Tokyo"
  region    = var.region

  pubsub_target {
    topic_name = var.cloud_functions_pubsub_topic_id
    data       = base64encode("{}")
  }

}
