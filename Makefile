build: build-base

test: build test-base test-xdebug test-xhprof

build-base:
	docker build -t droptica/jmeter base --no-cache
test-base:
	@echo "test pase PHP 7.0"
	@./tests.py 'droptica/jmeter' '-v' 'Copyright (c) 1999-2016 The Apache Software Foundation'
