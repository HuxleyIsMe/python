# This is a side quest into shells/terminals and what even are they?

So recently i had had a little deep dive into shell scripting however i had skipped over the terminal, i think kinda taking it fro granted and assuming that i already kinda new what there was to know:

- its an interface to enable me to interact with my computer.

> *The terminal emulator is a graphical application whose role it is to interpret data coming from the shell and display it on screen. This display is often textual but not always.*

What really struck me here was 'graphical' its still a GUI, which means we can still have some fun rendering... 


The emmulator sits in front of the shell, it communicates bi directionally with the shell using a 'psudo-terminal' abbreviated as 'pty'. 

The shell is using Ansi char codes to communicate to the shell.
## resources:

- [Build a terminal emulator](https://medium.com/@artur.araqelyan.0001/developing-terminal-emulator-in-c-9f3d2007e7c1)
- [Anatomy of a terminal](https://poor.dev/blog/terminal-anatomy/)
- [Shell lingo from IBM](https://www.ibm.com/docs/en/aix/7.2.0?topic=administration-operating-system-shells)
- [Creating a terminal emulator](https://www.google.com/search?q=create+a+terminal+emulator&sca_esv=7f3b3e58f08bcb9f&rlz=1C5OZZY_enGB1128GB1128&sxsrf=AE3TifMIZMBh3b6hYj4Jzs0Q-BGI7jSAnw%3A1748247826106&ei=EiU0aPecBqGwwPAPj83b8Ag&ved=0ahUKEwj37Z3V2sCNAxUhGBAIHY_mFo4Q4dUDCBA&uact=5&oq=create+a+terminal+emulator&gs_lp=Egxnd3Mtd2l6LXNlcnAiGmNyZWF0ZSBhIHRlcm1pbmFsIGVtdWxhdG9yMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFSNQjUABYuyJwAXgBkAEAmAGZAaAB5ReqAQQxLjI1uAEDyAEA-AEBmAIboALeGKgCE8ICBxAjGCcY6gLCAhMQABiABBhDGLQCGIoFGOoC2AEBwgIZEC4YgAQYQxjUAhi0AhjIAxiKBRjqAtgBAcICBBAjGCfCAgoQABiABBhDGIoFwgILEC4YgAQY0QMYxwHCAgUQABiABMICChAjGIAEGCcYigXCAg0QLhiABBhDGNQCGIoFwgIKEC4YgAQYQxiKBcICCxAAGIAEGJECGIoFwgIKEAAYgAQYFBiHAsICCBAAGBYYChgemAML8QUKVLr8NVfSh7oGBggBEAEYAZIHBDEuMjagB5m6AbIHBDAuMja4B9MYwgcJMC4xMi4xMy4yyAdn&sclient=gws-wiz-serp#fpstate=ive&vld=cid:f0906a42,vid:r41AS-SHYMM,st:0)