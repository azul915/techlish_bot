# ------------------------------------------------
# Common

variable "region" {
  description = "Deploy region"
  type        = string
  default     = "us-central1"
}

variable "gcp_project" {
  description = "Google Cloud Planform project name"
  type        = string
  default = "techlish"
}

# ------------------------------------------------
# Google Cloud Scheduler

variable "cloud_scheduler_job_name" {
  description = "Google Cloud Scheduler job name"
  type        = string
  default = "job-twice-a-day"
}

variable "cloud_scheduler_job_schedule" {
  description = "Google Cloud Scheduler job schedule"
  type        = string
  default = "00 8,20 * * *"
}

# ------------------------------------------------
# Google Cloud Pub/Sub

variable "cloud_pubsub_topic_name" {
  description = "Google Cloud Pub/Sub topic name"
  type        = string
}

# ------------------------------------------------
# Google Cloud Functions

variable "cloud_functions_function_name" {
  description = "Google Cloud Functions function name"
  type        = string
  default = "tweet-and-write-speadsheet"
}

variable "cloud_functions_runtime" {
  description = "Google Cloud Functions runtime"
  type        = string
  default     = "python37"
}

variable "cloud_functions_entry_point" {
  description = "Google Cloud Functions entry point"
  type        = string
  default = "handle_cloud_functions"
}

variable "cloud_functions_available_memory_mb" {
  description = "Google Cloud Functions available memory MB"
  type        = number
  default = 128
}

variable "cloud_functions_timeout" {
  description = "Google Cloud Functions timeout"
  type        = number
  default = 60
}

variable "cloud_functions_environment_variables" {
  description = "Google Cloud Functions environment"
  type        = map(string)
  default     = {}
}
