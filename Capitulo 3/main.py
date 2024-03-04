import sys

clients = [
    {
        'nombre':'Pablo',
        'compania':'Google',
        'email': 'pablo.google.com',
        'posicion':'Ingeniero de software'
    },
    {
        'nombre':'Juan',
        'compania':'Platzi',
        'email': 'juan.platzi.com',
        'posicion':'Desarrollador'
    },

]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Cliente ya existe en la lista de clientes')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {nombre} | {compania} | {email} | {posicion}'.format(
            uid=idx,
            nombre = client['nombre'],
            compania = client['compania'],
            email = client['email'],
            posicion = client['posicion']
        ))


def update_client(client_id, updated_client):
    global clients

    if len(clients) -1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Cliente no se encuentra en la lista de clientes')

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break

def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('Que te gustaria hacer hoy?')
    print('[L]istar clientes')
    print('[C]rear cliente')
    print('[A]actualizar cliente')
    print('[E]liminar cliente')
    print('[B]uscar cliente')
    
def _get_client_field(field_name):
    field = None
    while not field:
        field =  input('Cual es el(la) {} del cliente?'.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'nombre': _get_client_field('nombre'),
        'compania': _get_client_field('compania'),
        'email': _get_client_field('email'),
        'posicion': _get_client_field('posicion'),
    }

    return client

def _get_client_name():
    client_name = None
    while not client_name:
        client_name =  input('Cual es el nombre del cliente?')
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'nombre':_get_client_field('nombre'),
            'compania':_get_client_field('compania'),
            'email':_get_client_field('email'),
            'posicion':_get_client_field('posicion')
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'A':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()
    elif command == 'E':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'B':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('El cliente esta en el listado de clientes')
        else:
            print('El cliente: {} no esta en nuestro listado de clientes'.format(client_name))
    else:
        print('Comando invalido')