# Jmeter in docker

## Tags
- `latest`

## Installation / Usage

1. Install the `droptica/jmeter` container:

    ``` sh
    $ docker pull droptica/jmeter
    ```

  Alternatively, pull a specific version of `droptica/jmeter`:
    ``` sh
    $ docker pull droptica/jmeter:latest
    ```
    
2. Create test file eg.: my_test.jmx    

3. Run the containter
    ```sh
    $ docker run -v /my-folder/with-test:/app droptica/jmeter -n -t my_test.jmx -l log.jtl -H my.proxy.server -P 8000
    ```
    