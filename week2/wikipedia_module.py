#Install the Wikipedia module from PyPi and recreate the examples on the PyPi page



import wikipedia
print wikipedia.summary("Wikipedia")

wikipedia.search("Barack")


ny = wikipedia.page("New York City")

print ny.title

print ny.url

print ny.content

print ny.links[0]

wikipedia.set_lang("fr")
print wikipedia.summary("Facebook", sentences=1)