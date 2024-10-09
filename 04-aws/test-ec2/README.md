- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply -auto-approve
- terraform destroy -auto-approve

in case you get some AWS Error, then use STS to decode it:
- aws sts decode-authorization-message --encoded-message <ENCODED MESSAGE>

#check if "AWSCompromisedKeyQuarantineV2" policy is applied to user in AWS. It can be deleted. But make sure to delete and re-create the compromised credentials.

ansible-playbook -i inventory.ini nginx-playbook.yaml


