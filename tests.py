#!/usr/bin/python

import sys
import subprocess

if len(sys.argv) == 3:
    docker_image = sys.argv[1]
    test = sys.argv[2]
    expected = sys.argv[3]
else:
    sys.exit("3 arguments expected. 1. docker image 2. test type (php/apache2/xdebug/xhprof) 3. expected output value")



bashCommand = "docker run {} -v".format(docker_image)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
if error:
    sys.exit('Docker process did not execute correctly. Error: {}'.format(error))
else:
    echo 'ok'