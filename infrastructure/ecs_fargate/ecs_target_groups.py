import pulumi_aws as aws
from ecs_fargate.ecs_variables import *

def get_load_balancer_target_group(vpc):
    try:
        atg = aws.lb.TargetGroup(
            ECS_LB_TARGET_GROUP_NAME,
            port=ECS_HOST_PORT,
            protocol=ECS_LB_PROTOCOL,
            target_type=ECS_TARGET_TYPE,
            vpc_id=vpc.id,
        )
        
        return atg
    
    except Exception as e:
        raise e 

