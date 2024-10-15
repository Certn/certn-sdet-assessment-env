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

However, you can always run via the command line or script provided:
- **Windows**: Open this folder and double-click the `windows-run-[TOOL]-test.bat`
  file
- **macOS**: Run `unix-run-[TOOL]-tests` in Terminal. Alternatively, you can
  double-click it in Finder and bypass the warnings.
- **Linux**: Run `./unix-run-[TOOL]-tests`
where `TOOL` can be either `playwright` or `selenium`.

## Your Task

Currently, there is a missing implementation in the test. You'll find a test file
that uses either Playwright or Selenium.

- Running the tests results in 1 failure (`NotImplementedError`)
- Running the tests results in 0 errors
- Two browser windows should briefly appear

When your assessment is complete, tests should pass when running as per the
above instructions.
