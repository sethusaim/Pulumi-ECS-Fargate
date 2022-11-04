import pulumi_aws as aws
from ecs_fargate.ecs_variables import *

def get_load_balancer_listener(target_group,load_balancer):
    try:
        wl = aws.lb.Listener(
            ECS_LB_LISTENER_NAME,
            load_balancer_arn=load_balancer.arn,
            port=ECS_HOST_PORT,
            default_actions=[
                aws.lb.ListenerDefaultActionArgs(
                    type=ECS_LB_LISTENER_DEFAULT_ACTION_TYPE, target_group_arn=target_group.arn
                )
            ],
        )
        
        return wl
    
    except Exception as e:
        raise e 


