from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


import json

class SettingsSync(Extension):
    """Synchronize settings, keybindings, and extensions across devices."""

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("Settings Sync extension initialised.")

    def export_profile(self, settings: dict, extensions: list[str]) -> str:
        payload = {
            "version": "1.0",
            "settings": settings,
            "extensions": extensions
        }
        return json.dumps(payload, indent=2)

    def import_profile(self, raw_json: str) -> dict:
        data = json.loads(raw_json)
        return {
            "settings": data.get("settings", {}),
            "extensions": data.get("extensions", [])
        }

    def install(self) -> None:
        self.api.logger.info("Settings Sync extension installed.")
