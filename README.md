# AWS exercise

This exercise stands up a classic load balancer, ec2 instance with respective security groups.  The ec2 instance is provisioned with a hello world style flask app a top apache.  Included are a setup script for your workspace setup and ansible playbook / role which provisions the aws infrastructure and ec2 node.  A teardown playbook is also included for cleanup.

# Setup

This was tested on:

* CentOS Linux release 7.4.1708 (Core)
* Pre-existing AWS Default VPC

Assumptions and test setup:

* AWS credentials in ~/.aws/credentials

Set up a virtualenv and install packages from the requirements.txt with the following command:

```
source set_env
```

Fill in the values of vars/main.yml.  Here is a non-working example of what it should look like:

```
region: "us-west-2"
vpc_id: "vpc-00000000"
vpc_subnet_id: "subnet-0000000"
instance_type: "t2.nano"
pem_key: "keypairname"
ami: ami-f2d3638a
role: webapp
```

# Demo

Standing up the demo:

```
ansible-playbook playbook.yml -e 'env=demo'
```

The instance ip address and AWS given dns name for the elb are provided as debug output at the end of the run.  You can verify the flask application work via:

```
curl demo-elb-XXXXXXXXXX.us-west-2.elb.amazonaws.com/hello/steven
```

Tearing it down:

```
ansible-playbook teardown.yml -e 'env=demo'
```
