init:
	pip3 install -r requirements.txt

package:
	python3 setup.py sdist bdist_wheel

docker:
	docker build -t yikaus/ssmp .

local:
	pip3 install dist/ssmp-0.0.7.tar.gz

upload: package
	twine check dist/* && twine upload dist/*
