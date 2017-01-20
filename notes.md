# Experiments

## Python works:

```
ml> python --version
Python 2.7.10
```

```
ml> python py/quicksort.py
pivot 10 left [3, 6, 8, 1, 2, 1] right []
pivot 1 left [] right [3, 6, 8, 2]
pivot 8 left [3, 6, 2] right []
pivot 6 left [3, 2] right []
pivot 2 left [] right [3]
[1, 1, 2, 3, 6, 8, 10]
ml>
```

## Installying 'scipy'

```
ml> brew install homebrew/python/scipy
==> Tapping homebrew/python
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-python'...
remote: Counting objects: 22, done.
remote: Compressing objects: 100% (22/22), done.
remote: Total 22 (delta 1), reused 6 (delta 0), pack-reused 0
Unpacking objects: 100% (22/22), done.
Checking connectivity... done.
Tapped 18 formulae (63 files, 97.1K)
==> Installing scipy from homebrew/python
==> Installing dependencies for homebrew/python/scipy: gmp, mpfr, libmpc, isl, gcc, homebrew/python/numpy
==> Installing homebrew/python/scipy dependency: gmp
==> Downloading https://homebrew.bintray.com/bottles/gmp-6.1.2.yosemite.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring gmp-6.1.2.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/gmp/6.1.2: 18 files, 3.1M
==> Installing homebrew/python/scipy dependency: mpfr
==> Downloading https://homebrew.bintray.com/bottles/mpfr-3.1.5.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring mpfr-3.1.5.yosemite.bottle.tar.gz
🍺  /usr/local/Cellar/mpfr/3.1.5: 25 files, 3.6M
==> Installing homebrew/python/scipy dependency: libmpc
==> Downloading https://homebrew.bintray.com/bottles/libmpc-1.0.3.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libmpc-1.0.3.yosemite.bottle.tar.gz
🍺  /usr/local/Cellar/libmpc/1.0.3: 11 files, 350.2K
==> Installing homebrew/python/scipy dependency: isl
==> Downloading https://homebrew.bintray.com/bottles/isl-0.18.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring isl-0.18.yosemite.bottle.tar.gz
🍺  /usr/local/Cellar/isl/0.18: 80 files, 3.8M
==> Installing homebrew/python/scipy dependency: gcc
==> Downloading https://homebrew.bintray.com/bottles/gcc-6.3.0_1.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring gcc-6.3.0_1.yosemite.bottle.tar.gz
==> Caveats
GCC has been built with multilib support. Notably, OpenMP may not work:
  https://gcc.gnu.org/bugzilla/show_bug.cgi?id=60670
If you need OpenMP support you may want to
  brew reinstall gcc --without-multilib
==> Summary
🍺  /usr/local/Cellar/gcc/6.3.0_1: 1,436 files, 280.6M
==> Installing homebrew/python/scipy dependency: homebrew/python/numpy
==> Downloading https://homebrew.bintray.com/bottles-python/numpy-1.12.0.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring numpy-1.12.0.yosemite.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/f2py
Target /usr/local/bin/f2py
already exists. You may want to remove it:
  rm '/usr/local/bin/f2py'

To force the link and overwrite all conflicting files:
  brew link --overwrite numpy

To list all files that would be deleted:
  brew link --overwrite --dry-run numpy

Possible conflicting files are:
/usr/local/bin/f2py
==> Caveats
If you use system python (that comes - depending on the OS X version -
with older versions of numpy, scipy and matplotlib), you may need to
ensure that the brewed packages come earlier in Python's sys.path with:
  mkdir -p /Users/home/Library/Python/2.7/lib/python/site-packages
  echo 'import sys; sys.path.insert(1, "/usr/local/lib/python2.7/site-packages")' >> /Users/home/Library/Python/2.7/lib/python/site-packages/homebrew.pth
==> Summary
🍺  /usr/local/Cellar/numpy/1.12.0: 440 files, 9.6M
==> Installing homebrew/python/scipy
==> Downloading https://homebrew.bintray.com/bottles-python/scipy-0.18.1.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring scipy-0.18.1.yosemite.bottle.tar.gz
==> Caveats
If you use system python (that comes - depending on the OS X version -
with older versions of numpy, scipy and matplotlib), you may need to
ensure that the brewed packages come earlier in Python's sys.path with:
  mkdir -p /Users/home/Library/Python/2.7/lib/python/site-packages
  echo 'import sys; sys.path.insert(1, "/usr/local/lib/python2.7/site-packages")' >> /Users/home/Library/Python/2.7/lib/python/site-packages/homebrew.pth
==> Summary
🍺  /usr/local/Cellar/scipy/0.18.1: 1,124 files, 42.5M
ml>
```

