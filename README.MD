# GalaxyBook Firmware Driver CLI

`galaxybook` is a simple command-line utility for managing the features present in the samsung-galaxybook firmware, that is mainline since linux kernel 6.15 and up.

## Usage

the base command `galaxybook` will give an overview of the current features implenented into the CLI. After galaxybook you can run the following commands:

### recording
Manages the 'Block Recording' firmware attribute present in the firmware.

`recording` gives the recording help overview showing the following

  -  `recording show` gives the current status of the 'Block Recording'

  -  `recording on` enables 'Block Recording', thus disabling the webcam

  -  `recording off` disables 'Block Recording', thus enabling the webcam

  -  `recording toggle` toggles 'Block Recording'


### batterylimit
Manages the 'Battery charge control end threshold' feature from the firmware

`batterylimit` show the current battery limit and set an new one if wanted.

   - `batterylimit show` Shows the current Battery Charge Limit

   - `batterylimit set` Set Battery Charge Limit (80-100)

### powerlid
Manages the 'Power on lid open' firmware attribute present in the firmware.

`powerlid` gives the recording help overview showing the following

  -  `powerlid show` gives the current status of 'power on lid open'

  -  `powerlid on` enables 'power on lid open'

  -  `powerlid off` disables 'power on lid open'

  -  `powerlid toggle` toggles 'Power on lid open'


## Installation

1. Download the repository

   ```bash
   git clone https://github.com/Ryan-Diazz/GalaxyBook-Firmware-Driver-CLI.git

   cd GalaxyBook-Firmware-Driver-CLI
   ```

2. install pipx (if not installed)

   On Debian/Ubuntu:
   ```bash
   sudo apt install pipx
   pipx ensurepath
   ```

   verify:

   ```bash
   pipx --version
   ```

3. Install the cli locally

   make sure you are in the same folder as where the pyproject.toml is located

   ```bash
   pipx install .
   ```

4. Verify installation
   run:

   ```bash
   galaxybook
   ```

   which will show you the possible functions of the CLI

5. Sudo

   when running `galaxybook` with `sudo` you may get 
   ```
   command not found
   ```
   this is because `sudo` resets your path

   #### Option 1: Use `sudo -E galaxybook`
      With the option `-E` sudo preserves user PATH, which lets you run the modifying commands of `galaxybook`

   #### Option 2: Add pipx local bin path to sudo secure_path
      Open sudo configuration:

      ```bash
      sudo visudo
      ``` 

      Find the line starting with:
      ```
      Defaults secure_path=...
      ```

      At the end add:
      ```
      :/home/YOUR_USERNAME/.local/bin
      ```
      <br>

      example: **Do Not Use this, Keep your OWN base String**
      ```
      Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/YOUR_USERNAME/.local/bin"
      ```


# License
This project is licensed under the terms of the MIT license. check the `LICENCE` File for more information


# Contribution
Running linux on an Samsung Galaxy Book (NP750XGJ) has proven quite a challange. Thanks to the awesome work of Joshua Grisham, the Driver situation has massively improved. However the control software has always felt a bit lacking. That’s why I started building this CLI, to make managing the machine a bit more user friendly.

I plan to add more features over time, but since this project is open source on GitHub, feel free to contribute! If something is missing, broken, or could be improved, don’t hesitate to open a pull request.

Have a wonderful day,

Ryan