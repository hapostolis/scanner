import socket, sys, configparser, time
from threading import Thread as z
def main():
    go = 1
    def count(type,num, arg, sec):
        r = len(arg)
        if r == 1:
            j = " " * 8
        elif r == 2:
            j = " " * 7
        elif r == 3:
            j = " " * 6
        elif r == 4:
            j = " " * 5
        elif r == 5:
            j = " " * 4
        if type == "v0":
            print("\033[41mProcess %s     Open     %s%s%s\033[0m" % (num,arg,j,sec))
        else:
            print("\033[41mOpen      %s%s%s\033[0m" % (arg,j,sec))
    config=configparser.ConfigParser()
    config.read("ports.ini")
    v = 0
    file=open("report.txt", "a")
    target=sys.argv[1]
    if "-v" in sys.argv[2:]:
        v = 1
    if "-vv" in sys.argv[2:]:
        v = 2
    def q():
        for o in range(0,13107):
            if go != 1:
                break
            if v == 2:
                for g in range(0,13107, 4000):
                    if o == g and o!=0:
                        print("\033[92mprocess 0 reached port: %s (range=0~13107) %d more\033[0m" % (str(o), 13107-o))
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
            b = s.connect_ex((target, o))
            last_port = o
            test = str(o)
            if b==0:
                try:
                    a = config[str(o)]["d"]
                except KeyError:
                    a = "Unknown"
                if v == 0:
                    count("v1", 0, str(o), a)
                else:
                    count("v0",0, str(o), a)
            s.close()
        print("[-] Process 0: Done")
    def w():
        for o in range(13107,26214):
            if go != 1:
                break
            if v == 2:
                for g in range(13107,26214, 4000):
                    if o == g and o != 13107:
                        print("\033[93mprocess 1 reached port: %s (range=13107~26214) %d more\033[0m" % (str(o), 26214-o))
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
            b = s.connect_ex((target, o))
            last_port = o
            if b==0:
                try:
                    a = config[str(o)]["d"]
                except KeyError:
                    a = "Unknown"
                if v == 0:
                    count("v1", 0, str(o), a)
                else:
                    count("v0", 1, str(o), a)
            s.close()
        print("[-] Process 1: Done")
    def e():
        for o in range(26214,39321):
            if go!=1:
                break
            if v == 2:
                for g in range(26214,39321, 4000):
                    if o == g and o != 26214:
                        print(" " * 42 + " TCP       26214~39321          test              test2")
#                        print("\033[94mprocess 2 reached port: %s (range=26214~39321) %d more\033[0m" % (str(o), 39321-o))
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
            b = s.connect_ex((target, o))
            last_port = o
            if b==0:
                try:
                    a = config[str(o)]["d"]
                except KeyError:
                    a = "Unknown"
                if v == 0:
                    count("v1", 0, str(o), a)
                else:
                    count("v0", 2, str(o), a)
            s.close()
        print("[-] Process 2: Done")
    def r():
        for o in range(39321,52428):
            if go!=1:
                break
            if v == 2:
                for g in range(39321,52248, 4000):
                    if o == g and o != 39321:
                        print("\033[95mprocess 3 reached port: %s (range=39321~52428) %d more\033[0m" % (str(o), 52248-o))
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
            b = s.connect_ex((target, o))
            last_port = o
            if b==0:
                try:
                    a = config[str(o)]["d"]
                except KeyError:
                    a = "Unknown"
                if v == 0:
                    count("v1", 0, str(o), a)
                else:
                    count("v0", 3, str(o), a)
            s.close()
        print("[-] Process 3: Done")
    def t():
        for o in range(52428,65536):
            if go!= 1:
                break
            if v == 2:
                for g in range(52428,65535, 4000):
                    if o == g and o != 52428:
                        print("\033[93mprocess 4 reached port: %s (range=52428~65535) %d more\033[0m" % (str(o), 65535-o))
                        print("+" * 30)
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
            b = s.connect_ex((target, o))
            last_port = o
            if b==0:
                try:
                    a = config[str(o)]["d"]
                except KeyError:
                    a = "Unknown"
                if v == 0:
                    count("v1", 0, str(o), a)
                else:
                    count("v0", 4, str(o), a)
            s.close()
        print("[-] Process 4: Done")
    print("Start scanning:  %s" % time.strftime("%A %H:%M:%S"))
    print("+-" * 20)
    if v==0:
        print("\033[1mStatus    Port     Service    Protocol\033[0m")
    elif v==1 or v==2:
        print("\033[1mProcess       Status   Port     Service   Protocol      Range           Current port    Ports left\033[0m")
    try:
        a = z(target=q)
        b = z(target=w)
        c = z(target=e)
        d = z(target=r)
        e = z(target=t)
        a.start()
        time.sleep(1)
        b.start()
        time.sleep(1)
        c.start()
        time.sleep(1)
        d.start()
        time.sleep(1)
        e.start()
    except KeyboardInterrupt:
        go = 0
        sys.exit()
main()
