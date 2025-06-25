provider "gcp" {
  region = var.region
}

resource "gcp_s3_bucket" "backstage_assets" {
  bucket = "${var.project_name}-backstage-assets"
  acl    = "private"
}
