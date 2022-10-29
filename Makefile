.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec prajwal-aws-2 --no-session -- sam deploy

deploy-site:
	aws-vault exec prajwal-aws-2 --no-session -- aws s3 sync ./resume-site s3://cloud-resume-prajwal

invoke-get:
	sam build && aws-vault exec prajwal-aws-2 --no-session -- sam local invoke GetFunction

invoke-put:
	sam build && aws-vault exec prajwal-aws-2 --no-session -- sam local invoke PutFunction