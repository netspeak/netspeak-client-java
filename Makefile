SHELL := /bin/bash

protoc:
	mkdir -p src/main/python/generated
	protoc --python_out=src/main/python/generated NetspeakService.proto

python: protoc
	python3.10 -m venv src/main/python/venv
	cd src/main/python && source venv/bin/activate && python -m pip install -r requirements.txt
	cd src/main/python && source venv/bin/activate && python setup.py build

java:
	mvn clean compile
	mvn package assembly:single

clean:
	rm -rf src/main/python/generated/NetspeakService_pb2.py
	rm -rf src/main/python/venv
	rm -rf src/main/python/build
	mvn clean

build: clean protoc python java