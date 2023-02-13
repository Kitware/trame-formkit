def setup(server, **kargs):
    client_type = "vue2"
    if hasattr(server, "client_type"):
        client_type = server.client_type

    if client_type == "vue3":
        from . import vue3

        server.enable_module(vue3)
    else:
        raise TypeError(
            f"Trying to initialize trame_formkit with unsupported client_type={client_type}"
        )
