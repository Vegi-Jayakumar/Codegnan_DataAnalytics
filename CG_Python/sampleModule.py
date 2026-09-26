'''
A Module is a python file (.py) containing usable logic.
'''

def details(name,place):
    """
    prints details
    """
    print(f"Name:{name}")
    print(f"Place: {place}")

data = {
    'ids': [12,32,43,23],
    'names': ['Saketh','Akash','Sunil','Neha'],
    'batches': ['PFS','JFS','DA','DS','AAA']
}

# if __name__ == "__main__":  #we call __name__ as dunder name
#     details('jayakumar','Visakhapatnam')
#     print(data)
#     print(__name__)

print(__name__)