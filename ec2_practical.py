"""
ec2_practical.py

AWS Cloud Computing Practical — boto3 se EC2 instance launch,
list, aur stop/terminate karna.

Run karne se pehle:
    pip3 install boto3
    aws configure   (access key, secret key, region set karo)
"""

import boto3
import time

# EC2 client banao (region wahi rakho jo `aws configure` me diya tha)
ec2 = boto3.client("ec2", region_name="ap-south-1")


def launch_instance():
    """Ek naya free-tier EC2 instance launch karta hai."""
    response = ec2.run_instances(
        ImageId="ami-0f5ee92e2d63afc18",   # Ubuntu 22.04 LTS (ap-south-1) — apne region ka AMI ID daalna
        InstanceType="t2.micro",            # Free tier eligible
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [{"Key": "Name", "Value": "boto3-practical-instance"}],
            }
        ],
    )
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"[+] Instance launch ho gaya: {instance_id}")
    return instance_id


def wait_and_show_status(instance_id):
    """Instance running hone tak wait karta hai, phir public IP dikhata hai."""
    print("[*] Instance running hone ka wait kar rahe hain...")
    waiter = ec2.get_waiter("instance_running")
    waiter.wait(InstanceIds=[instance_id])

    desc = ec2.describe_instances(InstanceIds=[instance_id])
    instance = desc["Reservations"][0]["Instances"][0]
    print(f"[+] State: {instance['State']['Name']}")
    print(f"[+] Public IP: {instance.get('PublicIpAddress', 'N/A')}")


def list_all_instances():
    """Account ke saare EC2 instances list karta hai."""
    print("\n[*] Saare instances:")
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for inst in reservation["Instances"]:
            name = next(
                (t["Value"] for t in inst.get("Tags", []) if t["Key"] == "Name"),
                "(no name)",
            )
            print(f"  - {inst['InstanceId']} | {name} | {inst['State']['Name']}")


def stop_instance(instance_id):
    """Instance ko stop karta hai (charges rukwane ke liye)."""
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"[+] Instance stop ho raha hai: {instance_id}")


def terminate_instance(instance_id):
    """Instance ko permanently terminate (delete) karta hai."""
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"[+] Instance terminate ho raha hai: {instance_id}")


if __name__ == "__main__":
    # 1. Naya instance launch karo
    new_id = launch_instance()

    # 2. Running hone tak wait karo aur status dikhao
    wait_and_show_status(new_id)

    # 3. Saare instances list karo
    list_all_instances()

    # 4. Practical khatam hone par stop kar do (charges bachane ke liye)
    # stop_instance(new_id)

    # 5. Agar poora delete karna ho:
    # terminate_instance(new_id)
