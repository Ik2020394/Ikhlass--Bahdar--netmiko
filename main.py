print("Hello, Git!")
from netmiko import ConnectHandler

def acces_netmiko():
    router = {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    with ConnectHandler(**router) as ssh:
        
        clock = ssh.send_command("show clock")
        print(clock)

        
        interfaces = ssh.send_command("show ip interface brief")
        with open("interfaces.txt", "w") as f:
            f.write(interfaces)

def dire_bonjour():
    print("Hello, Git!")

dire_bonjour()

def dire_salut():
    print("Salut, Git!")

dire_salut()
