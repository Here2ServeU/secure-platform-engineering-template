terraform {
  source = "../../../terraform/gcp/modules/backstage"
}

inputs = {
  cluster_name = "backstage-gcp-cluster"
  namespace    = "backstage"
}
