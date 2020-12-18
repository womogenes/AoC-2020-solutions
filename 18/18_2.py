with open("18_input.txt") as fin:
    data = fin.read()


def evaluate(expression):
    #print("expression:", expression)

    # Goal: get rid of all the addition signs
    multiplicands = []

    # These still exist
    prevValue = ""

    # Current index
    index = 0

    # Boolean to tell whether the last argument is part of a sum
    lastIsAddition = False

    while index < len(expression):
        char = expression[index]

        if char.isdigit():
            prevValue += char

        elif char == "+":
            # Find where it ends!
            summands = [int(prevValue)]
            prevValue = ""
            index += 1
            
            while index < len(expression):
                char = expression[index]

                if char.isdigit():
                    prevValue += char

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

                elif char == "*":
                    break

                elif char == "+":
                    summands.append(int(prevValue))
                    prevValue = ""

                index += 1

            if index == len(expression):
                lastIsAddition = True

            if prevValue != "":
                summands.append(int(prevValue))

            #print("summands:", summands)

            multiplicands.append(sum(summands))
            prevValue = ""

        elif char == "*":
            multiplicands.append(int(prevValue))
            prevValue = ""

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
            #print("inside:", insideParentheses)
            prevValue = evaluate(insideParentheses)

        index += 1

    # Get the last multiplicand
    if prevValue != "" and not lastIsAddition:
        multiplicands.append(int(prevValue))

    #print(multiplicands)

    prod = 1
    for i in multiplicands:
        prod *= i

    return prod


ans = 0
for expression in data.split("\n"):
    expression = expression.replace(" ", "")
    ans += evaluate(expression)

print(ans)

#print(evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))