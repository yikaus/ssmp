init:
	pip3 install -r requirements.txt

test:
	nosetests tests

package:
	python3 setup.py sdist

local:
	pip3 install dist/ssmp-0.0.1.tar.gz
