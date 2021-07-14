aws cloudformation deploy --template-file .\grox-ec2-dev-101.yaml --stack-name teal-dev
aws cloudformation deploy --template-file .\grox-ec2-dmz-101.yaml --stack-name teal-dmz
aws cloudformation deploy --template-file .\grox-ec2-prv-101.yaml --stack-name teal-prv
