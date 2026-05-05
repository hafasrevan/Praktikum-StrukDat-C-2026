stack = []

stack.append('riot.games.com')
stack.append('steam.com')
stack.append('my.konami.net')
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

print("Size: ",len(stack))
