from homeassistant.helpers.entity import Entity
from homeassistant.const import ENERGY_KILO_WATT_HOUR

async def async_setup_entry(hass, entry, async_add_entities):
    api = hass.data["neoom"][entry.entry_id]["api"]
    site_id = hass.data["neoom"][entry.entry_id]["site_id"]
    async_add_entities([NeoomEnergySensor(api, site_id)], update_before_add=True)

class NeoomEnergySensor(Entity):
    def __init__(self, api, site_id):
        self.api = api
        self.site_id = site_id
        self._state = None

    @property
    def name(self):
        return f"Neoom Energy {self.site_id}"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return ENERGY_KILO_WATT_HOUR

    async def async_update(self):
        data = await self.api.get_latest_energy(self.site_id)
        self._state = data.get("energy")
