from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.settings_sync import setup
from src.settings_sync.extension import SettingsSync


class TestSettingsSyncExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = SettingsSync(app_instance.api)
        exported = ext.export_profile({"font_size": 14}, ["python", "prettier"])
        imported = ext.import_profile(exported)
        assert imported["settings"]["font_size"] == 14
        assert "python" in imported["extensions"]
