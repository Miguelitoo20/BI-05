import subprocess
result = subprocess.run(['cmd', '/c', 'echo', 'Hola Mundo'], capture_output=True, text=True)
print(result.stdout)
