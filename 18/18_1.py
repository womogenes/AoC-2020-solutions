with open("18_input.txt") as fin:
    data = fin.read()


def evaluate(expression):
    # Evaluates a string based on the new rules!

    # Current operation
    op = ""

    # Current value
    cur = 0

    # Value that we are accumulating inside the loop
    prevValue = ""

    # Loop through the expression, evaluating as we go
    index = 0
    while index < len(expression):
        char = expression[index]

        if char.isdigit():
            prevValue += char

        elif char in ["+", "*"]:
            # Evaluate the previous operation
            if op != "":
                if op == "+":
                    cur += int(prevValue)
                else:
                    cur *= int(prevValue)

            else:
                # No operations have been done before
                cur = int(prevValue)

            prevValue = ""
            op = char

        elif char == "(":
            # Balance the parentheses to get to the end
            ls = 1 # Lefts
            rs = 0 # Rights
            startIndex = index + 1

            while ls != rs and index < len(expression):
                index += 1
                ls += expression[index] == "("
                rs += expression[index] == ")"

            # Lefts and rights are balanced, evaluate what's inside
            insideParentheses = expression[startIndex:index]
            prevValue = evaluate(insideParentheses)

        index += 1

    # At the end, perform the operation
    if op != "":
        if op == "+":
            cur += int(prevValue)
        else:
            cur *= int(prevValue)

    return cur


ans = 0
for expression in data.split("\n"):
    expression = expression.replace(" ", "")
    ans += evaluate(expression)

print(ans)