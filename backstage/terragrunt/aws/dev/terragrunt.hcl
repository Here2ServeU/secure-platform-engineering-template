terraform {
  source = "../../../terraform/aws/modules/backstage"
}

inputs = {
  cluster_name = "backstage-aws-cluster"
  namespace    = "backstage"
}
