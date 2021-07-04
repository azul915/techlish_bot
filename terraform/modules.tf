# Modules

# ------------------------------------------------
# Google Cloud Scheduler
module "cloud_scheduler" {
  source = "./modules/cloud_scheduler"

  gcp_project                  = var.gcp_project
  region                       = var.region
  cloud_scheduler_job_name     = var.cloud_scheduler_job_name
  cloud_scheduler_job_schedule = var.cloud_scheduler_job_schedule
  //  cloud_scheduler_pubsub_topic_id = module.cloud_functions_techlish.google_pubsub_topic_id
  cloud_functions_pubsub_topic_id = "projects/techlish/topics/${var.cloud_pubsub_topic_name}"
}

# ------------------------------------------------
# Google Cloud Functions
data "archive_file" "zip" {
  type        = "zip"
  source_dir  = "../app"
  output_path = "../.out/functions.zip"
}

data "google_service_account" "cloud_functions" {
  account_id = "techlish"
}

module "cloud_functions_techlish" {
  source = "./modules/cloud_functions"

  gcp_project             = var.gcp_project
  region                  = var.region
  cloud_pubsub_topic_name = var.cloud_pubsub_topic_name

  cloud_functions_function_name         = var.cloud_functions_function_name
  cloud_functions_runtime               = var.cloud_functions_runtime
  cloud_functions_entry_point           = var.cloud_functions_entry_point
  cloud_functions_available_memory_mb   = var.cloud_functions_available_memory_mb
  cloud_functions_timeout               = var.cloud_functions_timeout
  cloud_functions_service_account_email = data.google_service_account.cloud_functions.email
  cloud_functions_environment_variables = var.cloud_functions_environment_variables

}
