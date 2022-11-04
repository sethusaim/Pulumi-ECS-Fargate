import pulumi_aws as aws
import json
from ecs_fargate.ecs_variables import *


def get_ecs_task_definition(iam_role):
    try:
        task_definition = aws.ecs.TaskDefinition(
            ECS_TASK_DEF_NAME,
            family=ECS_TASK_DEF_FAMILY,
            cpu=ECS_CPU,
            memory=ECS_MEMORY,
            network_mode=ECS_NETWORK_MODE,
            requires_compatibilities=ECS_MODE,
            execution_role_arn=iam_role.arn,
            container_definitions=json.dumps(
                [
                    {
                        "name": ECS_CONTAINER_NAME,
                        "image": ECS_CONTAINER_NAME,
                        "portMappings": [
                            {
                                "containerPort": ECS_CONTAINER_PORT,
                                "hostPort": ECS_HOST_PORT,
                                "protocol": ECS_CONTAINER_PROTOCOL,
                            }
                        ],
                    }
                ]
            ),
        )

        return task_definition

    except Exception as e:
        raise e
