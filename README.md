# code-wars

Repo showing how to setup basic unit testing in pycharm using [code wars](https://www.codewars.com/) problems as
examples

## Getting started

1. once you've opened the project in pycharm, navigate to `file` > `settings` > `tools` > `python integrated tools`
2. make sure your `default test runner` is set to `Unittests` or `Autodetect (Unittests)`
    1. If you have to change your test runner, you might get a message about your project. Just click the fix button  
       <img alt="settings" src="/admin/image/settings_unit_tests.png"/>
3. to create a new function, copy below and paste it to the bottom of `kyu_six.py` OR follow the same format to create a
new kyu file. Below is the minimum you should have.
   ```python
   def function_name(arg): # pick a name that makes sense
      """kata prompt"""
      # your code here       
      return False
   ```
5. once you've added your first function to your new file, move the cursor to the function name and hit `ctrl` + `shift` + `t`
6. select `Create New Test...` and click `ok` on the popup box
7. in the new test file, follow the layout of the existing test files. Use the data provided by code wars prompt to test
   for the results against the expected values