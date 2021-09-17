input = input("Please input your username: ")

username = input[:input.index("@")]
domain = input[input.index("@") + 1:input.index(".")]

print(username)
print(domain)