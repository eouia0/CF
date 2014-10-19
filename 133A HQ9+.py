def hq9(string):
    for item in string:
        if item in ["H","Q","9"]:
            return "YES"
    return "NO"

print hq9(raw_input())