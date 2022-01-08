# code-wars
Repo showing how to setup basic unit testing in pycharm using [code wars](https://www.codewars.com/) problems as examples

## Getting started 
1. once you've opened the project in pycharm, navigate to `file` > `settings` > `tools` > `python integrated tools`
2. make sure your `default test runner` is set to `pytest` or `Autodetect (pytest)`
    1. If you have to change your test runner, you might get a message about your project. Just click the fix button  
      <img alt="settings" src="/admin/image/settings_unit_tests.png"/>
3. follow the file layout to add a new problem in the `src` directory
4. once you've added your first function to your new file, move the cursor to the function name and hit `ctrl` + `shift` + `t`
5. select `Create New Test...` and click `ok` on the popup box
6. in the new test file, follow the layout of the existing test files using the data provided by code wars to the proper results and expected values