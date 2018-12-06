from collections import Counter

paragraph = """Paramiko is a combination of the Esperanto words for paranoid and friend. It's a module for Python 2.7/3.4+ that implements the SSH2 protocol for secure encrypted and authenticated connections to remote machines. Unlike SSL aka TLS, SSH2 protocol does not require hierarchical certificates signed by a powerful central authority. You may know SSH2 as the protocol that replaced Telnet and rsh for secure access to remote shells, but the protocol also includes the ability to open arbitrary channels to remote services across the encrypted tunnel this is how SFTP works, for example)."""

list_of_words = paragraph.split()
wc = Counter(list_of_words)


#def by_values(word):
#    """callable """
#    return wc[word]


# lambda arg1, arg2,.... : expression

for key in sorted(wc, key=lambda word: wc[word], reverse=True):
    print(key, ':', wc[key])
