Simple tool for symbol math:

Is parse ascii-format formulas into function tree

List of commands:

setvar var_name float_value -- adds to work environment var name with float value
setfun func_name function_in_ascii_format -- adds to work environment symbolic function. 
diff func_name var -- show derivative of function by var variable (it is not nessesary to be variable in work environment)
clear,clearvar,clearfunc -- clear all/all variables/all functions from the work environment
calc func_name -- calculate (or simlify) function with variables in work environment
plot (x1,y1,z1) -- plots 3d points on graph with mathplotlib. Example:

plot (1,2,3) (2^2,4*5,8) -- 2 points
plot (1,2,3) (sin(2)*exp(cos(3)+ln(3)/4),4,5) -- Can evaluate formulas in coordinates, if they can be simplified to a real value


exit -- shuts down programm session

Feel free to use any part of this code)


