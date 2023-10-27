setup-venv:
	source .venv/bin/activate

run:
	python3.11.exe src/main.py

gen:
	python3 gen.py

update-deps:
	python -m pip freeze > requirements.txt

gen-proto:
	protoc --python_out=./src/generated --twirpy_out=./src/generated ./src/proto/hashmap.proto && \
	mv src/generated/src/proto/hashmap_pb2.py src/generated/hashmap_pb2.py && \
  mv src/generated/src/proto/hashmap_twirp.py src/generated/hashmap_twirp.py && \
	protoc --python_out=./src/generated --experimental_allow_proto3_optional --twirpy_out=./src/generated ./src/proto/auth.proto && \
	mv src/generated/src/proto/auth_pb2.py src/generated/auth_pb2.py && \
  mv src/generated/src/proto/auth_twirp.py src/generated/auth_twirp.py && \
	rm -rf src/generated/src
