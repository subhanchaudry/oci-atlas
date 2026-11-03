variable "region" { type = string }
variable "home_region" { type = string }
variable "tenancy_id" { type = string }
variable "compartment_id" { type = string }
variable "secret_compartment_id" { type = string }
variable "subnet_id" { type = string }
variable "availability_domain" { type = string }
variable "db_secret_id" { type = string }
variable "nsg_ids" {
  type = list(string)
  validation {
    condition     = length(var.nsg_ids) > 0
    error_message = "Supply existing NSGs for private client and database/API access."
  }
}
variable "db_dsn" {
  type = string
  validation {
    condition     = startswith(lower(var.db_dsn), "tcps://")
    error_message = "Supply the database's TCPS Easy Connect hostname, port and service."
  }
}
variable "image_url" {
  type = string
  validation {
    condition     = can(regex("@sha256:[a-f0-9]{64}$", var.image_url))
    error_message = "Pin the image by its SHA-256 digest."
  }
}
variable "shape" {
  type    = string
  default = "CI.Standard.E4.Flex"
}
variable "name" {
  type    = string
  default = "atlas-container-api"
  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{2,40}$", var.name))
    error_message = "Use 3–41 lowercase letters, digits or hyphens, starting with a letter."
  }
}
variable "config_file_profile" {
  type    = string
  default = "DEFAULT"
}
variable "auth" {
  type    = string
  default = "SecurityToken"
  validation {
    condition     = contains(["SecurityToken", "APIKey", "InstancePrincipal", "ResourcePrincipal"], var.auth)
    error_message = "Choose a supported Terraform OCI authentication mode."
  }
}
variable "image_pull_secret" {
  description = "Existing registry credential secret with pull authorization established before this stack."
  type        = object({ registry_endpoint = string, secret_id = string })
  default     = null
}
