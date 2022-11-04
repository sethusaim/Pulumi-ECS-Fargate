import pulumi_aws as aws
from ecs_fargate_with_load_balancer.ecs_variables import *

from pulumi import ResourceOptions


def get_ecs_fargate_service(
    cluster, task_definition, security_group, vpc_subnets, target_group, wlb
):
    try:
        service = aws.ecs.Service(
            ECS_SERVICE_NAME,
            cluster=cluster.arn,
            desired_count=ECS_SERVICE_DESIRED_COUNT,
            launch_type=ECS_SERVICE_LAUNCH_TYPE,
            task_definition=task_definition.arn,
            network_configuration=aws.ecs.ServiceNetworkConfigurationArgs(
                assign_public_ip=ECS_SERVICE_NETWORK_PUBLIC_IP,
                subnets=vpc_subnets.ids,
                security_groups=[security_group.id],
            ),
            load_balancers=[
                aws.ecs.ServiceLoadBalancerArgs(
                    target_group_arn=target_group.arn,
                    container_name=ECS_CONTAINER_NAME,
                    container_port=ECS_CONTAINER_PORT,
                )
            ],
            opts=ResourceOptions(depends_on=[wlb]),
        )

        return service

    except Exception as e:
        raise e
