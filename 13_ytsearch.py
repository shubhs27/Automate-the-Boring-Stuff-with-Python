import webbrowser, sys, pyperclip

sys.argv    # ['ytsearch.py', 'best', 'programmers']

if len(sys.argv)>1:
    search= ' '.join(sys.argv[1:])     # 'best programmers'
else:
    search= pyperclip.paste()

webbrowser.open('https://www.youtube.com/results?search_query='+search)