## Problems running cat.py

Attempting to install 'openssl'...

See https://github.com/Homebrew/legacy-homebrew/issues/22816

```
py> brew install openssl
Warning: openssl is a keg-only and another version is linked to opt.
Use `brew install --force` if you want to install this version
py> brew link openssl --force
Warning: Refusing to link: openssl
Linking keg-only openssl means you may end up linking against the insecure,
deprecated system OpenSSL while using the headers from Homebrew's openssl.
Instead, pass the full include/library paths to your compiler e.g.:
  -I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib
py> brew uninstall python
Uninstalling /usr/local/Cellar/python/2.7.10_1... (6,241 files, 83.3M)
py> brew install python --with-brewed-openssl
==> Installing dependencies for python: readline, sqlite
==> Installing python dependency: readline
==> Downloading https://homebrew.bintray.com/bottles/readline-7.0.1.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring readline-7.0.1.yosemite.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local.

macOS provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only.


Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/readline/lib
    CPPFLAGS: -I/usr/local/opt/readline/include

==> Summary
🍺  /usr/local/Cellar/readline/7.0.1: 46 files, 2.1M
==> Installing python dependency: sqlite
==> Downloading https://homebrew.bintray.com/bottles/sqlite-3.16.2.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring sqlite-3.16.2.yosemite.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local.

macOS provides an older sqlite3.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/sqlite/lib
    CPPFLAGS: -I/usr/local/opt/sqlite/include
    PKG_CONFIG_PATH: /usr/local/opt/sqlite/lib/pkgconfig

==> Summary
🍺  /usr/local/Cellar/sqlite/3.16.2: 11 files, 3.0M
Warning: python: this formula has no --with-brewed-openssl option so it will be ignored!
==> Installing python
==> Downloading https://homebrew.bintray.com/bottles/python-2.7.13.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring python-2.7.13.yosemite.bottle.tar.gz
==> Using the sandbox
==> /usr/local/Cellar/python/2.7.13/bin/python -s setup.py --no-user-cfg install --force --verbose --single-version-externally-managed --record=installed.txt --
==> /usr/local/Cellar/python/2.7.13/bin/python -s setup.py --no-user-cfg install --force --verbose --single-version-externally-managed --record=installed.txt --
==> /usr/local/Cellar/python/2.7.13/bin/python -s setup.py --no-user-cfg install --force --verbose --single-version-externally-managed --record=installed.txt --
==> Caveats
Pip and setuptools have been installed. To update them
  pip install --upgrade pip setuptools

You can install Python packages with
  pip install <package>

They will install into the site-package directory
  /usr/local/lib/python2.7/site-packages

See: http://docs.brew.sh/Homebrew-and-Python.html

.app bundles were installed.
Run `brew linkapps python` to symlink these to /Applications.
==> Summary
🍺  /usr/local/Cellar/python/2.7.13: 3,526 files, 48M
py>
```

