First create a virtual environment using Python 3.10

Install packages that are in ***requirements.txt***

Create a directory in project root called *reports* and leave it blank.
When you start a test run, at the end of the run, an HTML and .png files(if any test fails) will be added to the directory.
Whenever a new test run will start, the content inside *reports* will be deleted.
*reports* folder and content inside it are ignored and won't be pushed to github.

Create a file ***config.py*** inside the *config* package and paste this code inside:
> import os
> 
>    class SetupData:
> 
>    BASE_URL = [Page URL]
> 
>    BROWSER = [Browser you want to run your test in, it should be all in capital letters]
> 
>    HEADLESS_BROWSER = [True when you want to run tests normally, False whenever tests run in CI pipeline]
> 
>    os.environ['GH_TOKEN'] = [github token that is used for webdriver manager]

You must fill all variables with your own information.
**config.py** file is ignored and won't get pushed to github.

Attached find a link on how to generate a github token for webdriver manager: https://github.com/SergeyPirogov/webdriver_manager#gh_token

Create a YML file called ***credentials.yml*** inside the *test_data* package and paste this code inside:
>user-credentials:
> 
>  email: [email to login to app with]
> 
>  password: [password]
>
>wrong-credentials:
> 
>  email: "wrong@email.com"
> 
>  password: "WrongPassword"

Command to run all tests that are inside the *tests* directory(without generating a report):
> pytest tests

Command to run tests on a specific class inside *tests* directory(without generating report):
> pytest tests/[nameOfTestFile.py]

Command to run tests that are inside *tests* directory and generating report:
> pytest -v tests --html=reports/report.html --self-contained-html