# 스택


class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity # 스택 용량
        self.array = [None] * self.capacity # 요소 배열
        self.top = -1 # 상단의 인덱스
    # 스택의 공백 상태 인지
    def isEmpty(self):
        if self.top == - 1:
            return True
        else:
            return False        
    # 스택의 포화 상태 인지
    def isFull(self):
        return self.top == self.capacity - 1 # 비교 연산 결과를 바로 번환

    # 스택의 삽입 연산
    def push(self, e):
        #global top
        if not self.isFull(): # 포화상태가 아니면 스택에 추가하는 코드
            self.top += 1
            self.array[self.top] = e
        else:
            pass # overflow 예외는 처리하지 않음

    # 스택의 삭제 연산
    def pop(self):
        #global top
        if not self.isEmpty():
            self.top -=1
            return self.array[self.top+1]
        else:
            print("stack underflow")
            exit()

    # 스택의 peek() 연산 -> not empty의 경우 상단의 값을 리턴 해주고 삭제는 하지않는
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass

    # 스택의 요쇼 수를 반환하는 size() 연산
    def size(self):
        return self.top + 1

if __name__ == "__main__":
    s1 = ArrayStack(20) # 용량이 20인 ArrayStack 객체 s1 생성
    s2 = ArrayStack(100) # 용량이 100인 ArrayStack 객체 s2 생성
    s = ArrayStack(100)             # 스택 객체를 생성

    msg = input("문자열 입력: ")    # 문자열을 입력받음
    for c in msg :                  # 문자열의 각 문자 c에 대해
        s.push(c)                   # c를 스택에 삽입

    print("문자열 출력: ", end='')
    while not s.isEmpty():          # 스택이 공백상태가 아니라면
        print(s.pop(), end='')      # 하나의 요소를 꺼내서 출력
    print()
