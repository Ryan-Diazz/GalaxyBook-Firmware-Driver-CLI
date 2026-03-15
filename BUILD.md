for people wanting to build their own version, following are the build steps i used to build my version.

The following build instructions are adjusted to systems using **externally managed Python** (common on Debian/Ubuntu).


## 1. Create a virtual environment for python build

From inside the project directory, run:

```bash
python3 -m venv .venv
```

this creates an virtual enviroment to activate it, run:

```bash
source .venv/bin/activate
```

Your shell should now show `(.venv)`.


## 2. Install python build tools

Inside the venv:

```bash
pip install --upgrade pip
pip install build
```

The **build** package is now installed in the virtual environment.


## 3. Build the Python distribution

Run:

```bash
python -m build
```

This produces:

```
dist/
  galaxybook-x.x.x.tar.gz
  galaxybook-x.x.x-py3-none-any.whl
```

You can test install it in the venv with:

```bash
pip install dist/galaxybook-x.x.x-py3-none-any.whl
```

Then test it as usual with:

```bash
galaxybook
```

## 4. Deactivate the virtual environment

Once the build works:

```bash
deactivate
```

The build artifacts remain in `dist/`.

## 5. Create the Debian packaging

Install Debian packaging tools from APT:

```bash
sudo apt install dh-python debhelper devscripts build-essential
```

## 6. Build the `.deb`

Run:

```bash
debuild -us -uc
```

This produces:

```
../galaxybook-firmware-driver-cli_x.x.x_all.deb
```
among other artifacts

## 7. Install it:

```bash
sudo dpkg -i ../galaxybook-firmware-driver-cli_x.x.x_all.deb
```

Now `galaxybook` should work system wide.
