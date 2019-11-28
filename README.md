# LiveChat test in Python(Selenium)
Selenium Project

Testing LiveChat application

For run the tests you will need:

allure-pytest                   2.8.6
allure-python-commons           2.8.6
pytest                          5.0.1
pytest-ordering                 0.6
selenium                        3.141.0


Python3
chromedriver (https://chromedriver.chromium.org/)



After that open console, navigate to project foler and run:
py.test -v -s
or 
py.test --alluredir=%allure_result_folder% ./tests
allure serve %allure_result_folder%
For generate report from tests


