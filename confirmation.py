import jsonmodules

jsonmodules.greet()

temp=input
data=jsonmodules.loadjson(temp)

inpu=input("aaa")
data.append(inpu)
jsonmodules.updatejson(data)