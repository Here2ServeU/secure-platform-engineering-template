provider "azure" {
  region = var.region
}

resource "azure_s3_bucket" "backstage_assets" {
  bucket = "${var.project_name}-backstage-assets"
  acl    = "private"
}
