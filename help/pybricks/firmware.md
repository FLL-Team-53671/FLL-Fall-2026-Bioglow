# Compiling PyBricks firmware

To disable the slots functionality in PyBricks, I had to do a bunch of steps.
(I'm probably missing a couple of them here.)

See: https://github.com/pybricks/pybricks-micropython/blob/master/CONTRIBUTING.md

Clone the pybricks-micropython repository: `git clone
https://github.com/pybricks/pybricks-micropython`

Run `uv sync` and `source .venv/bin/activate`

I had to disable `no-build` in pyproject.toml and install a bunch of
prerequisite packages because uv couldn't download a build of pygame that was
compatible with the newer Python interpreter in Fedora. Packages I had to
install included:

- SDL2-devel
- arm-none-eabi-gcc-cs
- arm-none-eabi-newlib
- freetype-devel

Update to the latest released version of pybricks-micropython. In my case, this
meant: `git checkout tags/v4.1.3 -b v4.1.3`

Edit `lib/pbio/platform/prime_hub_f4/pbsysconfig.h` and set
`PBSYS_CONFIG_HMI_NUM_SLOTS` and `PBSYS_CONFIG_STORAGE_NUM_SLOTS` to 1 instead
of 5.

Compile: `make mpy-cross -j8; make -C bricks/primehub -j8`

Flash the SPIKE Prime Hub with the new firmware. This seems to only work with
the flash tool at code.pybricks.com.  The file is:
bricks/primehub_f4/build/firmware.zip`
