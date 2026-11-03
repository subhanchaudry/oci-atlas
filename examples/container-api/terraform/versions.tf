terraform {
  required_version = ">= 1.5.0, < 2.0.0"
  required_providers {
    oci = {
      source  = "oracle/oci"
      version = "7.22.0"
    }
  }
}
provider "oci" {
  region              = var.region
  config_file_profile = var.config_file_profile
  auth                = var.auth
}
provider "oci" {
  alias               = "home"
  region              = var.home_region
  config_file_profile = var.config_file_profile
  auth                = var.auth
}
