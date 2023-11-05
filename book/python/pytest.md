
## Pytest

```bash
# run pytest
pytest test.py
pytest --verbose code.py::test_func
pytest --verbose code.py::classname::test_func

pytest -v -k TestClassName
pytest -v --tb=no -k "equality and not equality_fail"

    # only run tests which failed on last run
pytest --lf

# Parallel testing
# with pytest-xdist
pytest -s -v -n auto
    # n - the number of available CPUs

# View TRACE
# https://trace.playwright.dev/


pytest --setup-show test_name.py

pytest --fixtures -v

# flags
    -s aka --capture=no  # to see print output
    --setup-show  # is used to see the order of execution
    -r  # to report reasons for different test results at the end of the session
    -ra  # stands for “all except passed.”
```


## REPORT

```bash
# REPORTS
    # installation, need java to run allure
scoop install allure
allure --version
    # run with allur report
pytest --alluredir=<path to report directory> test.py
pytest --alluredir=.report/allure-results

allure serve <path to report directory>
allure serve .report/allure-results
# or
allure generate

# pytest-html
$ pytest --html=.report/report.html --self-contained-html
```


## Playwright

```bash
# PLAYWRIGHT
# browser
playwright uninstall --all
playwright install --help
# Install custom browsers, supports chromium, chrome, chrome-beta, msedge, msedge-beta, msedge-dev, firefox, webkit. 
playwright install chromium

# update
pip install pytest-playwright playwright -U

# RUN TEST
# Running tests in headed mode
pytest --headed test_login.py

# Running Tests on multiple browsers
pytest test_login.py --browser webkit --browser firefox
--slowmo # Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on (default: 0)
--output # Directory for artifacts produced by tests (default: test-results)

pytest -v --headed --slowmo 100 src/tests/ui_playwrt/test_form.py

# browser
pytest -v --browser firefox --browser chromium
pytest test_login.py --browser-channel msedge

# DEBUG MODE
# run in debug mode
PWDEBUG=1 pytest -s
    # windows 
$env:PWDEBUG=1

# Test generator
playwright codegen demo.playwright.dev/todomvc
playwright codegen --ignore-https-errors https://example.com
playwright codegen --viewport-size=800,600 playwright.dev
playwright codegen --device="iPhone 13" playwright.dev

playwright codegen --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" bing.com/maps

playwright codegen github.com/microsoft/playwright --save-storage=.auth/user.json
playwright codegen --load-storage=.auth/user.json github.com/microsoft/playwright
```