N, Q = map(int, input().split())
durations = [int(input()) for _ in range(N)]
queries = [int(input()) for _ in range(Q)]

time_ranges = []
current_time = 0

for i in range(N):
    start = current_time
    end = current_time + durations[i] - 1
    time_ranges.append((start, end))
    current_time = end + 1

for t in queries:
    for i in range(N):
        if time_ranges[i][0] <= t <= time_ranges[i][1]:
            print(i + 1)
            break