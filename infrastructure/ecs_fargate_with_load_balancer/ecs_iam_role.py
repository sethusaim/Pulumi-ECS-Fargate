import json
import pulumi_aws as aws
from ecs_fargate_with_load_balancer.ecs_variables import ECS_TASK_IAM_ROLE_NAME,ECS_TASK_IAM_ROLE_POLICY_NAME


def get_ecs_iam_role():
    try:
        role = aws.iam.Role(
            ECS_TASK_IAM_ROLE_NAME,
            assume_role_policy=json.dumps(
                {
                    "Version": "2008-10-17",
                    "Statement": [
                        {
                            "Sid": "",
                            "Effect": "Allow",
                            "Principal": {"Service": "ecs-tasks.amazonaws.com"},
                            "Action": "sts:AssumeRole",
                        }
                    ],
                }
            ),
        )

        return role

    except Exception as e:
        raise e


def get_ecs_iam_role_policy_attachment():
    try:
        iam_role = get_ecs_iam_role()

        rpa = aws.iam.RolePolicyAttachment(
            ECS_TASK_IAM_ROLE_POLICY_NAME,
            role=iam_role.name,
            policy_arn="arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy",
        )

        return rpa

    except Exception as e:
        raise e
