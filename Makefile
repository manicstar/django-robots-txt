test:
	python quicktest.py robots_txt

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
