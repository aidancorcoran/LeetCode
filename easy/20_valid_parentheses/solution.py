def solution( s: str ) -> bool:
    # So we have a string of parentheses, we have to check every single one and push them onto a stack
    stack = []
    bracket_map = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for bracket in s:
        if bracket in bracket_map.values(): # A closing bracket
            if not stack:
                return False
            else:
                if bracket_map[stack.pop()] != bracket:
                    return False
        else: # An opening bracket
            stack.append(bracket)

    if stack:
        return False
    return True
                

def main():
    s = "()[]{}"

    print(solution(s))

if __name__ == "__main__":
    main()



# So we have a char array of brackets, for every opening bracket we see we need to push it on the stack, if we
# see a closing bracket and there is nothing on the stack or it doesnt match the value popped off we just return false