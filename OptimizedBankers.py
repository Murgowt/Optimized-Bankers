def bankers(processes,resources,currently_allocated, max_need ,available):
    print(processes,'p')
    if(processes==0):
        print('Deadlock Not Avoidable.')
        exit()        
    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {max_need[i]} is executing")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    
        if not safe:
            left=[]
            for i in range(processes):
                if  running[i]:
                    print(i+1,max_need[i])
                    left.append(i)
            maxi=0
            maxs=0
            for i in left:
                temp=0
                
                for j in range(resources):
                    temp+=max_need[i][j] - currently_allocated[i][j]
                if temp>maxs:
                    maxs=temp
                    maxi=i
            print("maxs",maxs,maxi)
            #print("left",left)
            #print("the processes are in an unsafe state.")
            ca=[]
            mn=[]
            allocated = [0] * resources
            for j in range(resources):
                available[j] += currently_allocated[maxi][j]
            for i in left:
                if i!=maxi:
                    ca.append(currently_allocated[i])
                    mn.append(max_need[i])
            available=bankers(len(left)-1,resources,ca,mn,available)
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j]  > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {max_need[i]} is executing")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                else:
                    print(f"process {max_need[i]} cannot be avoided.Hence we need to supply more resources")
            break
            
        #print(f"the process is in a safe state.\navailable resources : {available}\n")
    return available
def main():
    processes = int(input("number of processes : "))
    resources = int(input("number of resources : "))
   #max_resources = [ int(i) for i in input("maximum resources(instances of each Resource) : ").split()]

    print("\n-- allocated resources for each process --")
    currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]
    print(currently_allocated)
    print("\n-- maximum resources for each process --")
    max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\ntotal allocated resources : {allocated}")

    available =[ int(i) for i in input("Available Resources : ").split()]
    print(f"total available resources : {available}\n")

    available=bankers(processes,resources,currently_allocated, max_need,available)
    print(f"\navailable resources : {available}\n")

if __name__ == '__main__':
    main()
