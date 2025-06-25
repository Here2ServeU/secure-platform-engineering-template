provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "backstage_assets" {
  bucket = "${var.project_name}-backstage-assets"
  acl    = "private"
}
