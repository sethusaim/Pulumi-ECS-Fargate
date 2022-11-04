import pulumi_aws as aws
from ecs_fargate_with_load_balancer.ecs_variables import *

def get_ecs_security_group(vpc):
    try:
        group = aws.ec2.SecurityGroup(
            ECS_SECURITY_GROUP_NAME,
            vpc_id=vpc.id,
            ingress=[
                aws.ec2.SecurityGroupIngressArgs(
                    protocol=ECS_INGRESS_1_PROTOCOL,
                    from_port=ECS_INGRESS_1_FROM_PORT,
                    to_port=ECS_INGRESS_1_TO_PORT,
                    cidr_blocks=ECS_INGRESS_1_CIDR_BLOCKS,
                )
            ],
            egress=[
                aws.ec2.SecurityGroupEgressArgs(
                    protocol=ECS_EGRESS_PROTOCOL,
                    from_port=ECS_EGRESS_FROM_PORT,
                    to_port=ECS_EGRESS_TO_PORT,
                    cidr_blocks=ECS_EGRESS_CIDR_BLOCKS,
                )
            ],
        )

        return group

    except Exception as e:
        raise e
