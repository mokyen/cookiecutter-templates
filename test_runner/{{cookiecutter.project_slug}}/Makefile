.PHONY: smoke stress install regression

# Install all the needed pip dependencies into the virtualenv
install:
	python -m pip install -r requirements.txt

# Run both smoke and regression tests
tests: smoke regression

regression:
	py.test \
	--junitxml="regression.xml" \
	--instafail \
	--timeout=300 \
	-vv tests -m regression

smoke:
	py.test \
	--junitxml="smoke.xml" \
	--instafail \
	--timeout=300 \
	-vv tests -m smoketest

# Contiunously run the full test suite for either an amount of time or cycles.
stress:
	py.test \
	--junitxml="stress.xml" \
	--instafail \
	--timeout=300 \
	# --hours 1 --minutes 8 --seconds 9 \
	# --count=100 \
	-vv tests
