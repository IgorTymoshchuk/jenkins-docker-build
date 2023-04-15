import boto3
import json
import os


def find_value_for_key(tags_list, key_name):
    for tag in tags_list:
        if tag["Key"] == key_name:
            return tag["Value"]
    return None


if __name__ == '__main__':

    aws_access_key_id = os.environ.get('aws_access_key_id')
    aws_secret_access_key = os.environ.get('aws_secret_access_key')
    aws_region = os.environ.get('aws_region')
    ec2_instance_state_code = os.environ.get('ec2_instance_state_code')

    ec2 = boto3.resource('ec2',
                               aws_access_key_id=aws_access_key_id,
                               aws_secret_access_key=aws_secret_access_key,
                               region_name=aws_region)

    filters = [
        {
            'Name': 'instance-state-code',
            'Values': [ec2_instance_state_code]
        }, {
            'Name': 'tag:k8s.io/role/master',
            'Values': ['1']
        }
    ]

    instances = ec2.instances.filter(Filters=filters)

    instance_matches = []
    for instance in instances:
        instance_name = find_value_for_key(instance.tags, "Name")
        record = {"id": instance.id, "name": instance_name}
        instance_matches.append(record)

    instance_matches_json = json.dumps(instance_matches)
    print(instance_matches_json)
