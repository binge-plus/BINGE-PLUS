module "artifact_registry" {
  source      = "git::https://github.com/GoogleCloudPlatform/cloud-foundation-fabric.git//modules/artifact-registry?ref=v29.0.0"
  project_id  = "binge-plus-deployment"
  location    = "us-central1"
  name        = "my-repo"
  description = "My Docker repository"
  format      = "DOCKER"
  labels = {
    environment = "binge-plus-deployment"
    team        = "devops"
  }
  cleanup_policies = {
    # "delete-old-versions" = {
    #   action = "DELETE"
    #   condition = {
    #     older_than = "120d"
    #   }
    # }
  }
}