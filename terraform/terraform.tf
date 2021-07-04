terraform {
  required_version = "= 0.12.29"

  backend "gcs" {
    bucket      = "azul915-tf-state"
    prefix      = "terraform/techlish"
    credentials = "./credentials/credentials.json"
  }
}
