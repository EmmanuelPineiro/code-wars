# code-wars

Repo showing how to setup basic unit testing in pycharm using [code wars](https://www.codewars.com/) problems as
examples

## Getting started

1. once you've opened the project in pycharm, navigate to `file` > `settings` > `tools` > `python integrated tools`
2. make sure your `default test runner` is set to `Unittests` or `Autodetect (Unittests)`
    1. If you have to change your test runner, you might get a message about your project. Just click the fix button  
       <img alt="\
   ```
4. once you've added your first function to your new file, move the cursor to the function name and hit `ctrl` + `shift` + `t`
5. select `Create New Test...`, update the class name to be your function name in CamelCase, and click `ok` on the popup box  
    <img alt="new unit test setup" src="/admin/image/new_unit_test_setup.png"/>
6. in the new test file, follow the layout of the existing test files. Use the data provided by code wars prompt to test
   for the results against the expected values