class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde A")

class C(A):
    def hablar(self):
        print("Hola desde A")

class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D() ###Heredemos desde donde heredemos siempre tendra prioridad desde donde estamos llamando 
d.hablar()###Si no encuentra en D, se ira por B por ser la primer clase a pasar, sino C y finalmente por A porque a B le pasamos la A
print(D.mro()) 