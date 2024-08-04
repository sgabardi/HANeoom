from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .neoom_api import NeoomAPI  # Angenommen, du hast deine API-Klasse in neoom_api.py

async def async_setup(hass: HomeAssistant, config: dict):
    # Global setup tasks.
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Setup specific configurations
    hass.data.setdefault("neoom", {})
    api = NeoomAPI(entry.data["api_key"])
    hass.data["neoom"][entry.entry_id] = {
        "api": api,
        "site_id": entry.data["site_id"]
    }
    
    # Sensor-Setup (Beispiel)
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    
    return True
