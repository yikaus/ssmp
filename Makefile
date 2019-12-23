init:
	pip3 install -r requirements.txt

package:
	python3 setup.py sdist bdist_wheel

local:
	pip3 install dist/ssmp-0.0.1.tar.gz
