from pulumi import export
from ecs_fargate.main import get_ecs_fargate_endpoint

ecs_farget_endpoint = get_ecs_fargate_endpoint()

export("url", ecs_farget_endpoint)
