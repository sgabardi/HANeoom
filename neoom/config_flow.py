import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

class NeoomConfigFlow(config_entries.ConfigFlow, domain="neoom"):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return NeoomOptionsFlow(config_entry)

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Hier könntest du zusätzlich die Eingaben validieren, z.B. ob die API erreichbar ist.
            return self.async_create_entry(title="Neoom", data=user_input)
        
        data_schema = vol.Schema({
            vol.Required("api_key"): str,
            vol.Required("site_id"): str
        })
        
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)

class NeoomOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Required("api_key", default=self.config_entry.options.get("api_key")): str,
            vol.Required("site_id", default=self.config_entry.options.get("site_id")): str
        })
        
        return self.async_show_form(step_id="init", data_schema=data_schema)
