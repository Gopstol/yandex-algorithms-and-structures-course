"""
Дек реализован по сути так же, как и очередь на кольцевом буфере в 9 уроке 2 спринта.
Соответственно сложность всех операций отдельно составляет О(1), так как в функциях нет никаких циклов и переборов.
Временная сложность всей программы, выполняющей n команд - О(n)
Простраственная сложность - О(m), т.к. работаем с массивом фиксированной длины m
"""


class Deque:
    def __init__(self, max_size):
        self.max_size: int = max_size
        self.deck: list = [0] * self.max_size
        self.head: int = 0
        self.tail: int = 1
        self.size: int = 0

    def push_back(self, value):
        if self.size == self.max_size:
            raise IndexError
        else:
            self.deck[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            raise IndexError
        else:
            self.deck[self.head] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError
        else:
            self.tail = (self.tail - 1) % self.max_size
            done = self.deck[self.tail]
            self.deck[self.tail] = 0
            self.size -= 1
            return done

    def pop_front(self):
        if self.size == 0:
            raise IndexError
        else:
            self.head = (self.head + 1) % self.max_size
            done = self.deck[self.head]
            self.deck[self.head] = 0
            self.size -= 1
            return done


def main():
    n = int(input())
    m = int(input())
    my_deque = Deque(m)
    command_queue: list = []

    for i in range(n):
        command_queue.append(input())

    for command in command_queue:
        try:
            if command == "pop_back":
                print(my_deque.pop_back())
            elif command == "pop_front":
                print(my_deque.pop_front())
            else:
                if command.split()[0] == "push_back":
                    my_deque.push_back(command.split()[1])
                else:
                    my_deque.push_front(command.split()[1])

        except IndexError:
            print('error')


if __name__ == "__main__":
    main()
