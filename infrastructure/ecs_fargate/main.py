from ecs_fargate.ecs_cluster import create_ecs_cluster
from ecs_fargate.ecs_fargate_vpc import get_default_subnet_ids, get_default_vpc
from ecs_fargate.ecs_sg import get_ecs_security_group
from ecs_fargate.ecs_alb import get_ecs_load_balancer
from ecs_fargate.ecs_target_groups import get_load_balancer_target_group
from ecs_fargate.ecs_alb_listener import get_load_balancer_listener
from ecs_fargate.ecs_iam_role import get_ecs_iam_role
from ecs_fargate.ecs_task_definition import get_ecs_task_definition
from ecs_fargate.ecs_fargate_service import get_ecs_fargate_service

def get_ecs_fargate_endpoint():
    try:
        cluster = create_ecs_cluster()

        default_vpc = get_default_vpc()

        default_vpc_subnets = get_default_subnet_ids()

        security_group = get_ecs_security_group(vpc=default_vpc)
        
        alb = get_ecs_load_balancer(sg_group=security_group,vpc_subnets=default_vpc_subnets)
        
        atg = get_load_balancer_target_group(vpc=default_vpc)
        
        wl = get_load_balancer_listener(target_group=atg,load_balancer=alb)
        
        iam_role = get_ecs_iam_role()
        
        task_definition = get_ecs_task_definition(iam_role=iam_role)
        
        service = get_ecs_fargate_service(cluster=cluster,task_definition=task_definition,security_group=security_group,vpc_subnets=default_vpc_subnets,target_group=atg,wlb=wl)
                
        return alb.dns_name

    except Exception as e:
        raise e




