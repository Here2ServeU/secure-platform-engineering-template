variable "project" {
  type        = string
  description = "GCP project ID"
}

variable "region" {
  type        = string
  description = "GCP region"
}

variable "cluster_name" {
  type        = string
  description = "GKE cluster name"
}

variable "node_count" {
  type        = number
  description = "Initial node count"
  default     = 2
}

variable "machine_type" {
  type        = string
  description = "GCE machine type for nodes"
  default     = "e2-medium"
}