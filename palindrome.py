def palindrome_finder(string):
    palindrome = True
    start = 0
    end = -1
    while start < len(string)/2:
        if string[start] == string[end]:
            start = start + 1
            end = end - 1
            continue
        else:
            palindrome = False
            break
    print palindrome

palindrome_finder("radar")
palindrome_finder("cat")

