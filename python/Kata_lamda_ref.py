# lamda functions and code snippets

# http://www.secnetix.de/olli/Python/lambda_functions.hawk

def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print(f)
print(g)


g_incr = g(42)
print(g_incr)

