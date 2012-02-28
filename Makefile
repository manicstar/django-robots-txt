test:
	make -C django-robots-txt-test-project test

install:
	python setup.py install

build:
	python setup.py build

sdist:
	python setup.py sdist

upload:
	python setup.py sdist upload

clean:
	rm -rf dist build *.egg-info django-robots-txt-*
