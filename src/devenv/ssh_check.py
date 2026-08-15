from pathlib import Path

def get_ssh_status():
    
    home = Path.home()
    ssh_dir = home / ".ssh"

    id_ed25519_key = ssh_dir / "id_ed25519"
    rsa_key = ssh_dir / "id_rsa"

    if id_ed25519_key.exists():
        return {
            "has_key": True,
            "key_path": str(id_ed25519_key)
        }
    if rsa_key.exists():
        return {
            "has_key": True,
            "key_path": str(rsa_key)
        }
    return{
        "has_key": False,
        "key_path": None
    }

# print(get_ssh_status())
    
