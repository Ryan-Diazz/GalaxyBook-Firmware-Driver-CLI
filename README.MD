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

### 1. Download the '*.deb' from the latest release

   Navigate to the [Latest release](https://github.com/Ryan-Diazz/GalaxyBook-Firmware-Driver-CLI/releases/latest), From there download the latest `galaxybook-firmware-driver-cli_x.x.x_all.deb` file

### 2. Install using dpkg

   On Debian/Ubuntu:
   ```bash
   sudo dpkg -i galaxybook-firmware-driver-cli_x.x.x_all.deb
   ```

### 3. Enjoy!

   Run
   ```bash
   galaxybook
   ```
   An help overview should appear with all the possible function currently implementented in `galaxybook-cli`


# License
This project is licensed under the terms of the MIT license. check the [LICENCE](https://github.com/Ryan-Diazz/GalaxyBook-Firmware-Driver-CLI/blob/main/LICENCE) File for more information

# Build
For build instructions please read [BUILD](https://github.com/Ryan-Diazz/GalaxyBook-Firmware-Driver-CLI/blob/main/BUILD.md).

# About
Running linux on an Samsung Galaxy Book 4 (NP750XGJ) has proven quite a challange. Thanks to the awesome work of Joshua Grisham's [samsung-galaxybook-extras](https://github.com/joshuagrisham/samsung-galaxybook-extras), the Driver situation has massively improved. However the software support for the driver has felt a bit lacking. That’s why I started building this CLI, to make managing my machine a bit more user friendly.

I should have all the important features implemented, but since this project is open source on GitHub, feel free to contribute! If something is missing, broken, or could be improved, don’t hesitate to open a pull request.

Have a wonderful day and enjoy easier management,

Ryan
