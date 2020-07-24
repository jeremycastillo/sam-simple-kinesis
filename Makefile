SERVICE=SimpleKinesis

test:
	tox

build: test
	sam build -m requirements.txt --use-container

run: build
	sam local invoke "$(SERVICE)" -e ./events/event.json

zip:
	./zip.bash $(SERVICE)

clean:
	rm -rf .aws-sam