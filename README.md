# aws-vpc-ec2
## Rudimentary AWS Cloud Formation scripts
* grox-vpc-101.yaml builds a VPC with three subnets: dmz, dev, and prv
* grox-ec2-dev-101.yaml builds a dev linux box in the dev subnet, based on a private AWS ami 
* grox-ec2-dmz-101.yaml builds an nginx, express, node.js web server in the dmz subnet, based on a private AWS ami
* grox-ec2-prv-101.yaml build a linux box for hosting a postgres DB in the private subnet

We use a color term -- in this case "teal" -- to give our components a catchy name for use in filtering, billing, etc.
