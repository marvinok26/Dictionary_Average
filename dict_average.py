if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0
    if query_name in student_marks:
        for i in student_marks[query_name]:
            total += i
    mean = total / len(student_marks[query_name])
    
    print("{:0.2f}".format(mean))
