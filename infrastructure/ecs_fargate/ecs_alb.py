import pulumi_aws as aws
from ecs_fargate.ecs_variables import ECS_ALB_NAME


def get_ecs_load_balancer(sg_group, vpc_subnets):
    try:
        alb = aws.lb.LoadBalancer(
            ECS_ALB_NAME, security_groups=[sg_group.id], subnets=vpc_subnets.ids
        )

        return alb

    except Exception as e:
        raise e