Ok, abandoned Homebrew for this stuff; using 'pip'....
```
py> which pip
/usr/local/bin/pip
py> python -m pip install --upgrade pip
Requirement already up-to-date: pip in /usr/local/lib/python2.7/site-packages
py> pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
Requirement already satisfied: numpy in /usr/local/lib/python2.7/site-packages
Requirement already satisfied: scipy in /usr/local/lib/python2.7/site-packages
Collecting matplotlib
  Downloading matplotlib-2.0.0-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (12.8MB)
    100% |████████████████████████████████| 12.8MB 92kB/s
Collecting ipython
  Downloading ipython-5.1.0-py2-none-any.whl (747kB)
    100% |████████████████████████████████| 747kB 1.1MB/s
Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl
Collecting pandas
  Downloading pandas-0.19.2-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (11.9MB)
    100% |████████████████████████████████| 11.9MB 101kB/s
Collecting sympy
  Downloading sympy-1.0.tar.gz (4.3MB)
    100% |████████████████████████████████| 4.3MB 258kB/s
Requirement already satisfied: nose in /usr/local/Cellar/numpy/1.12.0/libexec/nose/lib/python2.7/site-packages
Collecting pyparsing!=2.0.0,!=2.0.4,!=2.1.2,!=2.1.6,>=1.5.6 (from matplotlib)
  Downloading pyparsing-2.1.10-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 3.1MB/s
Collecting functools32 (from matplotlib)
  Downloading functools32-3.2.3-2.zip
Collecting pytz (from matplotlib)
  Downloading pytz-2016.10-py2.py3-none-any.whl (483kB)
    100% |████████████████████████████████| 491kB 1.7MB/s
Collecting six>=1.10 (from matplotlib)
  Downloading six-1.10.0-py2.py3-none-any.whl
Collecting cycler>=0.10 (from matplotlib)
  Downloading cycler-0.10.0-py2.py3-none-any.whl
Collecting subprocess32 (from matplotlib)
  Downloading subprocess32-3.2.7.tar.gz (54kB)
    100% |████████████████████████████████| 61kB 3.2MB/s
Collecting python-dateutil (from matplotlib)
  Downloading python_dateutil-2.6.0-py2.py3-none-any.whl (194kB)
    100% |████████████████████████████████| 194kB 2.4MB/s
Collecting decorator (from ipython)
  Downloading decorator-4.0.11-py2.py3-none-any.whl
Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python2.7/site-packages (from ipython)
Collecting pickleshare (from ipython)
  Downloading pickleshare-0.7.4-py2.py3-none-any.whl
Collecting backports.shutil-get-terminal-size; python_version == "2.7" (from ipython)
  Downloading backports.shutil_get_terminal_size-1.0.0-py2.py3-none-any.whl
Collecting pygments (from ipython)
  Downloading Pygments-2.1.3-py2.py3-none-any.whl (755kB)
    100% |████████████████████████████████| 757kB 1.2MB/s
Collecting pexpect; sys_platform != "win32" (from ipython)
  Downloading pexpect-4.2.1-py2.py3-none-any.whl (55kB)
    100% |████████████████████████████████| 61kB 3.2MB/s
Collecting pathlib2; python_version == "2.7" or python_version == "3.3" (from ipython)
  Downloading pathlib2-2.2.1-py2.py3-none-any.whl
Collecting simplegeneric>0.8 (from ipython)
  Downloading simplegeneric-0.8.1.zip
Collecting prompt-toolkit<2.0.0,>=1.0.3 (from ipython)
  Downloading prompt_toolkit-1.0.9-py2-none-any.whl (241kB)
    100% |████████████████████████████████| 245kB 2.4MB/s
Collecting traitlets>=4.2 (from ipython)
  Downloading traitlets-4.3.1-py2.py3-none-any.whl (74kB)
    100% |████████████████████████████████| 81kB 3.8MB/s
Collecting appnope; sys_platform == "darwin" (from ipython)
  Downloading appnope-0.1.0-py2.py3-none-any.whl
Collecting ipywidgets (from jupyter)
  Downloading ipywidgets-5.2.2-py2.py3-none-any.whl (43kB)
    100% |████████████████████████████████| 51kB 4.1MB/s
Collecting qtconsole (from jupyter)
  Downloading qtconsole-4.2.1-py2.py3-none-any.whl (104kB)
    100% |████████████████████████████████| 112kB 3.5MB/s
Collecting nbconvert (from jupyter)
  Downloading nbconvert-5.0.0-py2.py3-none-any.whl (371kB)
    100% |████████████████████████████████| 378kB 1.8MB/s
Collecting notebook (from jupyter)
  Downloading notebook-4.3.1-py2.py3-none-any.whl (6.8MB)
    100% |████████████████████████████████| 6.8MB 167kB/s
Collecting jupyter-console (from jupyter)
  Downloading jupyter_console-5.0.0-py2.py3-none-any.whl
Collecting ipykernel (from jupyter)
  Downloading ipykernel-4.5.2-py2.py3-none-any.whl (98kB)
    100% |████████████████████████████████| 102kB 3.3MB/s
Collecting mpmath>=0.19 (from sympy)
  Downloading mpmath-0.19.tar.gz (498kB)
    100% |████████████████████████████████| 501kB 1.5MB/s
Collecting ptyprocess>=0.5 (from pexpect; sys_platform != "win32"->ipython)
  Downloading ptyprocess-0.5.1-py2.py3-none-any.whl
Collecting scandir; python_version < "3.5" (from pathlib2; python_version == "2.7" or python_version == "3.3"->ipython)
  Downloading scandir-1.4.zip
Collecting wcwidth (from prompt-toolkit<2.0.0,>=1.0.3->ipython)
  Downloading wcwidth-0.1.7-py2.py3-none-any.whl
Collecting enum34; python_version == "2.7" (from traitlets>=4.2->ipython)
  Downloading enum34-1.1.6-py2-none-any.whl
Collecting ipython-genutils (from traitlets>=4.2->ipython)
  Downloading ipython_genutils-0.1.0-py2.py3-none-any.whl
Collecting widgetsnbextension>=1.2.6 (from ipywidgets->jupyter)
  Downloading widgetsnbextension-1.2.6-py2.py3-none-any.whl (1.5MB)
    100% |████████████████████████████████| 1.5MB 640kB/s
Collecting jupyter-client>=4.1 (from qtconsole->jupyter)
  Downloading jupyter_client-4.4.0-py2.py3-none-any.whl (76kB)
    100% |████████████████████████████████| 81kB 3.9MB/s
Collecting jupyter-core (from qtconsole->jupyter)
  Downloading jupyter_core-4.2.1-py2.py3-none-any.whl (125kB)
    100% |████████████████████████████████| 133kB 3.0MB/s
Collecting entrypoints>=0.2.2 (from nbconvert->jupyter)
  Downloading entrypoints-0.2.2-py2.py3-none-any.whl
Collecting nbformat (from nbconvert->jupyter)
  Downloading nbformat-4.2.0-py2.py3-none-any.whl (153kB)
    100% |████████████████████████████████| 153kB 2.8MB/s
Collecting pandocfilters>=1.4.1 (from nbconvert->jupyter)
  Downloading pandocfilters-1.4.1.tar.gz
Collecting testpath (from nbconvert->jupyter)
  Downloading testpath-0.3-py2.py3-none-any.whl (82kB)
    100% |████████████████████████████████| 92kB 3.3MB/s
Collecting bleach (from nbconvert->jupyter)
  Downloading bleach-1.5.0-py2.py3-none-any.whl
Collecting jinja2 (from nbconvert->jupyter)
  Downloading Jinja2-2.9.4-py2.py3-none-any.whl (274kB)
    100% |████████████████████████████████| 276kB 2.7MB/s
Collecting mistune!=0.6 (from nbconvert->jupyter)
  Downloading mistune-0.7.3-py2.py3-none-any.whl
Collecting terminado>=0.3.3; sys_platform != "win32" (from notebook->jupyter)
  Downloading terminado-0.6.tar.gz
Collecting tornado>=4 (from notebook->jupyter)
  Downloading tornado-4.4.2.tar.gz (460kB)
    100% |████████████████████████████████| 460kB 1.5MB/s
Collecting pyzmq>=13 (from jupyter-client>=4.1->qtconsole->jupyter)
  Downloading pyzmq-16.0.2-cp27-cp27m-macosx_10_6_intel.whl (1.1MB)
    100% |████████████████████████████████| 1.1MB 890kB/s
Collecting configparser>=3.5; python_version == "2.7" (from entrypoints>=0.2.2->nbconvert->jupyter)
  Downloading configparser-3.5.0.tar.gz
Collecting jsonschema!=2.5.0,>=2.4 (from nbformat->nbconvert->jupyter)
  Downloading jsonschema-2.5.1-py2.py3-none-any.whl
Collecting html5lib!=0.9999,!=0.99999,<0.99999999,>=0.999 (from bleach->nbconvert->jupyter)
  Downloading html5lib-0.9999999.tar.gz (889kB)
    100% |████████████████████████████████| 890kB 1.0MB/s
Collecting MarkupSafe>=0.23 (from jinja2->nbconvert->jupyter)
  Downloading MarkupSafe-0.23.tar.gz
Collecting singledispatch (from tornado>=4->notebook->jupyter)
  Downloading singledispatch-3.4.0.3-py2.py3-none-any.whl
Collecting certifi (from tornado>=4->notebook->jupyter)
  Downloading certifi-2016.9.26-py2.py3-none-any.whl (377kB)
    100% |████████████████████████████████| 378kB 1.8MB/s
Collecting backports_abc>=0.4 (from tornado>=4->notebook->jupyter)
  Downloading backports_abc-0.5-py2.py3-none-any.whl
Building wheels for collected packages: sympy, functools32, subprocess32, simplegeneric, mpmath, scandir, pandocfilters, terminado, tornado, configparser, html5lib, MarkupSafe
  Running setup.py bdist_wheel for sympy ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/05/93/22/2d0f59d842347b1f38df0d3f7a3870586df60568d2a49d94c5
  Running setup.py bdist_wheel for functools32 ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/3c/d0/09/cd78d0ff4d6cfecfbd730782a7815a4571cd2cd4d2ed6e69d9
  Running setup.py bdist_wheel for subprocess32 ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/7d/4c/a4/ce9ceb463dae01f4b95e670abd9afc8d65a45f38012f8030cc
  Running setup.py bdist_wheel for simplegeneric ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/7b/31/08/c85e74c84188cbec6a6827beec4d640f2bd78ae003dc1ec09d
  Running setup.py bdist_wheel for mpmath ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/02/2b/99/cd867d5da48d951118a8020e86c0c12a65022702426582d4b8
  Running setup.py bdist_wheel for scandir ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/31/79/6f/d0107427b00f37471daff10cdd0262dd981f55b24154040f30
  Running setup.py bdist_wheel for pandocfilters ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/d4/01/68/49055c80b9f01ccb49241e73c8019628605064730941d70b56
  Running setup.py bdist_wheel for terminado ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/3b/c2/ea/af635ffb63857a8c2ddd22da6a4b52f5b7ea3065db94ef5d7c
  Running setup.py bdist_wheel for tornado ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/b3/db/47/46e05d1ee3ecfba252fcab42f0a156dab0df0cddf99fa0827c
  Running setup.py bdist_wheel for configparser ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/1c/bd/b4/277af3f6c40645661b4cd1c21df26aca0f2e1e9714a1d4cda8
  Running setup.py bdist_wheel for html5lib ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/6f/85/6c/56b8e1292c6214c4eb73b9dda50f53e8e977bf65989373c962
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: /Users/home/Library/Caches/pip/wheels/a3/fa/dc/0198eed9ad95489b8a4f45d14dd5d2aee3f8984e46862c5748
Successfully built sympy functools32 subprocess32 simplegeneric mpmath scandir pandocfilters terminado tornado configparser html5lib MarkupSafe
Installing collected packages: pyparsing, functools32, pytz, six, cycler, subprocess32, python-dateutil, matplotlib, decorator, scandir, pathlib2, pickleshare, backports.shutil-get-terminal-size, pygments, ptyprocess, pexpect, simplegeneric, wcwidth, prompt-toolkit, enum34, ipython-genutils, traitlets, appnope, ipython, configparser, entrypoints, jupyter-core, jsonschema, nbformat, pandocfilters, testpath, html5lib, bleach, MarkupSafe, jinja2, mistune, nbconvert, singledispatch, certifi, backports-abc, tornado, terminado, pyzmq, jupyter-client, ipykernel, notebook, widgetsnbextension, ipywidgets, qtconsole, jupyter-console, jupyter, pandas, mpmath, sympy
Successfully installed MarkupSafe-0.23 appnope-0.1.0 backports-abc-0.5 backports.shutil-get-terminal-size-1.0.0 bleach-1.5.0 certifi-2016.9.26 configparser-3.5.0 cycler-0.10.0 decorator-4.0.11 entrypoints-0.2.2 enum34-1.1.6 functools32-3.2.3.post2 html5lib-0.9999999 ipykernel-4.5.2 ipython-5.1.0 ipython-genutils-0.1.0 ipywidgets-5.2.2 jinja2-2.9.4 jsonschema-2.5.1 jupyter-1.0.0 jupyter-client-4.4.0 jupyter-console-5.0.0 jupyter-core-4.2.1 matplotlib-2.0.0 mistune-0.7.3 mpmath-0.19 nbconvert-5.0.0 nbformat-4.2.0 notebook-4.3.1 pandas-0.19.2 pandocfilters-1.4.1 pathlib2-2.2.1 pexpect-4.2.1 pickleshare-0.7.4 prompt-toolkit-1.0.9 ptyprocess-0.5.1 pygments-2.1.3 pyparsing-2.1.10 python-dateutil-2.6.0 pytz-2016.10 pyzmq-16.0.2 qtconsole-4.2.1 scandir-1.4 simplegeneric-0.8.1 singledispatch-3.4.0.3 six-1.10.0 subprocess32-3.2.7 sympy-1.0 terminado-0.6 testpath-0.3 tornado-4.4.2 traitlets-4.3.1 wcwidth-0.1.7 widgetsnbextension-1.2.6
py>
```

Endless hacker nonsense...


```
py> pip install Pillow==2.6.0
Collecting Pillow==2.6.0
  Downloading Pillow-2.6.0-cp27-none-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.whl (2.8MB)
    100% |████████████████████████████████| 2.8MB 398kB/s
Installing collected packages: Pillow
Successfully installed Pillow-2.6.0
```


Now it seems to do something...

```
py> python cat.py
uint8 (196, 236, 3)
py>


