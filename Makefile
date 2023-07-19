docker-image:
	pipenv run pip freeze > requirements.txt && docker build -t mailing-service:test . && rm requirements.txt

docker-clean:
	docker stop mailing  && docker rm mailing

docker-run:
	docker run -d -p 9000:8080 --name mailing mailing-service:test

docker-all:
	make docker-image && make docker-clean && make docker-run

invoke: 
	aws lambda invoke --function-name mailing-service --payload file://request-sapmle.json output.json --log-type Tail --query 'LogResult' --output text --cli-binary-format raw-in-base64-out | base64 --decode

deploy: 
	docker tag mailing-service:test 681839224497.dkr.ecr.us-east-1.amazonaws.com/tenderi-services:latest && docker push 681839224497.dkr.ecr.us-east-1.amazonaws.com/tenderi-services:latest  
