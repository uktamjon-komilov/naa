class Manager:
    def get(self, *args, **kwargs):
        return ""
    
    def all(self, *args, **kwargs):
        return ""
    
    def filter(self, *args, **kwargs):
        return ""
    
    def order_by(self, *args, **kwargs):
        return ""
    

class Model:
    print("...")
    objects = Manager()
    print("...")


class Book(Model):
    title = String(255)
    description = Text()

b = Book()
b.objects.all()
b.objects.filter()
b.objects.get()