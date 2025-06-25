terraform {
  source = "../../../terraform/azure/modules/backstage"
}

inputs = {
  cluster_name = "backstage-azure-cluster"
  namespace    = "backstage"
}
