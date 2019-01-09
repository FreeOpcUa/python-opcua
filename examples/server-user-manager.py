import sys
sys.path.insert(0, "..")
import time

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


from opcua import ua, Server

def simple_user_manager(isession, name, pwd):
    # simple user manager that only allows my_user:my_password to log in
    if name == "my_user" and pwd == b"my_password":
        return True
    return False

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    server.user_manager.set_user_manager(simple_user_manager)

    # starting!
    server.start()

    try:
        embed()
    finally:
        server.stop()    
