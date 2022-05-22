import os
from pathlib import Path

from skyplane.config import SkyplaneConfig

# paths
skyplane_root = Path(__file__).parent.parent
config_root = Path("~/.skyplane").expanduser()
config_root.mkdir(exist_ok=True)

if "SKYPLANE_CONFIG" in os.environ:
    config_path = Path(os.environ["SKYPLANE_CONFIG"]).expanduser()
else:
    config_path = config_root / "config"

aws_config_path = config_root / "aws_config"
azure_config_path = config_root / "azure_config"
azure_sku_path = config_root / "azure_sku_mapping"
gcp_config_path = config_root / "gcp_config"

key_root = config_root / "keys"
tmp_log_dir = Path("/tmp/skyplane")
tmp_log_dir.mkdir(exist_ok=True)

# header
def print_header():
    header = "\n"
    header += """=================================================
  ______  _             _                 _     
 / _____)| |           | |               | |    
( (____  | |  _  _   _ | |  _____   ____ | |  _ 
 \____ \ | |_/ )| | | || | (____ | / ___)| |_/ )
 _____) )|  _ ( | |_| || | / ___ || |    |  _ ( 
(______/ |_| \_) \__  | \_)\_____||_|    |_| \_)
                (____/                          
================================================="""
    header += "\n"
    print(header, flush=True)


# definitions
KB = 1024
MB = 1024 * 1024
GB = 1024 * 1024 * 1024
if config_path.exists():
    cloud_config = SkyplaneConfig.load_config(config_path)
else:
    cloud_config = SkyplaneConfig(False, False, False)
is_gateway_env = os.environ.get("SKYPLANE_IS_GATEWAY", None) == "1"