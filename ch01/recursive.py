# 후위 표현법 계산 코드 (재귀함수 이용)

def evaluate_postfix(tokens):
    if not tokens:
        return None

    token = tokens.pop()
    
    if token.isnumeric():
        return float(token)
    else:
        operand2 = evaluate_postfix(tokens)
        operand1 = evaluate_postfix(tokens)
        
        if token == '+':
            return operand1 + operand2
        elif token == '-':
            return operand1 - operand2
        elif token == '*':
            return operand1 * operand2
        elif token == '/':
            return operand1 / operand2
        elif token == '^':
            return operand1 ** operand2

# 후위 표기법 수식 입력
postfix_expression = "2 3 4 + *"
tokens = postfix_expression.split()
result = evaluate_postfix(tokens.copy())

# 결과 출력
print("후위 표기법 계산 결과:", result)

# 재귀 버전
def find_max_recursive(data):
    if len(data) == 1:
        return data[0]
    else:
        sub_max = max(data[1:])
        if data[len(data)-1] > sub_max:
            return data[len(data)-1]
        else:
            return sub_max

# 반복 버전
def find_max_iterative(data):
    max_value = data[0]
    for num in data:
        if num > max_value:
            max_value = num
    return max_value

# 공차가 3인 등차수열의 n 번째 원소를 구하는 프로그램을 코딩해 보기
# n == 1인건 첫째항이 1인듯?
def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + 3
# print("공차가 3인 등차수열의 5번째 원소값은?",seq(5))

# 하노이의 타워 문제를 코딩해보기
#def move(n, src, tmp, dest):