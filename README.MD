# Galaxy Book Recording Block command

`recording` is a simple command-line utility for managing the 'Block Recording' feature present in the samsung-galaxybook firmware present in linux kernel 6.15 and up.

## Usage

`recording` gives the possible argument options accepted by the script

`recording show` gives the current status of the 'Block Recording'

`recording on` enables 'Block Recording', thus disabling the webcam

`recording off` disables 'Block Recording', thus enabling the webcam

`recording toggle` toggles 'Block Recording'

## Installation

1. Download or save the script as `recording.sh`
2. Make the script executable

   ```bash
   chmod +x recording.sh
   ```

3. Move the script to `/usr/local/bin`

   ```bash
   sudo mv recording.sh /usr/local/bin/recording
   ```
   Note that it renamed `recording.sh` to `recording` this makes sure that you don't have to type '.sh' everytime you want to use the command


4. (Optional) Enable passwordless `sudo` for this command

   To allow the command to run without prompting for a password when writing to the firmware attribute:

   ```bash
   sudo visudo
   ```

   Add the following line at the end of the file (replace `youruser` with your username):

   ```
   youruser ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/class/firmware-attributes/samsung-galaxybook/attributes/block_recording/current_value
   ```

   This allows `sudo tee` to write to the attribute file without exposing full sudo privileges.
