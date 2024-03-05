import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manejo de clientes"""
    pass

@clients.command()
@click.option('-n','--nombre', type=str, prompt=True, help='Nombre del cliente')
@click.option('-c','--compania', type=str, prompt=True, help='compania del cliente')
@click.option('-e','--email', type=str, prompt=True, help='email del cliente')
@click.option('-p','--puesto', type=str, prompt=True, help='puesto del cliente')
@click.pass_context
def create(ctx, nombre, compania, email, puesto):
    """Crear un nuevo cliente"""
    client = Client(nombre, compania, email, puesto)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """Lista de todos los clientes"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    click.echo('  ID  |  NOMBRE  | COMPANIA  |  EMAIL  |  PUESTO')
    click.echo('*'*100)
    for client in client_list:
        click.echo('{uid} | {nombre} | {compania} | {email} | {puesto}'.format(
            uid=client['uid'],
            nombre=client['nombre'],
            compania=client['compania'],
            email=client['email'],
            puesto=client['puesto']
        ))

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Actualizar clientes"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Cliente actualizado')
    else:
        click.echo('Cliente no encontrado')


def _update_client_flow(client):
    click.echo('Deja el campo vacio sino quieres modificar el valor')
    client.nombre =click.prompt('New nombre', type=str, default=client.nombre)
    client.compania =click.prompt('New compania', type=str, default=client.compania)
    client.email =click.prompt('New email', type=str, default=client.email)
    client.puesto =click.prompt('New puesto', type=str, default=client.puesto)

    return client


@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Eliminar un cliente"""
    client_service = ClientService(ctx.obj['clients_table'])

    if click.confirm('Estas seguro de que quieres eliminar al cliente con uid {}'.format(client_uid)):
        client_service.delete_client(client_uid)


all = clients