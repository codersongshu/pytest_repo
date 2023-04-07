https://www.youtube.com/watch?v=_QtM7QGuj1A&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=1

1. To run the test, go to the folder and run:
	pytest test_file_name.py

2. Verbose result
	pytest -v test_file_name.py

https://www.youtube.com/watch?v=VKY-0LEmrwk&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=2

3. Run only one test in a file instead of all the tests
	pytest test_math_func.py::test_add -v

4. Run the test based on the names of the test (use -k option)
	pytest -v -k “add”

	we can use ‘or’ and ‘and’ keyword as well
		pytest -v -k “add or string”
		pytest -v -k “add and string”

5. Run the tests based on mark
	- Import pytest library in the file where tests are
		import pytest
	- add the mark on top of each test
		@pytest.mark.number
		@pytest.mark.strings
	- run tests in terminal
		pytest -v -m number

6. Exit first - when first failure occurs, pytest will exit from the execution of tests
	pytest -v -x

7. Other commands
	- clear results
		clear
	- hide stack trace
		pytest -v -x --tb=no
	- max failure
		pytest -v --maxfail=2
	- skip a test: add this marker on top of a test
		@pytest.mark.skip(reason=“Do not run this test.” )
	- skip if condition: skip only if some condition is satisfied (skip if python version is less than 3 (min, max))
		import sys
		@pytest.mark.skipif(sys.version_info < (3,3), reason=“Do not run this test.” )
	- ’s’ option allows print statement to be executed
		add a print statement in the test
		Eg: print(match_func.add(7,3), ‘——————————’)

		and in terminal add below command
		pytest -v -s test_math_func.py
 		or
		pytest -v --capture=no
	- quite mode: q
		pytest -v -q

https://www.youtube.com/watch?v=7qMhuVGqGY4&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=3

8. Parametrize tests
	import math_func
	import pytest
	import sys

	@pytest.mark.parametrize('num1, num2, result',
                         [(7,3,10),('Hello',' World','Hello World'),(10.5,5.5,16)]
                         )
	def test_add(num1, num2, result):
		assert math_func.add(num1,num2) == result

https://www.youtube.com/watch?v=JJmTO95AoqE&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=4

9. Setup and teardown meadtho
	- Setup and tear down meathod (use -s option to see the print statement and see the results)
		we need to create two functions - setup_module and teardown_module to create and destroy the resources
		Example:
		
		def setup_module(module):
  			print('----------setup------------')
  			global db
  			db = studentDB()
 			db.connect('data.json')

		def teardown_module(module):
    			print('----------teardown------------')
   			 db.close()
		
10. Fixtures
	- we can use fixtures which will run the code before test cases and set up any resources if needed
	- scope = ‘module’ makes the setup par only run once
	- if we want to tear down, then use ‘yield’ instead of return
 
	@pytest.fixture(scope='module')
	def db():
    		print('----------setup------------')
    		db = studentDB()
    		db.connect('data.json')
    		# return db
    		yield db
    		print('----------teardown------------')
    		db.close()

https://www.youtube.com/watch?v=2sb5JJLpzw8&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=6

11. Run pytest with PyCharm

	Go to
		PyCharm -> Settings -> Tools -> Python Integrated Tools -> Testing -> Default Test Runner -> pytest

	Add verbose argument
		Go to the dropdown on top saying ‘pytest in …file’ -> Edit Configurations ->  Additional arguments = -v -s
