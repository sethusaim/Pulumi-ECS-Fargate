import pulumi_aws as aws
from ecs_fargate.ecs_variables import ECS_CLUSTER_NAME


def create_ecs_cluster():
    try:
        cluster = aws.ecs.Cluster(ECS_CLUSTER_NAME)

        return cluster

    except Exception as e:
        raise e
