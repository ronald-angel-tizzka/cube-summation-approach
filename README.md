# README #

Cube Summation problem (https://www.hackerrank.com/challenges/cube-summation) solution using a python dictionaries approach. 

Main Modules:


- summation_service = exposes a REST service to call the summation_service process using FLASK.
- cube_summation.py = manages the general logic for the summation operation. Uses some reusable objects like rows and the 
   matrix utils with the main lambda functions used in the process. 
- matrix_utils = helper class with main lambda functions used through the process. 
- file_helper.py = manages the persistence in this case using file input and output.


Run test on:

service/test/summation_test.py