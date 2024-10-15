# Certn SDET Selenium Assessment

## Setup

You must have installed,

- Google Chrome
- Python 3.11+
- Git

If you wish to use a different web browser and need help doing so, please ask
your interviewer for the modifications needed.

You'll then need to set up dependencies for this project:

- **Windows**: Open this folder and double-click the `windows-py-setup.bat` file
  (Python.org install) or `windows-python-setup.bat` (Windows Store or PATH
  installation)
- **macOS**: Run `unix-setup` in Terminal. Alternatively, you can double-click
  it in Finder and bypass the warnings.
- **Linux**: Run `./unix-setup`

These scripts set up a "virtual environment" in the local folder, and won't
impact your system installation of browsers and/or Python.

## Running the Tests

Depending on your IDE and configuration, you may be able to run tests directly
from the IDE.

However, as a backup, you can always run via the command line or script
provided.

- **Windows**: Open this folder and double-click the `windows-run-tests.bat` file
- **macOS**: Run `unix-run-tests` in Terminal. Alternatively, you can
  double-click it in Finder and bypass the warnings.
- **Linux**: Run `./unix-run-tests`

## Your Task

You will know environment setup is successful and ready for you to begin the
assessment when:

- Running the tests results in 2 failures (`NotImplementedError`)
- Running the tests results in 0 errors
- Two browser windows should briefly appear

When your assessment is complete, tests should pass when running as per the
above instructions.
