import sympy

formula = "12+x"
x = sympy.Symbol("x")
nx = sympy.sympify("x-1")
formula = sympy.sympify(formula)
formula = formula.factor(formula)
func = sympy.integrate(formula, x)
cont = True

while(cont):
    new_expression = func.subs(x, nx)
    difference = sympy.Add(func, -new_expression)
    diff = sympy.simplify(difference)
    difference = -sympy.Add(diff, -formula.factor())
    if (diff==formula):
        cont = False
        break
    new_part = sympy.integrate(difference, x)
    func = sympy.Add(new_part, func)
print(sympy.factor(func))

