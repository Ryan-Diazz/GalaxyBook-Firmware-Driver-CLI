# GalaxyBook Firmware Driver CLI

`galaxybook` is a simple command-line utility for managing the features present in the samsung-galaxybook firmware, that is mainline since linux kernel 6.15 and up.

## Usage

the base command `galaxybook` will give an overview of the current features implenented into the CLI. 

It can be run without sudo for features that doesn't write to a file. Permission warnings will show for cammonds requiring sudo.

After `galaxybook` you can run the following commands:

### recording
Manages the 'Block Recording' firmware attribute present in the firmware.

`recording` gives the recording help overview showing the following

  -  `recording show` gives the current status of the 'Block Recording'

  -  `recording on` enables 'Block Recording', thus disabling the webcam

  -  `recording off` disables 'Block Recording', thus enabling the webcam

  -  `recording toggle` toggles 'Block Recording'


### battery
Manages the Battery features from the firmware

`battery` Manage battery features

   - `battery info` Show battery information

   - `battery status` Show battery status

   - `battery health` show battery health

   - `battery limit` Manage battery charge limit from 80% to 100%

   - `battery wattage` Monitor system wattage (current, minimum, maximum, avarage)


### powerlid
Manages the 'Power on lid open' firmware attribute present in the firmware.

`powerlid` gives the recording help overview showing the following

  -  `powerlid show` gives the current status of 'power on lid open'

  -  `powerlid on` enables 'power on lid open'

  -  `powerlid off` disables 'power on lid open'

  -  `powerlid toggle` toggles 'Power on lid open'


### Keyboard Backlight
Manage keyboard backlight with percentages (most keyboards only support modes 0-3 but percentage allows for different maximums)

`kb-light` Manage keyboard backlight
   - `show` Show current keyboard backlight level

   - `set` Set keyboard backlight brightness as a percentage


### Performance mode profile
Manage power profile through cli (becaus  linux mint doesn't show low-power (fan off) modus)

`profile` Manage Performace mode profile
   - `show` shows possible choices for power profiles in oder from low power to high power

   - `set [name]` Set performace profile (with autocomplete for name)


## Installation
requires Python > 3.9

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
This project is licensed under the terms of the MIT license. check the [LICENCE](https://github.com/Ryan-Diazz/GalaxyBook-Firmware-Driver-CLI/blob/main/LICENCE) File for more information


# About
Running linux on an Samsung Galaxy Book 4 (NP750XGJ) has proven quite a challange. Thanks to the awesome work of Joshua Grisham's [samsung-galaxybook-extras](https://github.com/joshuagrisham/samsung-galaxybook-extras), the Driver situation has massively improved. However the software support for the driver has felt a bit lacking. That’s why I started building this CLI, to make managing my machine a bit more user friendly.

I should have all the important features implemented, but since this project is open source on GitHub, feel free to contribute! If something is missing, broken, or could be improved, don’t hesitate to open a pull request.

Have a wonderful day and enjoy easier management,

Ryan