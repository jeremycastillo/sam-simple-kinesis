SERVICE=SimpleKinesis

build:
	sam build -m requirements.txt --use-container

run:
	sam local invoke "$(SERVICE)" -e ./events/event.json

test: build
	tox

zip:
	./zip.bash $(SERVICE)

clean:
	rm -rf .aws-sam