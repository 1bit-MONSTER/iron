import sys, time, inspect, json

# The current call stack; for each active function call, we store (func_identifier, start_time)
call_stack = []

# The cumulative time spent in each call stack path
# Map {function identifier: tuple (cumulative_time, {sub_call_function_identifier: cumulative_time, ...}) }
time_per_path = [0.0, {}]


def profile_call(frame, event, arg):
    global call_stack

    timestamp = time.perf_counter()

    func_name = frame.f_code.co_name
    filename = frame.f_code.co_filename
    line_no = frame.f_lineno
    func_identifier = f"{str(frame.f_code.co_filename)}:{frame.f_code.co_firstlineno}:{frame.f_code.co_name}"

    if event == "call":
        call_stack.append((func_identifier, timestamp))
    elif event == "return":
        if 0 == len(call_stack):
            return
        last_func_identifier, start_time = call_stack[-1]
        if last_func_identifier != func_identifier:
            print(call_stack)
            raise RuntimeError(f"Function return mismatch: expected {last_func_identifier}, got {func_identifier}")
        elapsed = timestamp - start_time

        this_path_time = time_per_path
        for f, _ in call_stack:
            this_path_time = this_path_time[1].setdefault(f, [0.0, {}])
        this_path_time[0] += elapsed

        call_stack.pop()


def enable_profiling():
    sys.setprofile(profile_call)


def store_profile(path):
    sys.setprofile(None)
    with open(path, "w") as f:
        json.dump(time_per_path[1], f, indent=2)

