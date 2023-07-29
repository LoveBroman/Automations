# Automations

## Making the Script Globally Accessible on MacOS/Unix Systems

### Method 1: Copy the script to a directory in your PATH

1. Copy the script to `/usr/local/bin` using the `cp` command:

    ```bash
    cp /path/to/your/script.py /usr/local/bin
    ```

    Note: You may need to use `sudo` if you don't have permission to copy files to `/usr/local/bin`:

    ```bash
    sudo cp /path/to/your/script.py /usr/local/bin
    ```

    After these steps, you should be able to run your script from anywhere by typing `script.py` into the terminal.

    Remember, any updates to your original script will not be reflected in the copy located in `/usr/local/bin`.

### Method 2: Create a symbolic link

1. Create a symbolic link in `/usr/local/bin` to your script:

    ```bash
    ln -s /path/to/your/script.py /usr/local/bin/script.py
    ```

    Note: You may need to use `sudo` if you don't have permission to create links in `/usr/local/bin`:

    ```bash
    sudo ln -s /path/to/your/script.py /usr/local/bin/script.py
    ```

    This way, your script will always be up-to-date with your development version, and you can run it from anywhere by typing `script.py` into the terminal.
