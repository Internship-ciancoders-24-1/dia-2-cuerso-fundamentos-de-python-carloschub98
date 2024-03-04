import sys

clients = 'pablo,juan,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
    else:
        print('Cliente ya existe en la lista de clientes')
    _add_coma()


def list_clients():
    global clients
    print(clients)

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name)
    else:
        print('Cliente no se encuentra en la lista de clientes')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',','')
    else:
        print('Cliente no se encuentra en la lista de clientes')

def search_client(client_name):
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_coma():
    global clients
    clients += ','

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('Que te gustaria hacer hoy?')
    print('[L]istar clientes')
    print('[C]rear cliente')
    print('[A]actualizar cliente')
    print('[E]liminar cliente')
    print('[B]uscar cliente')
    

def _get_client_namet():
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
        client_name = _get_client_namet()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'A':
        client_name = _get_client_namet()
        update_client_name = input('Cual es el nombre del cliente a actualizar?')
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'E':
        client_name = _get_client_namet()
        delete_client(client_name)
        list_clients()
    elif command == 'B':
        client_name = _get_client_namet()
        found = search_client(client_name)
        if found:
            print('El cliente esta en el listado de clientes')
        else:
            print('El cliente: {} no esta en nuestro listado de clientes'.format(client_name))
    else:
        print('Comando invalido')