pattern = '@gmail.com'
with open('emails_filtered.txt', 'w+') as dest:
    with open('emails.txt', 'r') as em:
        for line in em.readlines():
            if line.endswith(pattern + '\n'):
                print(line, end='', file=dest)
