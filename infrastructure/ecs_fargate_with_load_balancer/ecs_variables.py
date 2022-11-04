## ECS Fargate related configuration

ECS_CLUSTER_NAME = "test-fargate-cluster"

ECS_SECURITY_GROUP_NAME = "test-fargate-security-group"

### Security Group ingress Rule 1 related configuration

ECS_INGRESS_1_PROTOCOL = "tcp"

ECS_INGRESS_1_FROM_PORT = 80

ECS_INGRESS_1_TO_PORT = 80

ECS_INGRESS_1_CIDR_BLOCKS = ["0.0.0.0/0"]

### Security Group Egress Rule related configuration

ECS_EGRESS_PROTOCOL = "-1"

ECS_EGRESS_FROM_PORT = 0

ECS_EGRESS_TO_PORT = 0

ECS_EGRESS_CIDR_BLOCKS = ["0.0.0.0/0"]

## ECS Load Balancer related configuration

ECS_ALB_NAME = "test-fargate-lb"

## ECS Load Balancer Target Group related configuration

ECS_LB_TARGET_GROUP_NAME = "test-fargate-tg"

ECS_LB_PROTOCOL = "HTTP"

ECS_TARGET_TYPE = "ip"

## ECS Load Balancer related configuration

ECS_LB_LISTENER_NAME = "web"

ECS_LB_LISTENER_DEFAULT_ACTION_TYPE = "forward"

## ECS Task Execution IAM Role related configuration

ECS_TASK_IAM_ROLE_NAME = "task-exec-role"

## ECS Task Execution IAM Role Policy related configuration

ECS_TASK_IAM_ROLE_POLICY_NAME = "task-exec-policy"

## ECS Task Definition related configuration

ECS_TASK_DEF_NAME = "app-task"

ECS_TASK_DEF_FAMILY = "fargate-task-definition"

ECS_CPU = 256

ECS_MEMORY = 512

ECS_NETWORK_MODE = "awsvpc"

ECS_MODE = ["FARGATE"]

ECS_CONTAINER_NAME = "test-fargate-app"

ECS_CONTAINER_NAME = "nginx"

ECS_CONTAINER_PORT = 80

ECS_HOST_PORT = 80

ECS_CONTAINER_PROTOCOL = "tcp"

## ECS Service related configuration

ECS_SERVICE_NAME = "test-fargate-svc"

ECS_SERVICE_DESIRED_COUNT = 3

ECS_SERVICE_LAUNCH_TYPE = "FARGATE"

ECS_SERVICE_NETWORK_PUBLIC_IP = True
