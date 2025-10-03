import argparse

def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

parser = argparse.ArgumentParser()
parser.add_argument("expression", help="The expression to evaluate")
args = parser.parse_args()

result = calculate(args.expression)
print(f"Result: {result}")