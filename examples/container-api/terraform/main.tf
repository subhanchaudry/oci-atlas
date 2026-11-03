resource "oci_container_instances_container_instance" "api" {
  availability_domain                  = var.availability_domain
  compartment_id                       = var.compartment_id
  display_name                         = var.name
  shape                                = var.shape
  container_restart_policy             = "ALWAYS"
  graceful_shutdown_timeout_in_seconds = 60
  shape_config {
    ocpus         = 1
    memory_in_gbs = 4
  }
  vnics {
    subnet_id             = var.subnet_id
    nsg_ids               = var.nsg_ids
    is_public_ip_assigned = false
  }
  containers {
    display_name                   = "api"
    image_url                      = var.image_url
    is_resource_principal_disabled = false
    environment_variables = {
      ATLAS_DB_SECRET_ID = var.db_secret_id
      ATLAS_DB_DSN       = var.db_dsn
    }
    health_checks {
      health_check_type        = "HTTP"
      path                     = "/health"
      port                     = 8080
      initial_delay_in_seconds = 15
      interval_in_seconds      = 30
      timeout_in_seconds       = 3
      failure_threshold        = 3
      success_threshold        = 1
      failure_action           = "KILL"
    }
  }
  dynamic "image_pull_secrets" {
    for_each = var.image_pull_secret == null ? [] : [var.image_pull_secret]
    content {
      registry_endpoint = image_pull_secrets.value.registry_endpoint
      secret_type       = "VAULT"
      secret_id         = image_pull_secrets.value.secret_id
    }
  }
  freeform_tags = { "project" = "oci-atlas", "example" = "container-api" }
}

# Exact resource membership limits runtime secret access to this container instance.
# Health does not require a database connection, allowing IAM to propagate after creation.
resource "oci_identity_dynamic_group" "api" {
  provider       = oci.home
  compartment_id = var.tenancy_id
  name           = "${var.name}-runtime"
  description    = "Runtime identity for the Atlas private API"
  matching_rule  = "ALL {resource.type = 'computecontainerinstance', resource.id = '${oci_container_instances_container_instance.api.id}'}"
}
resource "oci_identity_policy" "secret" {
  provider       = oci.home
  compartment_id = var.secret_compartment_id
  name           = "${var.name}-secret"
  description    = "Read only the existing application credential secret"
  statements = [
    "Allow dynamic-group id ${oci_identity_dynamic_group.api.id} to read secret-bundles in compartment id ${var.secret_compartment_id} where target.secret.id = '${var.db_secret_id}'"
  ]
}
output "container_instance_id" { value = oci_container_instances_container_instance.api.id }
output "vnic_id" { value = oci_container_instances_container_instance.api.vnics[0].vnic_id }
