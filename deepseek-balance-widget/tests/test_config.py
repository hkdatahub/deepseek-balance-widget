import os
import json
import tempfile
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import Config


def test_config_creates_defaults():
    tmp = tempfile.mkdtemp()
    cfg = Config(config_dir=tmp)
    assert cfg.get_refresh_interval() == 300
    assert cfg.get_api_key() is None


def test_config_save_and_load_api_key():
    tmp = tempfile.mkdtemp()
    cfg = Config(config_dir=tmp)
    cfg.set_api_key("sk-test-key-123")
    assert cfg.get_api_key() == "sk-test-key-123"

    cfg2 = Config(config_dir=tmp)
    assert cfg2.get_api_key() == "sk-test-key-123"


def test_config_refresh_interval():
    tmp = tempfile.mkdtemp()
    cfg = Config(config_dir=tmp)
    cfg.set_refresh_interval(600)
    assert cfg.get_refresh_interval() == 600
