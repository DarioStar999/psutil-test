import psutil as ps

def getpid(process_name):
    for proc in ps.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == process_name.lower():
            return print(f"Pid: {proc.info['pid']}")
    return None
def getTempSensor():
    return ps.sensors_temperatures()
def getCPUUsage():
    return ps.cpu_percent()
def getMemoryUsage():
    return ps.virtual_memory().percent
def getDiskUsage():
    return ps.disk_usage('/')
def getProcessList():
    return '\n '.join([f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_percent']}%" 
                      for proc in ps.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])])


cpu_usage = getCPUUsage()
memory_usage = getMemoryUsage()
disk_usage = getDiskUsage()
process_list = getProcessList()

while True:
    select = input("""
    Choose an option:
    1) CPU Usage
    2) Memory Usage
    3) Disk Usage
    4) Process List
    5) Process Pid
    6) Exit
        Choice: """)
    
    if select == "1":
        print(f"CPU Usage: {cpu_usage}%")
    elif select == "2":
        print(f"Memory Usage: {memory_usage}%")
    elif select == "3":
        print(f"Disk Usage: {disk_usage}%")
    elif select == "4":
        print(f"Process List:\n{process_list}")
    elif select == "5":
        getpid(process_name=input("process_name: "))
    elif select == "6":
        print("exit")
        break
    else:
        print("Invalid choice!")