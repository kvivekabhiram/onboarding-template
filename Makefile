PROJECT = onboarding

init:
	pip install -r requirements.txt;

install:
	virtualenv -p python3 venv3; \
	. venv3/bin/activate; \
	pip install -r requirements.txt; \
	pip install .  ; \

develop:
	pip3 install virtualenv
	virtualenv -p python3 venv3; \
	. venv3/bin/activate; \
	pip install -r requirements.txt; \
	pip install -e .; \

clean:
	rm -rf venv; rm -rf $(PROJECT)/packages; rm -rf tmp; rm -rf __pycache__; \
	rm -rf tests/__pycache__; rm -f $(PROJECT)/*,cover rm -f $(PROJECT)/*.pyc; \
	rm -rf *.egg-info; rm -rf build; rm -rf dist

test:
	python test_basic_funfacts.py

zip: $(PROJECT).zip

$(PROJECT).zip: clean install
	pushd venv3/lib/python3.7/site-packages/ ; zip -x '*.pyc' -r9 ../../../../$@ *