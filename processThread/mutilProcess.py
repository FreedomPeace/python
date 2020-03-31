import os
print("Process(%s) start ..."%os.getpid())
pid = os.fork()
if pid == 0 :
    print("I am child process (%s)and my parent process is (%s)",os.getpid(),
            os.getppid())
else:
    print(" I (%s) created child process is (%s)",os.getpid(),pid)
print("end")
