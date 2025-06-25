terraform {
  source = "../../../terraform/aws"
}

inputs = {
  cluster_name = "backstage-aws-cluster"
  namespace    = "backstage"
}
