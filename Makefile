SHELL := /bin/bash
ENV := soccer_env

create_env:
	conda create -y -n ${ENV} python=2.7

dev_install:
	make create_env
	source activate ${ENV} && \
	pip install -r requirements.txt && \
	pip install -e .

install:
	make create_env
	source activate ${ENV} && \
	pip install -r requirements.txt && \
	python setup.py install

download:
	PYTHONPATH=. python soccer_predictions/collect_data.py

clean:
	source deactivate && \
	conda env remove -y -n ${ENV}
