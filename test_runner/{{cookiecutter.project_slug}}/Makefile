.PHONY: smoke stress install

install:
	python -m pip install -r requirements.txt

smoke:
	py.test \
	--instafail \
	--timeout=300 \
	-vv tests

stress:
	py.test \
	--instafail \
	--timeout=300 \
	# --hours 1 --minutes 8 --seconds 9 \
	# --count=100 \
	-vv tests
