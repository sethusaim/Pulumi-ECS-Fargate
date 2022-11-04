import pulumi_aws as aws


def get_default_vpc():
    try:
        default_vpc = aws.ec2.get_vpc(default=True)

        return default_vpc

    except Exception as e:
        raise e


def get_default_subnet_ids():
    try:
        default_vpc = get_default_vpc()

        default_vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=default_vpc.id)

        return default_vpc_subnets

    except Exception as e:
        raise e
