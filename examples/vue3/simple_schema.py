from trame.app import get_server
from trame.widgets import formkit
from trame.ui.html import DivLayout

# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller


def submit_form(form_data):
    print(form_data)


state.formkit_schema = [
    {"$el": "h1", "children": "Register"},
    {
        "$formkit": "text",
        "name": "email",
        "label": "Email",
        "help": "This will be used for your account.",
        "validation": "required|email",
    },
    {
        "$formkit": "password",
        "name": "password",
        "label": "Password",
        "help": "Enter your new password.",
        "validation": "required|length:5,16",
    },
    {
        "$formkit": "password",
        "name": "password_confirm",
        "label": "Confirm password",
        "help": "Enter your new password again to confirm it.",
        "validation": "required|confirm",
        "validationLabel": "password confirmation",
    },
    {
        "$cmp": "FormKit",
        "props": {
            "name": "eu_citizen",
            "type": "checkbox",
            "id": "eu",
            "label": "Are you a european citizen?",
        },
    },
    {
        "$formkit": "select",
        "if": "$get(eu).value",
        "name": "cookie_notice",
        "label": "Cookie notice frequency",
        "options": {
            "refresh": "Every page load",
            "hourly": "Ever hour",
            "daily": "Every day",
        },
        "help": "How often should we display a cookie notice?",
    },
]

# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------

with DivLayout(server) as layout:
    with formkit.FormKit(type="form", submit=(submit_form, "[$event]")):
        formkit.FormKitSchema(
            schema=("state.formkit_schema",),
        )

if __name__ == "__main__":
    server.start()
