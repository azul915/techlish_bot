variable "gcp_project" {
  type = string
}

variable "region" {
  type = string
}

variable "cloud_pubsub_topic_name" {
  type = string
}

variable "cloud_functions_function_name" {
  type = string
}

variable "cloud_functions_runtime" {
  type = string
}

variable "cloud_functions_entry_point" {
  type = string
}

variable "cloud_functions_available_memory_mb" {
  type    = number
  default = 128
}

variable "cloud_functions_timeout" {
  type    = number
  default = 60
}

variable "cloud_functions_service_account_email" {
  type = string
}

variable "cloud_functions_environment_variables" {
  type    = map(string)
  default = {}
}
