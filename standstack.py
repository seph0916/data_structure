# * 연산자를 통해서 같은값을 나열하는 리스트로 만들 수 있다.
capacity = 10
array = [None] * capacity
top = -1

# 스택의 공백 상태 인지
def isEmpty():
    if top == - 1:
        return True
    else:
        return False

# 스택의 포화 상태 인지
def isFull():
    return top == capacity - 1 # 비교 연산 결과를 바로 번환

# 스택의 삽입 연산
def push(e):
    # global top
    if not isFull(): # 포화상태가 아니면 스택에 추가하는 코드
        top += 1
        array[top] = e
    else:
        print("stack overflow")
        exit()

# 스택의 삭제 연산
def pop():
    # global top
    if not isEmpty():
        top -=1
        return array[top+1]
    else:
        print("stack underflow")
        exit()

# 스택의 peek() 연산 -> not empty의 경우 상단의 값을 리턴 해주고 삭제는 하지않는
def peek():
    if not isEmpty():
        return array[top]
    else:
        pass

# 스택의 요쇼 수를 반환하는 size() 연산
def size():
    return top + 1